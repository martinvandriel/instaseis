# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ex/local/src/instaseis/instaseis/gui/qt_window.ui'
#
# Created: Mon Oct 27 17:57:29 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1350, 755)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 700))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.select_folder_button = QtGui.QPushButton(self.centralwidget)
        self.select_folder_button.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.select_folder_button.setFont(font)
        self.select_folder_button.setObjectName(_fromUtf8("select_folder_button"))
        self.horizontalLayout_6.addWidget(self.select_folder_button)
        self.reset_view_button = QtGui.QPushButton(self.centralwidget)
        self.reset_view_button.setObjectName(_fromUtf8("reset_view_button"))
        self.horizontalLayout_6.addWidget(self.reset_view_button)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_6.addWidget(self.line_3)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.tt_times = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tt_times.setFont(font)
        self.tt_times.setObjectName(_fromUtf8("tt_times"))
        self.horizontalLayout_6.addWidget(self.tt_times)
        spacerItem2 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_6.addWidget(self.line_6)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.lowpass_check_box = QtGui.QCheckBox(self.centralwidget)
        self.lowpass_check_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lowpass_check_box.setFont(font)
        self.lowpass_check_box.setChecked(False)
        self.lowpass_check_box.setTristate(False)
        self.lowpass_check_box.setObjectName(_fromUtf8("lowpass_check_box"))
        self.horizontalLayout_6.addWidget(self.lowpass_check_box)
        self.lowpass_period = QtGui.QDoubleSpinBox(self.centralwidget)
        self.lowpass_period.setEnabled(False)
        self.lowpass_period.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lowpass_period.setDecimals(1)
        self.lowpass_period.setMinimum(0.0)
        self.lowpass_period.setMaximum(1000.0)
        self.lowpass_period.setProperty("value", 5.0)
        self.lowpass_period.setObjectName(_fromUtf8("lowpass_period"))
        self.horizontalLayout_6.addWidget(self.lowpass_period)
        self.lowpass_label = QtGui.QLabel(self.centralwidget)
        self.lowpass_label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lowpass_label.setFont(font)
        self.lowpass_label.setObjectName(_fromUtf8("lowpass_label"))
        self.horizontalLayout_6.addWidget(self.lowpass_label)
        self.highpass_check_box = QtGui.QCheckBox(self.centralwidget)
        self.highpass_check_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.highpass_check_box.setFont(font)
        self.highpass_check_box.setChecked(False)
        self.highpass_check_box.setTristate(False)
        self.highpass_check_box.setObjectName(_fromUtf8("highpass_check_box"))
        self.horizontalLayout_6.addWidget(self.highpass_check_box)
        self.highpass_period = QtGui.QDoubleSpinBox(self.centralwidget)
        self.highpass_period.setEnabled(False)
        self.highpass_period.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.highpass_period.setDecimals(1)
        self.highpass_period.setMinimum(0.0)
        self.highpass_period.setMaximum(1000.0)
        self.highpass_period.setProperty("value", 50.0)
        self.highpass_period.setObjectName(_fromUtf8("highpass_period"))
        self.horizontalLayout_6.addWidget(self.highpass_period)
        self.highpass_label = QtGui.QLabel(self.centralwidget)
        self.highpass_label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.highpass_label.setFont(font)
        self.highpass_label.setObjectName(_fromUtf8("highpass_label"))
        self.horizontalLayout_6.addWidget(self.highpass_label)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.components_combo = QtGui.QComboBox(self.centralwidget)
        self.components_combo.setEditable(False)
        self.components_combo.setObjectName(_fromUtf8("components_combo"))
        self.components_combo.addItem(_fromUtf8(""))
        self.components_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.components_combo)
        spacerItem5 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.resample_check_box = QtGui.QCheckBox(self.centralwidget)
        self.resample_check_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.resample_check_box.setFont(font)
        self.resample_check_box.setChecked(False)
        self.resample_check_box.setTristate(False)
        self.resample_check_box.setObjectName(_fromUtf8("resample_check_box"))
        self.horizontalLayout_6.addWidget(self.resample_check_box)
        self.resample_factor = QtGui.QDoubleSpinBox(self.centralwidget)
        self.resample_factor.setEnabled(False)
        self.resample_factor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resample_factor.setMinimum(1.0)
        self.resample_factor.setProperty("value", 10.0)
        self.resample_factor.setObjectName(_fromUtf8("resample_factor"))
        self.horizontalLayout_6.addWidget(self.resample_factor)
        self.sr_ref_label = QtGui.QLabel(self.centralwidget)
        self.sr_ref_label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sr_ref_label.setFont(font)
        self.sr_ref_label.setObjectName(_fromUtf8("sr_ref_label"))
        self.horizontalLayout_6.addWidget(self.sr_ref_label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.z_graph = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_graph.sizePolicy().hasHeightForWidth())
        self.z_graph.setSizePolicy(sizePolicy)
        self.z_graph.setMouseTracking(False)
        self.z_graph.setToolTip(_fromUtf8(""))
        self.z_graph.setObjectName(_fromUtf8("z_graph"))
        self.verticalLayout_2.addWidget(self.z_graph)
        self.n_graph = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_graph.sizePolicy().hasHeightForWidth())
        self.n_graph.setSizePolicy(sizePolicy)
        self.n_graph.setToolTip(_fromUtf8(""))
        self.n_graph.setObjectName(_fromUtf8("n_graph"))
        self.verticalLayout_2.addWidget(self.n_graph)
        self.e_graph = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_graph.sizePolicy().hasHeightForWidth())
        self.e_graph.setSizePolicy(sizePolicy)
        self.e_graph.setObjectName(_fromUtf8("e_graph"))
        self.verticalLayout_2.addWidget(self.e_graph)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_8.addWidget(self.line_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.info_text = QtGui.QTextBrowser(self.centralwidget)
        self.info_text.setMinimumSize(QtCore.QSize(470, 100))
        self.info_text.setMaximumSize(QtCore.QSize(470, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(8)
        self.info_text.setFont(font)
        self.info_text.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.info_text.setTabStopWidth(20)
        self.info_text.setObjectName(_fromUtf8("info_text"))
        self.verticalLayout_3.addWidget(self.info_text)
        self.finsource_tab = QtGui.QTabWidget(self.centralwidget)
        self.finsource_tab.setMinimumSize(QtCore.QSize(470, 0))
        self.finsource_tab.setMaximumSize(QtCore.QSize(470, 16777215))
        self.finsource_tab.setObjectName(_fromUtf8("finsource_tab"))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_9)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab_9)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.source_latitude = QtGui.QDoubleSpinBox(self.tab_9)
        self.source_latitude.setMinimum(-90.0)
        self.source_latitude.setMaximum(90.0)
        self.source_latitude.setObjectName(_fromUtf8("source_latitude"))
        self.gridLayout_2.addWidget(self.source_latitude, 1, 1, 1, 1)
        self.source_longitude = QtGui.QDoubleSpinBox(self.tab_9)
        self.source_longitude.setMinimum(-180.0)
        self.source_longitude.setMaximum(180.0)
        self.source_longitude.setObjectName(_fromUtf8("source_longitude"))
        self.gridLayout_2.addWidget(self.source_longitude, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_9)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.depth_label = QtGui.QLabel(self.tab_9)
        self.depth_label.setMinimumSize(QtCore.QSize(120, 0))
        self.depth_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.depth_label.setObjectName(_fromUtf8("depth_label"))
        self.horizontalLayout_3.addWidget(self.depth_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mt_fig = Qt4MplCanvas(self.tab_9)
        self.mt_fig.setMinimumSize(QtCore.QSize(60, 60))
        self.mt_fig.setMaximumSize(QtCore.QSize(60, 60))
        self.mt_fig.setObjectName(_fromUtf8("mt_fig"))
        self.horizontalLayout.addWidget(self.mt_fig)
        self.source_tab = QtGui.QTabWidget(self.tab_9)
        self.source_tab.setObjectName(_fromUtf8("source_tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.m_rr = QtGui.QDoubleSpinBox(self.tab)
        self.m_rr.setPrefix(_fromUtf8(""))
        self.m_rr.setMinimum(-99.0)
        self.m_rr.setMaximum(99.0)
        self.m_rr.setObjectName(_fromUtf8("m_rr"))
        self.gridLayout.addWidget(self.m_rr, 1, 1, 1, 1)
        self.m_rt = QtGui.QDoubleSpinBox(self.tab)
        self.m_rt.setPrefix(_fromUtf8(""))
        self.m_rt.setMinimum(-99.0)
        self.m_rt.setMaximum(99.0)
        self.m_rt.setObjectName(_fromUtf8("m_rt"))
        self.gridLayout.addWidget(self.m_rt, 1, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.m_rp = QtGui.QDoubleSpinBox(self.tab)
        self.m_rp.setPrefix(_fromUtf8(""))
        self.m_rp.setMinimum(-99.0)
        self.m_rp.setMaximum(99.0)
        self.m_rp.setObjectName(_fromUtf8("m_rp"))
        self.gridLayout.addWidget(self.m_rp, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.m_tt = QtGui.QDoubleSpinBox(self.tab)
        self.m_tt.setPrefix(_fromUtf8(""))
        self.m_tt.setMinimum(-99.0)
        self.m_tt.setMaximum(99.0)
        self.m_tt.setObjectName(_fromUtf8("m_tt"))
        self.gridLayout.addWidget(self.m_tt, 3, 2, 1, 1)
        self.m_tp = QtGui.QDoubleSpinBox(self.tab)
        self.m_tp.setPrefix(_fromUtf8(""))
        self.m_tp.setMinimum(-99.0)
        self.m_tp.setMaximum(99.0)
        self.m_tp.setObjectName(_fromUtf8("m_tp"))
        self.gridLayout.addWidget(self.m_tp, 3, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.m_pp = QtGui.QDoubleSpinBox(self.tab)
        self.m_pp.setPrefix(_fromUtf8(""))
        self.m_pp.setMinimum(-99.0)
        self.m_pp.setMaximum(99.0)
        self.m_pp.setObjectName(_fromUtf8("m_pp"))
        self.gridLayout.addWidget(self.m_pp, 4, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setEnabled(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setColumnStretch(3, 10)
        self.source_tab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setMargin(9)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.strike_value = QtGui.QLabel(self.tab_2)
        self.strike_value.setMinimumSize(QtCore.QSize(30, 0))
        self.strike_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.strike_value.setObjectName(_fromUtf8("strike_value"))
        self.gridLayout_4.addWidget(self.strike_value, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.dip_slider = QtGui.QSlider(self.tab_2)
        self.dip_slider.setMaximum(90)
        self.dip_slider.setProperty("value", 90)
        self.dip_slider.setOrientation(QtCore.Qt.Horizontal)
        self.dip_slider.setObjectName(_fromUtf8("dip_slider"))
        self.gridLayout_4.addWidget(self.dip_slider, 1, 1, 1, 1)
        self.dip_value = QtGui.QLabel(self.tab_2)
        self.dip_value.setMinimumSize(QtCore.QSize(30, 0))
        self.dip_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dip_value.setObjectName(_fromUtf8("dip_value"))
        self.gridLayout_4.addWidget(self.dip_value, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)
        self.rake_slider = QtGui.QSlider(self.tab_2)
        self.rake_slider.setMinimum(-180)
        self.rake_slider.setMaximum(180)
        self.rake_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rake_slider.setObjectName(_fromUtf8("rake_slider"))
        self.gridLayout_4.addWidget(self.rake_slider, 2, 1, 1, 1)
        self.rake_value = QtGui.QLabel(self.tab_2)
        self.rake_value.setMinimumSize(QtCore.QSize(30, 0))
        self.rake_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rake_value.setObjectName(_fromUtf8("rake_value"))
        self.gridLayout_4.addWidget(self.rake_value, 2, 2, 1, 1)
        self.strike_slider = QtGui.QSlider(self.tab_2)
        self.strike_slider.setMaximum(360)
        self.strike_slider.setOrientation(QtCore.Qt.Horizontal)
        self.strike_slider.setObjectName(_fromUtf8("strike_slider"))
        self.gridLayout_4.addWidget(self.strike_slider, 0, 1, 1, 1)
        self.source_tab.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.source_tab)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.depth_slider = QtGui.QSlider(self.tab_9)
        self.depth_slider.setMinimum(-300)
        self.depth_slider.setMaximum(0)
        self.depth_slider.setProperty("value", -10)
        self.depth_slider.setSliderPosition(-10)
        self.depth_slider.setOrientation(QtCore.Qt.Vertical)
        self.depth_slider.setTickPosition(QtGui.QSlider.NoTicks)
        self.depth_slider.setObjectName(_fromUtf8("depth_slider"))
        self.horizontalLayout_5.addWidget(self.depth_slider)
        self.finsource_tab.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.open_srf_file_button = QtGui.QPushButton(self.tab_10)
        self.open_srf_file_button.setObjectName(_fromUtf8("open_srf_file_button"))
        self.horizontalLayout_2.addWidget(self.open_srf_file_button)
        self.update_button = QtGui.QPushButton(self.tab_10)
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.horizontalLayout_2.addWidget(self.update_button)
        self.auto_update_check_box = QtGui.QCheckBox(self.tab_10)
        self.auto_update_check_box.setEnabled(True)
        self.auto_update_check_box.setObjectName(_fromUtf8("auto_update_check_box"))
        self.horizontalLayout_2.addWidget(self.auto_update_check_box)
        self.finsource_tab.addTab(self.tab_10, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.finsource_tab)
        self.map_fig = Qt4MplCanvas(self.centralwidget)
        self.map_fig.setMinimumSize(QtCore.QSize(470, 280))
        self.map_fig.setMaximumSize(QtCore.QSize(470, 280))
        self.map_fig.setObjectName(_fromUtf8("map_fig"))
        self.verticalLayout_3.addWidget(self.map_fig)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.receiver_latitude = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.receiver_latitude.setMinimum(-90.0)
        self.receiver_latitude.setMaximum(90.0)
        self.receiver_latitude.setProperty("value", 45.0)
        self.receiver_latitude.setObjectName(_fromUtf8("receiver_latitude"))
        self.horizontalLayout_7.addWidget(self.receiver_latitude)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_7.addWidget(self.label_12)
        self.receiver_longitude = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.receiver_longitude.setMinimum(-180.0)
        self.receiver_longitude.setMaximum(180.0)
        self.receiver_longitude.setProperty("value", 45.0)
        self.receiver_longitude.setObjectName(_fromUtf8("receiver_longitude"))
        self.horizontalLayout_7.addWidget(self.receiver_longitude)
        spacerItem6 = QtGui.QSpacerItem(163, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.setStretch(0, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.components_combo.setCurrentIndex(1)
        self.finsource_tab.setCurrentIndex(0)
        self.source_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Instaseis GUI", None))
        self.select_folder_button.setText(_translate("MainWindow", "Open DB", None))
        self.reset_view_button.setText(_translate("MainWindow", "Reset View (R)", None))
        self.reset_view_button.setShortcut(_translate("MainWindow", "R", None))
        self.tt_times.setText(_translate("MainWindow", "Plot TauP Times (AK135)", None))
        self.lowpass_check_box.setText(_translate("MainWindow", "Lowpass", None))
        self.lowpass_label.setText(_translate("MainWindow", "s", None))
        self.highpass_check_box.setText(_translate("MainWindow", "Highpass", None))
        self.highpass_label.setText(_translate("MainWindow", "s", None))
        self.components_combo.setItemText(0, _translate("MainWindow", "ZNE", None))
        self.components_combo.setItemText(1, _translate("MainWindow", "ZRT", None))
        self.resample_check_box.setText(_translate("MainWindow", "Resample", None))
        self.sr_ref_label.setText(_translate("MainWindow", "x sampling rate", None))
        self.label.setText(_translate("MainWindow", "Latitude", None))
        self.label_2.setText(_translate("MainWindow", "Longitude", None))
        self.depth_label.setText(_translate("MainWindow", "Depth: 10 km", None))
        self.m_rr.setSuffix(_translate("MainWindow", "e16", None))
        self.m_rt.setSuffix(_translate("MainWindow", "e16", None))
        self.label_9.setText(_translate("MainWindow", "p", None))
        self.label_6.setText(_translate("MainWindow", "t", None))
        self.label_5.setText(_translate("MainWindow", "r", None))
        self.m_rp.setSuffix(_translate("MainWindow", "e16", None))
        self.label_7.setText(_translate("MainWindow", "t", None))
        self.m_tt.setSuffix(_translate("MainWindow", "e16", None))
        self.m_tp.setSuffix(_translate("MainWindow", "e16", None))
        self.label_8.setText(_translate("MainWindow", "p", None))
        self.m_pp.setSuffix(_translate("MainWindow", "e16", None))
        self.label_4.setText(_translate("MainWindow", "r", None))
        self.source_tab.setTabText(self.source_tab.indexOf(self.tab), _translate("MainWindow", "Moment Tensor", None))
        self.strike_value.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Dip", None))
        self.label_3.setText(_translate("MainWindow", "Strike", None))
        self.dip_value.setText(_translate("MainWindow", "0", None))
        self.label_13.setText(_translate("MainWindow", "Rake", None))
        self.rake_value.setText(_translate("MainWindow", "0", None))
        self.source_tab.setTabText(self.source_tab.indexOf(self.tab_2), _translate("MainWindow", "Strike Dip Rake", None))
        self.finsource_tab.setTabText(self.finsource_tab.indexOf(self.tab_9), _translate("MainWindow", "Point Source", None))
        self.open_srf_file_button.setText(_translate("MainWindow", "Open *.srf", None))
        self.update_button.setText(_translate("MainWindow", "update seismograms (U)", None))
        self.update_button.setShortcut(_translate("MainWindow", "U", None))
        self.auto_update_check_box.setText(_translate("MainWindow", "auto update", None))
        self.finsource_tab.setTabText(self.finsource_tab.indexOf(self.tab_10), _translate("MainWindow", "Finite Source", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Receiver", None))
        self.label_11.setText(_translate("MainWindow", "Latitude", None))
        self.label_12.setText(_translate("MainWindow", "Longitude", None))

from instaseis.gui.qt4mplcanvas import Qt4MplCanvas
from pyqtgraph import PlotWidget
