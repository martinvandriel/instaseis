#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Graphical user interface for Instaseis.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2013-2014
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import absolute_import

from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
# Default to antialiased drawing.
pg.setConfigOptions(antialias=True, foreground=(50, 50, 50), background=None)


from glob import iglob
import imp
import inspect
from mpl_toolkits.basemap import Basemap
from obspy.imaging.mopad_wrapper import Beach
from obspy.core.util.geodetics import locations2degrees
from obspy.taup.taup import getTravelTimes
import os
import sys

from instaseis import InstaSeisDB, Source, Receiver, FiniteSource

SCALING_FACTOR = 1E16


def compile_and_import_ui_files():
    """
    Automatically compiles all .ui files found in the same directory as the
    application py file.
    They will have the same name as the .ui files just with a .py extension.

    Needs to be defined in the same file as function loading the gui as it
    modifies the globals to be able to automatically import the created py-ui
    files. Its just very convenient.
    """
    directory = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    for filename in iglob(os.path.join(directory, '*.ui')):
        ui_file = filename
        py_ui_file = os.path.splitext(ui_file)[0] + os.path.extsep + 'py'
        if not os.path.exists(py_ui_file) or \
                (os.path.getmtime(ui_file) >= os.path.getmtime(py_ui_file)):
            from PyQt4 import uic
            print "Compiling ui file: %s" % ui_file
            with open(py_ui_file, 'w') as open_file:
                uic.compileUi(ui_file, open_file)
        # Import the (compiled) file.
        try:
            import_name = os.path.splitext(os.path.basename(py_ui_file))[0]
            globals()[import_name] = imp.load_source(import_name, py_ui_file)
        except ImportError, e:
            print "Error importing %s" % py_ui_file
            print e.message


