# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lion/workspace/code/instaseis/instaseis/gui/qt_window.ui'
#
# Created: Fri Oct 24 11:18:48 2014
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
        MainWindow.resize(1350, 900)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.reset_view_button = QtGui.QPushButton(self.centralwidget)
        self.reset_view_button.setObjectName(_fromUtf8("reset_view_button"))
        self.horizontalLayout_6.addWidget(self.reset_view_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.tt_times = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tt_times.setFont(font)
        self.tt_times.setObjectName(_fromUtf8("tt_times"))
        self.horizontalLayout_6.addWidget(self.tt_times)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.resample_check_box = QtGui.QCheckBox(self.centralwidget)
        self.resample_check_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.resample_check_box.setFont(font)
        self.resample_check_box.setChecked(False)
        self.resample_check_box.setTristate(False)
        self.resample_check_box.setObjectName(_fromUtf8("resample_check_box"))
        self.horizontalLayout_6.addWidget(self.resample_check_box)
        self.resample_factor = QtGui.QDoubleSpinBox(self.centralwidget)
        self.resample_factor.setMinimum(1.0)
        self.resample_factor.setProperty("value", 10.0)
        self.resample_factor.setObjectName(_fromUtf8("resample_factor"))
        self.horizontalLayout_6.addWidget(self.resample_factor)
        self.sr_ref_label = QtGui.QLabel(self.centralwidget)
        self.sr_ref_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sr_ref_label.setFont(font)
        self.sr_ref_label.setObjectName(_fromUtf8("sr_ref_label"))
        self.horizontalLayout_6.addWidget(self.sr_ref_label)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_6.addWidget(self.line_2)
        self.lanczos_a_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lanczos_a_label.setFont(font)
        self.lanczos_a_label.setObjectName(_fromUtf8("lanczos_a_label"))
        self.horizontalLayout_6.addWidget(self.lanczos_a_label)
        self.lanczos_a = QtGui.QSpinBox(self.centralwidget)
        self.lanczos_a.setMinimum(1)
        self.lanczos_a.setMaximum(20)
        self.lanczos_a.setProperty("value", 5)
        self.lanczos_a.setObjectName(_fromUtf8("lanczos_a"))
        self.horizontalLayout_6.addWidget(self.lanczos_a)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.z_graph = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_graph.sizePolicy().hasHeightForWidth())
        self.z_graph.setSizePolicy(sizePolicy)
        self.z_graph.setObjectName(_fromUtf8("z_graph"))
        self.verticalLayout_2.addWidget(self.z_graph)
        self.n_graph = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_graph.sizePolicy().hasHeightForWidth())
        self.n_graph.setSizePolicy(sizePolicy)
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
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_8.addWidget(self.line)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.select_folder_button = QtGui.QPushButton(self.centralwidget)
        self.select_folder_button.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_folder_button.setFont(font)
        self.select_folder_button.setObjectName(_fromUtf8("select_folder_button"))
        self.horizontalLayout_2.addWidget(self.select_folder_button)
        self.db_path_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_path_label.setFont(font)
        self.db_path_label.setText(_fromUtf8(""))
        self.db_path_label.setObjectName(_fromUtf8("db_path_label"))
        self.horizontalLayout_2.addWidget(self.db_path_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.info_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(10)
        self.info_label.setFont(font)
        self.info_label.setText(_fromUtf8(""))
        self.info_label.setObjectName(_fromUtf8("info_label"))
        self.verticalLayout_3.addWidget(self.info_label)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setMargin(2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.source_latitude = QtGui.QDoubleSpinBox(self.groupBox)
        self.source_latitude.setMinimum(-90.0)
        self.source_latitude.setMaximum(90.0)
        self.source_latitude.setObjectName(_fromUtf8("source_latitude"))
        self.gridLayout_2.addWidget(self.source_latitude, 1, 1, 1, 1)
        self.source_longitude = QtGui.QDoubleSpinBox(self.groupBox)
        self.source_longitude.setMinimum(-180.0)
        self.source_longitude.setMaximum(180.0)
        self.source_longitude.setObjectName(_fromUtf8("source_longitude"))
        self.gridLayout_2.addWidget(self.source_longitude, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.depth_label = QtGui.QLabel(self.groupBox)
        self.depth_label.setMinimumSize(QtCore.QSize(120, 0))
        self.depth_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.depth_label.setObjectName(_fromUtf8("depth_label"))
        self.horizontalLayout_3.addWidget(self.depth_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mt_fig = Qt4MplCanvas(self.groupBox)
        self.mt_fig.setMinimumSize(QtCore.QSize(60, 60))
        self.mt_fig.setMaximumSize(QtCore.QSize(60, 60))
        self.mt_fig.setObjectName(_fromUtf8("mt_fig"))
        self.horizontalLayout.addWidget(self.mt_fig)
        self.source_tab = QtGui.QTabWidget(self.groupBox)
        self.source_tab.setObjectName(_fromUtf8("source_tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setMargin(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
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
        self.m_rp = QtGui.QDoubleSpinBox(self.tab)
        self.m_rp.setPrefix(_fromUtf8(""))
        self.m_rp.setMinimum(-99.0)
        self.m_rp.setMaximum(99.0)
        self.m_rp.setObjectName(_fromUtf8("m_rp"))
        self.gridLayout.addWidget(self.m_rp, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.m_tt = QtGui.QDoubleSpinBox(self.tab)
        self.m_tt.setPrefix(_fromUtf8(""))
        self.m_tt.setMinimum(-99.0)
        self.m_tt.setMaximum(99.0)
        self.m_tt.setObjectName(_fromUtf8("m_tt"))
        self.gridLayout.addWidget(self.m_tt, 2, 2, 1, 1)
        self.m_tp = QtGui.QDoubleSpinBox(self.tab)
        self.m_tp.setPrefix(_fromUtf8(""))
        self.m_tp.setMinimum(-99.0)
        self.m_tp.setMaximum(99.0)
        self.m_tp.setObjectName(_fromUtf8("m_tp"))
        self.gridLayout.addWidget(self.m_tp, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 1)
        self.m_pp = QtGui.QDoubleSpinBox(self.tab)
        self.m_pp.setPrefix(_fromUtf8(""))
        self.m_pp.setMinimum(-99.0)
        self.m_pp.setMaximum(99.0)
        self.m_pp.setObjectName(_fromUtf8("m_pp"))
        self.gridLayout.addWidget(self.m_pp, 3, 3, 1, 1)
        self.source_tab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setMargin(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.strike_value = QtGui.QLabel(self.tab_2)
        self.strike_value.setMinimumSize(QtCore.QSize(50, 0))
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
        self.dip_value.setMinimumSize(QtCore.QSize(50, 0))
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
        self.rake_value.setMinimumSize(QtCore.QSize(50, 0))
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
        self.depth_slider = QtGui.QSlider(self.groupBox)
        self.depth_slider.setMinimum(-300)
        self.depth_slider.setMaximum(0)
        self.depth_slider.setProperty("value", -10)
        self.depth_slider.setSliderPosition(-10)
        self.depth_slider.setOrientation(QtCore.Qt.Vertical)
        self.depth_slider.setTickPosition(QtGui.QSlider.NoTicks)
        self.depth_slider.setObjectName(_fromUtf8("depth_slider"))
        self.horizontalLayout_5.addWidget(self.depth_slider)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.map_fig = Qt4MplCanvas(self.centralwidget)
        self.map_fig.setMinimumSize(QtCore.QSize(470, 280))
        self.map_fig.setMaximumSize(QtCore.QSize(470, 280))
        self.map_fig.setObjectName(_fromUtf8("map_fig"))
        self.verticalLayout_3.addWidget(self.map_fig)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setMargin(2)
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
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.setStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.source_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Instaseis GUI", None))
        self.reset_view_button.setText(_translate("MainWindow", "Reset View (R)", None))
        self.reset_view_button.setShortcut(_translate("MainWindow", "R", None))
        self.tt_times.setText(_translate("MainWindow", "Plot Taup Times (AK135)", None))
        self.resample_check_box.setText(_translate("MainWindow", "Resample", None))
        self.sr_ref_label.setText(_translate("MainWindow", "x sampling rate", None))
        self.lanczos_a_label.setText(_translate("MainWindow", "Lanczos a", None))
        self.select_folder_button.setText(_translate("MainWindow", "Select Folder", None))
        self.groupBox.setTitle(_translate("MainWindow", "Source", None))
        self.label.setText(_translate("MainWindow", "Latitude", None))
        self.label_2.setText(_translate("MainWindow", "Longitude", None))
        self.depth_label.setText(_translate("MainWindow", "Depth: 10 km", None))
        self.label_5.setText(_translate("MainWindow", "r", None))
        self.label_6.setText(_translate("MainWindow", "t", None))
        self.label_9.setText(_translate("MainWindow", "p", None))
        self.label_4.setText(_translate("MainWindow", "r", None))
        self.m_rr.setSuffix(_translate("MainWindow", "e16", None))
        self.m_rt.setSuffix(_translate("MainWindow", "e16", None))
        self.m_rp.setSuffix(_translate("MainWindow", "e16", None))
        self.label_7.setText(_translate("MainWindow", "t", None))
        self.m_tt.setSuffix(_translate("MainWindow", "e16", None))
        self.m_tp.setSuffix(_translate("MainWindow", "e16", None))
        self.label_8.setText(_translate("MainWindow", "p", None))
        self.m_pp.setSuffix(_translate("MainWindow", "e16", None))
        self.source_tab.setTabText(self.source_tab.indexOf(self.tab), _translate("MainWindow", "Moment Tensor", None))
        self.strike_value.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Dip", None))
        self.label_3.setText(_translate("MainWindow", "Strike", None))
        self.dip_value.setText(_translate("MainWindow", "0", None))
        self.label_13.setText(_translate("MainWindow", "Rake", None))
        self.rake_value.setText(_translate("MainWindow", "0", None))
        self.source_tab.setTabText(self.source_tab.indexOf(self.tab_2), _translate("MainWindow", "Strike Dip Rake", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Receiver", None))
        self.label_11.setText(_translate("MainWindow", "Latitude", None))
        self.label_12.setText(_translate("MainWindow", "Longitude", None))

from instaseis.gui.qt4mplcanvas import Qt4MplCanvas
from pyqtgraph import PlotWidget
