# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/redShiftTools_objSet_mesh.ui'
#
# Created: Tue Jan 23 17:42:31 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(500, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tessllation_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tessllation_label.setFont(font)
        self.tessllation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tessllation_label.setObjectName("tessllation_label")
        self.verticalLayout.addWidget(self.tessllation_label)
        self.tessellation_layout = QtWidgets.QFormLayout()
        self.tessellation_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.tessellation_layout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tessellation_layout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.tessellation_layout.setSpacing(4)
        self.tessellation_layout.setObjectName("tessellation_layout")
        self.sdRule_label = QtWidgets.QLabel(main_widget)
        self.sdRule_label.setMinimumSize(QtCore.QSize(150, 0))
        self.sdRule_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sdRule_label.setObjectName("sdRule_label")
        self.tessellation_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sdRule_label)
        self.tessellation_enable_CB = QtWidgets.QCheckBox(main_widget)
        self.tessellation_enable_CB.setObjectName("tessellation_enable_CB")
        self.tessellation_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tessellation_enable_CB)
        self.sdRule_comboBox = QtWidgets.QComboBox(main_widget)
        self.sdRule_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sdRule_comboBox.setObjectName("sdRule_comboBox")
        self.sdRule_comboBox.addItem("")
        self.sdRule_comboBox.addItem("")
        self.tessellation_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sdRule_comboBox)
        self.screeSpaceAdaptiveCB = QtWidgets.QCheckBox(main_widget)
        self.screeSpaceAdaptiveCB.setObjectName("screeSpaceAdaptiveCB")
        self.tessellation_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.screeSpaceAdaptiveCB)
        self.smoothSd_CB = QtWidgets.QCheckBox(main_widget)
        self.smoothSd_CB.setObjectName("smoothSd_CB")
        self.tessellation_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.smoothSd_CB)
        self.miniEdgeLength_label = QtWidgets.QLabel(main_widget)
        self.miniEdgeLength_label.setMinimumSize(QtCore.QSize(150, 0))
        self.miniEdgeLength_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.miniEdgeLength_label.setObjectName("miniEdgeLength_label")
        self.tessellation_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.miniEdgeLength_label)
        self.miniEdge_layout = QtWidgets.QHBoxLayout()
        self.miniEdge_layout.setObjectName("miniEdge_layout")
        self.miniEdge_LE = QtWidgets.QLineEdit(main_widget)
        self.miniEdge_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.miniEdge_LE.setInputMask("")
        self.miniEdge_LE.setFrame(True)
        self.miniEdge_LE.setObjectName("miniEdge_LE")
        self.miniEdge_layout.addWidget(self.miniEdge_LE)
        self.miniEdge_slider = QtWidgets.QSlider(main_widget)
        self.miniEdge_slider.setMaximum(32)
        self.miniEdge_slider.setOrientation(QtCore.Qt.Horizontal)
        self.miniEdge_slider.setObjectName("miniEdge_slider")
        self.miniEdge_layout.addWidget(self.miniEdge_slider)
        self.tessellation_layout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.miniEdge_layout)
        self.maxSd_label = QtWidgets.QLabel(main_widget)
        self.maxSd_label.setMinimumSize(QtCore.QSize(150, 0))
        self.maxSd_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxSd_label.setObjectName("maxSd_label")
        self.tessellation_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.maxSd_label)
        self.maxSd_layout = QtWidgets.QHBoxLayout()
        self.maxSd_layout.setObjectName("maxSd_layout")
        self.maxSd_LE = QtWidgets.QLineEdit(main_widget)
        self.maxSd_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.maxSd_LE.setObjectName("maxSd_LE")
        self.maxSd_layout.addWidget(self.maxSd_LE)
        self.maxSd_slider = QtWidgets.QSlider(main_widget)
        self.maxSd_slider.setMaximum(16)
        self.maxSd_slider.setOrientation(QtCore.Qt.Horizontal)
        self.maxSd_slider.setObjectName("maxSd_slider")
        self.maxSd_layout.addWidget(self.maxSd_slider)
        self.tessellation_layout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.maxSd_layout)
        self.outOfFrustumTessFactor_label = QtWidgets.QLabel(main_widget)
        self.outOfFrustumTessFactor_label.setMinimumSize(QtCore.QSize(150, 0))
        self.outOfFrustumTessFactor_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outOfFrustumTessFactor_label.setObjectName("outOfFrustumTessFactor_label")
        self.tessellation_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.outOfFrustumTessFactor_label)
        self.factor_layout = QtWidgets.QHBoxLayout()
        self.factor_layout.setObjectName("factor_layout")
        self.factor_LE = QtWidgets.QLineEdit(main_widget)
        self.factor_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.factor_LE.setObjectName("factor_LE")
        self.factor_layout.addWidget(self.factor_LE)
        self.factor_slider = QtWidgets.QSlider(main_widget)
        self.factor_slider.setMaximum(32)
        self.factor_slider.setOrientation(QtCore.Qt.Horizontal)
        self.factor_slider.setObjectName("factor_slider")
        self.factor_layout.addWidget(self.factor_slider)
        self.tessellation_layout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.factor_layout)
        self.verticalLayout.addLayout(self.tessellation_layout)
        self.frame = QtWidgets.QFrame(main_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.displacement_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.displacement_label.setFont(font)
        self.displacement_label.setAlignment(QtCore.Qt.AlignCenter)
        self.displacement_label.setObjectName("displacement_label")
        self.verticalLayout.addWidget(self.displacement_label)
        self.dm_big_layout = QtWidgets.QFormLayout()
        self.dm_big_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.dm_big_layout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.dm_big_layout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.dm_big_layout.setSpacing(4)
        self.dm_big_layout.setObjectName("dm_big_layout")
        self.dm_enable_CB = QtWidgets.QCheckBox(main_widget)
        self.dm_enable_CB.setObjectName("dm_enable_CB")
        self.dm_big_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dm_enable_CB)
        self.maximum_dm_label = QtWidgets.QLabel(main_widget)
        self.maximum_dm_label.setMinimumSize(QtCore.QSize(150, 0))
        self.maximum_dm_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maximum_dm_label.setObjectName("maximum_dm_label")
        self.dm_big_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maximum_dm_label)
        self.max_dm_layout = QtWidgets.QHBoxLayout()
        self.max_dm_layout.setObjectName("max_dm_layout")
        self.max_dm_LE = QtWidgets.QLineEdit(main_widget)
        self.max_dm_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.max_dm_LE.setObjectName("max_dm_LE")
        self.max_dm_layout.addWidget(self.max_dm_LE)
        self.max_dm_slider = QtWidgets.QSlider(main_widget)
        self.max_dm_slider.setMaximum(1000)
        self.max_dm_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_dm_slider.setObjectName("max_dm_slider")
        self.max_dm_layout.addWidget(self.max_dm_slider)
        self.dm_big_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.max_dm_layout)
        self.dm_scale_label = QtWidgets.QLabel(main_widget)
        self.dm_scale_label.setMinimumSize(QtCore.QSize(150, 0))
        self.dm_scale_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dm_scale_label.setObjectName("dm_scale_label")
        self.dm_big_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dm_scale_label)
        self.dm_scale_layout = QtWidgets.QHBoxLayout()
        self.dm_scale_layout.setObjectName("dm_scale_layout")
        self.dm_scale_LE = QtWidgets.QLineEdit(main_widget)
        self.dm_scale_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dm_scale_LE.setObjectName("dm_scale_LE")
        self.dm_scale_layout.addWidget(self.dm_scale_LE)
        self.dm_scale_slider = QtWidgets.QSlider(main_widget)
        self.dm_scale_slider.setMaximum(1000)
        self.dm_scale_slider.setOrientation(QtCore.Qt.Horizontal)
        self.dm_scale_slider.setObjectName("dm_scale_slider")
        self.dm_scale_layout.addWidget(self.dm_scale_slider)
        self.dm_big_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.dm_scale_layout)
        self.enable_auto_bump_mapping_CB = QtWidgets.QCheckBox(main_widget)
        self.enable_auto_bump_mapping_CB.setObjectName("enable_auto_bump_mapping_CB")
        self.dm_big_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enable_auto_bump_mapping_CB)
        self.verticalLayout.addLayout(self.dm_big_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.tessllation_label.setText(QtWidgets.QApplication.translate("main_widget", "Tessellation", None, -1))
        self.sdRule_label.setText(QtWidgets.QApplication.translate("main_widget", "Subdivision Rule", None, -1))
        self.tessellation_enable_CB.setText(QtWidgets.QApplication.translate("main_widget", "Enable", None, -1))
        self.sdRule_comboBox.setItemText(0, QtWidgets.QApplication.translate("main_widget", "Catmull-Clark + Loop", None, -1))
        self.sdRule_comboBox.setItemText(1, QtWidgets.QApplication.translate("main_widget", "Catmull-Clark Only", None, -1))
        self.screeSpaceAdaptiveCB.setText(QtWidgets.QApplication.translate("main_widget", "Screen Space Adaptive", None, -1))
        self.smoothSd_CB.setText(QtWidgets.QApplication.translate("main_widget", "Smooth Subdivision", None, -1))
        self.miniEdgeLength_label.setText(QtWidgets.QApplication.translate("main_widget", "Minimum Edge Length", None, -1))
        self.maxSd_label.setText(QtWidgets.QApplication.translate("main_widget", "Maximum Subdivitions", None, -1))
        self.outOfFrustumTessFactor_label.setText(QtWidgets.QApplication.translate("main_widget", "Out of Frustum Tess. Factor", None, -1))
        self.displacement_label.setText(QtWidgets.QApplication.translate("main_widget", "Displacement", None, -1))
        self.dm_enable_CB.setText(QtWidgets.QApplication.translate("main_widget", "Enable", None, -1))
        self.maximum_dm_label.setText(QtWidgets.QApplication.translate("main_widget", "Maximum Displacement", None, -1))
        self.dm_scale_label.setText(QtWidgets.QApplication.translate("main_widget", "Displacement Scale", None, -1))
        self.enable_auto_bump_mapping_CB.setText(QtWidgets.QApplication.translate("main_widget", "Enable Auto Bump Mapping", None, -1))