class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Injected by the compile_and_import_ui_files() function.
        self.ui = qt_window.Ui_MainWindow()  # NOQA
        self.ui.setupUi(self)

        label = {"z": "vertical", "e": "east", "n": "north"}
        for component in ["z", "n", "e"]:
            p = getattr(self.ui, "%s_graph" % component)
            p.setLabel("left", "Displacement", units="m")
            p.setLabel("bottom", "Time since event", units="s")

            p.setTitle(label[component].capitalize() + " component")

        self.ui.n_graph.setXLink(self.ui.e_graph)
        self.ui.n_graph.setXLink(self.ui.z_graph)
        self.ui.e_graph.setXLink(self.ui.z_graph)
        self.ui.n_graph.setYLink(self.ui.e_graph)
        self.ui.n_graph.setYLink(self.ui.z_graph)
        self.ui.e_graph.setYLink(self.ui.z_graph)

        # Set some random mt at startup.
        m_rr = 4.71E17 / SCALING_FACTOR
        m_tt = 3.81E15 / SCALING_FACTOR
        m_pp = -4.74E17 / SCALING_FACTOR
        m_rt = 3.99E16 / SCALING_FACTOR
        m_rp = -8.05E16 / SCALING_FACTOR
        m_tp = -1.23E17 / SCALING_FACTOR
        self.ui.m_rr.setValue(m_rr)
        self.ui.m_tt.setValue(m_tt)
        self.ui.m_pp.setValue(m_pp)
        self.ui.m_rt.setValue(m_rt)
        self.ui.m_rp.setValue(m_rp)
        self.ui.m_tp.setValue(m_tp)

        self.instaseis_db = None
        self.finite_source = None

        self.plot_map()
        self.plot_mt()
        self.update()

    @property
    def focmec(self):
        if self.ui.source_tab.currentIndex() == 0:
            return [float(self.ui.m_rr.value()), float(self.ui.m_tt.value()),
                    float(self.ui.m_pp.value()), float(self.ui.m_rt.value()),
                    float(self.ui.m_rp.value()), float(self.ui.m_tp.value())]
        elif self.ui.source_tab.currentIndex() == 1:
            source = Source.from_strike_dip_rake(
                latitude=float(self.ui.source_latitude.value()),
                longitude=float(self.ui.source_longitude.value()),
                depth_in_m=float(self.source_depth) * 1000.0,
                strike=float(self.ui.strike_slider.value()),
                dip=float(self.ui.dip_slider.value()),
                rake=float(self.ui.rake_slider.value()),
                M0=1)
            return [source.m_rr, source.m_tt,
                    source.m_pp, source.m_rt,
                    source.m_rp, source.m_tp]

    def plot_mt(self):
        self.mpl_mt_figure = self.ui.mt_fig.fig
        self.mpl_mt_ax = self.mpl_mt_figure.add_axes([0.0, 0.0, 1.0, 1.0])
        self.mpl_mt_ax.set_axis_off()
        self.mpl_mt_figure.patch.set_alpha(0.0)
        self.mpl_mt_figure.set_facecolor('None')

        self._draw_mt()

    def _draw_mt(self):
        if not hasattr(self, "mpl_mt_ax"):
            return

        try:
            self.bb.remove()
        except:
            pass

        self.bb = Beach(self.focmec, xy=(0, 0), width=200, linewidth=1,
                        facecolor="red")
        self.mpl_mt_ax.add_collection(self.bb)
        self.mpl_mt_ax.set_xlim(-105, 105)
        self.mpl_mt_ax.set_ylim(-105, 105)
        self.mpl_mt_figure.canvas.draw()

    def plot_map(self):
        self.mpl_map_figure = self.ui.map_fig.fig
        self.mpl_map_ax = self.mpl_map_figure.add_axes([0.01, 0.01, .98, .98])
        self.mpl_map_ax.set_title("Left click: Set Receiver; Right click: Set "
                                  "Source")

        self.map = Basemap(projection='moll', lon_0=0, resolution="c",
                           ax=self.mpl_map_ax)
        self.map.drawmapboundary(fill_color='#cccccc')
        self.map.fillcontinents(color='white', lake_color='#cccccc', zorder=0)
        self.mpl_map_figure.patch.set_alpha(0.0)

        self.mpl_map_figure.canvas.mpl_connect(
            'button_press_event', self._on_map_mouse_click_event)
        self.mpl_map_figure.canvas.draw()

    def _on_map_mouse_click_event(self, event):
        if None in (event.xdata, event.ydata):
            return
        # Get map coordinates by the inverse transform.
        lng, lat = self.map(event.xdata, event.ydata, inverse=True)
        # Left click: set receiver
        if event.button == 1:
            self.ui.receiver_longitude.setValue(lng)
            self.ui.receiver_latitude.setValue(lat)
        # Right click: set event
        elif (event.button == 3 and self.ui.finsource_tab.currentIndex() == 0):
            self.ui.source_longitude.setValue(lng)
            self.ui.source_latitude.setValue(lat)

    def _plot_event(self):
        if self.ui.finsource_tab.currentIndex() == 0:
            s = self.source
            lng, lat = s.longitude, s.latitude
        elif self.ui.finsource_tab.currentIndex() == 1:
            s = self.finite_source
            s.find_hypocenter()
            lng, lat = s.hypocenter_longitude, s.hypocenter_latitude

        try:
            if self.__event_map_obj.longitude == lng and \
                    self.__event_map_obj.latitude == lat:
                return
        except AttributeError:
            pass

        try:
            self.__event_map_obj.remove()
        except AttributeError:
            pass

        x1, y1 = self.map(lng, lat)
        self.__event_map_obj = self.map.scatter(x1, y1, s=300, zorder=10,
                                                color="yellow", marker="*",
                                                edgecolor="k")
        self.__event_map_obj.longitude = lng
        self.__event_map_obj.latitude = lat
        self.mpl_map_figure.canvas.draw()

    def _plot_receiver(self):
        r = self.receiver
        lng, lat = r.longitude, r.latitude
        try:
            if self.__receiver_map_obj.longitude == lng and \
                    self.__receiver_map_obj.latitude == lat:
                return
        except AttributeError:
            pass

        try:
            self.__receiver_map_obj.remove()
        except AttributeError:
            pass

        x1, y1 = self.map(lng, lat)
        self.__receiver_map_obj = self.map.scatter(x1, y1, s=170, zorder=10,
                                                   color="red", marker="v",
                                                   edgecolor="k")
        self.__receiver_map_obj.longitude = lng
        self.__receiver_map_obj.latitude = lat
        self.mpl_map_figure.canvas.draw()

    @property
    def source(self):
        fm = self.focmec
        fm = [_i * SCALING_FACTOR for _i in fm]
        return Source(
            latitude=float(self.ui.source_latitude.value()),
            longitude=float(self.ui.source_longitude.value()),
            depth_in_m=float(self.source_depth) * 1000.0, m_rr=fm[0],
            m_tt=fm[1], m_pp=fm[2], m_rt=fm[3], m_rp=fm[4],
            m_tp=fm[5])

    @property
    def receiver(self):
        return Receiver(
            latitude=float(self.ui.receiver_latitude.value()),
            longitude=float(self.ui.receiver_longitude.value()))

    def update(self, autorange=False, force=False):

        try:
            self._plot_receiver()
            self._plot_event()
        except AttributeError:
            return

        if (not bool(self.ui.auto_update_check_box.checkState())
                and self.ui.finsource_tab.currentIndex() == 1 and not force):
            return

        components = ["z", "n", "e"]
        components_map = {0: ("Z", "N", "E"),
                          1: ("Z", "R", "T")}

        components_choice = int(self.ui.components_combo.currentIndex())

        label_map = {0: {"z": "vertical", "n": "east", "e": "north"},
                     1: {"z": "vertical", "n": "radial", "e": "transverse"}}

        for component in components:
            p = getattr(self.ui, "%s_graph" % component)
            p.setTitle(label_map[components_choice][component].capitalize()
                       + " component")

        if self.ui.finsource_tab.currentIndex() == 0:
            src_latitude = self.source.latitude
            src_longitude = self.source.longitude
            src_depth_in_m = self.source.depth_in_m
        else:
            src_latitude = self.finite_source.hypocenter_latitude
            src_longitude = self.finite_source.hypocenter_longitude
            src_depth_in_m = self.finite_source.hypocenter_depth_in_m

        rec = self.receiver
        try:
            # Grab resampling settings from the UI.
            if bool(self.ui.resample_check_box.checkState()):
                dt = float(self.ui.resample_factor.value())
                dt = self.instaseis_db.dt / dt
            else:
                dt = None
            if self.ui.finsource_tab.currentIndex() == 0:
                st = self.instaseis_db.get_seismograms(
                    source=self.source, receiver=self.receiver, dt=dt,
                    components=components_map[components_choice])
            elif self.ui.finsource_tab.currentIndex() == 1:
                st = self.instaseis_db.get_seismograms_finite_source(
                    sources=self.finite_source, receiver=self.receiver, dt=dt,
                    components=components_map[components_choice])

            # check filter values from the UI
            if bool(self.ui.lowpass_check_box.checkState()):
                try:
                    freq = 1.0 / float(self.ui.lowpass_period.value())
                    st.filter('lowpass', freq=freq, zerophase=True)
                except ZeroDivisionError:
                    # this happens when typing in the lowpass_period box
                    pass

            if bool(self.ui.highpass_check_box.checkState()):
                try:
                    freq = 1.0 / float(self.ui.highpass_period.value())
                    st.filter('highpass', freq=freq, zerophase=True)
                except ZeroDivisionError:
                    # this happens when typing in the highpass_period box
                    pass

        except AttributeError:
            return

        if bool(self.ui.tt_times.checkState()):
            great_circle_distance = locations2degrees(
                src_latitude, src_longitude,
                rec.latitude, rec.longitude)
            self.tts = getTravelTimes(great_circle_distance,
                                      src_depth_in_m / 1000.0, model="ak135")

        for ic, component in enumerate(components):
            plot_widget = getattr(self.ui, "%s_graph" % component.lower())
            plot_widget.clear()
            tr = st.select(component=components_map[components_choice][ic])[0]
            times = tr.times()
            plot_widget.plot(times, tr.data, pen="k")

            if bool(self.ui.tt_times.checkState()):
                for tt in self.tts:
                    if tt["time"] >= times[-1]:
                        self.tts.remove(tt)
                        continue
                    if tt["phase_name"][0].lower() == "p":
                        pen = "#008c2866"
                    else:
                        pen = "#95000066"
                    plot_widget.addLine(x=tt["time"], pen=pen, z=-10)

            if autorange:
                plot_widget.autoRange()

    def on_select_folder_button_released(self):
        self.folder = str(QtGui.QFileDialog.getExistingDirectory(
            self, "Choose Directory",
            os.path.expanduser("~")))
        if not self.folder:
            return
        self.instaseis_db = InstaSeisDB(self.folder)

        # Adjust depth slider to the DB.
        max_rad = self.instaseis_db.parsed_mesh.kwf_rmax
        min_rad = self.instaseis_db.parsed_mesh.kwf_rmin
        self.ui.depth_slider.setMinimum(min_rad - max_rad)
        self.ui.depth_slider.setMaximum(0)

        if self.finite_source is not None:
            self.finite_source.resample_sliprate(
                dt=self.instaseis_db.dt, nsamp=self.instaseis_db.ndumps)

        self.update(autorange=True)
        self.set_info()

    def on_open_srf_file_button_released(self):
        self.srf_file = str(QtGui.QFileDialog.getOpenFileName(
            self, "Choose *.srf File",
            os.path.expanduser("~")))
        if not self.srf_file:
            return
        self.finite_source = FiniteSource.from_srf_file(self.srf_file)

        if self.instaseis_db is not None:
            self.finite_source.resample_sliprate(
                dt=self.instaseis_db.dt, nsamp=self.instaseis_db.ndumps)

        self.update()
        self.set_info()

    def set_info(self):
        info_str = ''
        if self.instaseis_db is not None:
            info_str += str(self.instaseis_db) + '\n'
        if self.finite_source is not None:
            info_str += str(self.finite_source)
        self.ui.info_text.setText(info_str)

    def on_source_latitude_valueChanged(self, *args):
        self.update()

    def on_source_longitude_valueChanged(self, *args):
        self.update()

    def on_receiver_latitude_valueChanged(self, *args):
        self.update()

    def on_receiver_longitude_valueChanged(self, *args):
        self.update()

    def on_m_rr_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    def on_m_tt_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    def on_m_pp_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    def on_m_rt_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    def on_m_rp_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    def on_m_tp_valueChanged(self, *args):
        self._draw_mt()
        self.update()

    @property
    def source_depth(self):
        value = int(-1.0 * int(self.ui.depth_slider.value()))
        return value

    def on_depth_slider_valueChanged(self, *args):
        self.ui.depth_label.setText("Depth: %i km" % self.source_depth)
        self.update()

    def on_strike_slider_valueChanged(self, *args):
        self.ui.strike_value.setText("%i" % self.ui.strike_slider.value())
        self._draw_mt()
        self.update()

    def on_dip_slider_valueChanged(self, *args):
        self.ui.dip_value.setText("%i" % self.ui.dip_slider.value())
        self._draw_mt()
        self.update()

    def on_rake_slider_valueChanged(self, *args):
        self.ui.rake_value.setText("%i" % self.ui.rake_slider.value())
        self._draw_mt()
        self.update()

    def on_reset_view_button_released(self, *args):
        self.ui.z_graph.autoRange()

    def on_resample_check_box_stateChanged(self, state):
        resample = bool(state)
        self.ui.resample_factor.setEnabled(resample)
        self.ui.sr_ref_label.setEnabled(resample)
        self.update()

    def on_resample_factor_valueChanged(self, *args):
        self.update()

    def on_tt_times_stateChanged(self, state):
        self.update()

    def on_lowpass_check_box_stateChanged(self, state):
        resample = bool(state)
        self.ui.lowpass_period.setEnabled(resample)
        self.ui.lowpass_label.setEnabled(resample)
        self.update()

    def on_lowpass_period_valueChanged(self, *args):
        self.update()

    def on_highpass_check_box_stateChanged(self, state):
        resample = bool(state)
        self.ui.highpass_period.setEnabled(resample)
        self.ui.highpass_label.setEnabled(resample)
        self.update()

    def on_highpass_period_valueChanged(self, *args):
        self.update()

    def on_components_combo_currentIndexChanged(self):
        self.update()

    def on_finsource_tab_currentChanged(self):
        self.update()

    def on_update_button_released(self):
        self.update(force=True)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if source.parent() in [self.ui.z_graph, self.ui.n_graph,
                                   self.ui.e_graph] \
                    and event.buttons() == QtCore.Qt.NoButton:
                try:
                    tt = float(self.ui.z_graph.mapToView(
                        pg.Point(event.pos().x(), event.pos().y())).x())
                    closest_phase = \
                        min(self.tts, key=lambda x: abs(x["time"] - tt))
                    tooltipstr = 'Mouse at %6.2f s, closest phase = %s, ' \
                        'arriving at %6.2f s' % \
                        (tt, closest_phase["phase_name"],
                         closest_phase["time"])
                except:
                    tooltipstr = ''

                self.ui.z_graph.setToolTip(tooltipstr)
                self.ui.n_graph.setToolTip(tooltipstr)
                self.ui.e_graph.setToolTip(tooltipstr)

        return QtGui.QMainWindow.eventFilter(self, source, event)


def launch():
    # Automatically compile all ui files if they have been changed.
    compile_and_import_ui_files()

    # Launch and open the window.
    app = QtGui.QApplication(sys.argv, QtGui.QApplication.GuiClient)
    window = Window()

    # Show and bring window to foreground.
    window.show()
    app.installEventFilter(window)
    window.raise_()
    os._exit(app.exec_())
