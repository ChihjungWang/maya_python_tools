# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/pixiTools_export_spine_json.ui',
# licensing of 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/pixiTools_export_spine_json.ui' applies.
#
# Created: Thu Sep  8 12:14:43 2022
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.flag_commend_layout = QtWidgets.QFormLayout()
        self.flag_commend_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.flag_commend_layout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.flag_commend_layout.setContentsMargins(2, 2, 2, 2)
        self.flag_commend_layout.setHorizontalSpacing(8)
        self.flag_commend_layout.setVerticalSpacing(4)
        self.flag_commend_layout.setObjectName("flag_commend_layout")
        self.create_plane_label = QtWidgets.QLabel(main_widget)
        self.create_plane_label.setMinimumSize(QtCore.QSize(140, 0))
        self.create_plane_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.create_plane_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_plane_label.setObjectName("create_plane_label")
        self.flag_commend_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.create_plane_label)
        self.createPlane_layout = QtWidgets.QHBoxLayout()
        self.createPlane_layout.setSpacing(4)
        self.createPlane_layout.setObjectName("createPlane_layout")
        self.createPlaneW_label = QtWidgets.QLabel(main_widget)
        self.createPlaneW_label.setMinimumSize(QtCore.QSize(30, 0))
        self.createPlaneW_label.setAlignment(QtCore.Qt.AlignCenter)
        self.createPlaneW_label.setObjectName("createPlaneW_label")
        self.createPlane_layout.addWidget(self.createPlaneW_label)
        self.createPlaneW_LE = QtWidgets.QLineEdit(main_widget)
        self.createPlaneW_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.createPlaneW_LE.setObjectName("createPlaneW_LE")
        self.createPlane_layout.addWidget(self.createPlaneW_LE)
        self.createPlaneH_label = QtWidgets.QLabel(main_widget)
        self.createPlaneH_label.setMinimumSize(QtCore.QSize(30, 0))
        self.createPlaneH_label.setAlignment(QtCore.Qt.AlignCenter)
        self.createPlaneH_label.setObjectName("createPlaneH_label")
        self.createPlane_layout.addWidget(self.createPlaneH_label)
        self.createPlaneH_LE = QtWidgets.QLineEdit(main_widget)
        self.createPlaneH_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.createPlaneH_LE.setObjectName("createPlaneH_LE")
        self.createPlane_layout.addWidget(self.createPlaneH_LE)
        self.nums_label = QtWidgets.QLabel(main_widget)
        self.nums_label.setObjectName("nums_label")
        self.createPlane_layout.addWidget(self.nums_label)
        self.nums_LE = QtWidgets.QLineEdit(main_widget)
        self.nums_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.nums_LE.setObjectName("nums_LE")
        self.createPlane_layout.addWidget(self.nums_LE)
        self.createPlane_PB = QtWidgets.QPushButton(main_widget)
        self.createPlane_PB.setObjectName("createPlane_PB")
        self.createPlane_layout.addWidget(self.createPlane_PB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.createPlane_layout.addItem(spacerItem)
        self.flag_commend_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.createPlane_layout)
        self.planeRenameEdit_label = QtWidgets.QLabel(main_widget)
        self.planeRenameEdit_label.setMinimumSize(QtCore.QSize(140, 0))
        self.planeRenameEdit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.planeRenameEdit_label.setObjectName("planeRenameEdit_label")
        self.flag_commend_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.planeRenameEdit_label)
        self.autoRename_layout = QtWidgets.QHBoxLayout()
        self.autoRename_layout.setSpacing(4)
        self.autoRename_layout.setObjectName("autoRename_layout")
        self.autoRename_LE = QtWidgets.QLineEdit(main_widget)
        self.autoRename_LE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.autoRename_LE.setText("")
        self.autoRename_LE.setReadOnly(False)
        self.autoRename_LE.setObjectName("autoRename_LE")
        self.autoRename_layout.addWidget(self.autoRename_LE)
        self.autoRename_PB = QtWidgets.QPushButton(main_widget)
        self.autoRename_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.autoRename_PB.setObjectName("autoRename_PB")
        self.autoRename_layout.addWidget(self.autoRename_PB)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.autoRename_layout.addItem(spacerItem1)
        self.flag_commend_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.autoRename_layout)
        self.textureFile_label = QtWidgets.QLabel(main_widget)
        self.textureFile_label.setMinimumSize(QtCore.QSize(140, 0))
        self.textureFile_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textureFile_label.setObjectName("textureFile_label")
        self.flag_commend_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.textureFile_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textureFile_LE = QtWidgets.QLineEdit(main_widget)
        self.textureFile_LE.setObjectName("textureFile_LE")
        self.horizontalLayout_5.addWidget(self.textureFile_LE)
        self.textureFileBro_PB = QtWidgets.QPushButton(main_widget)
        self.textureFileBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.textureFileBro_PB.setObjectName("textureFileBro_PB")
        self.horizontalLayout_5.addWidget(self.textureFileBro_PB)
        self.textureFileOpen_PB = QtWidgets.QPushButton(main_widget)
        self.textureFileOpen_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.textureFileOpen_PB.setObjectName("textureFileOpen_PB")
        self.horizontalLayout_5.addWidget(self.textureFileOpen_PB)
        self.flag_commend_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.shadeEdit_label = QtWidgets.QLabel(main_widget)
        self.shadeEdit_label.setMinimumSize(QtCore.QSize(140, 0))
        self.shadeEdit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shadeEdit_label.setObjectName("shadeEdit_label")
        self.flag_commend_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.shadeEdit_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.createLambert_PB = QtWidgets.QPushButton(main_widget)
        self.createLambert_PB.setObjectName("createLambert_PB")
        self.horizontalLayout_4.addWidget(self.createLambert_PB)
        self.planeEditFixSize_PB = QtWidgets.QPushButton(main_widget)
        self.planeEditFixSize_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.planeEditFixSize_PB.setObjectName("planeEditFixSize_PB")
        self.horizontalLayout_4.addWidget(self.planeEditFixSize_PB)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.flag_commend_layout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.canvasCam_label = QtWidgets.QLabel(main_widget)
        self.canvasCam_label.setMinimumSize(QtCore.QSize(140, 0))
        self.canvasCam_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.canvasCam_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.canvasCam_label.setObjectName("canvasCam_label")
        self.flag_commend_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.canvasCam_label)
        self.canvasCam_layout = QtWidgets.QHBoxLayout()
        self.canvasCam_layout.setSpacing(4)
        self.canvasCam_layout.setObjectName("canvasCam_layout")
        self.canvasCam_LE = QtWidgets.QLineEdit(main_widget)
        self.canvasCam_LE.setMaximumSize(QtCore.QSize(160, 16777215))
        self.canvasCam_LE.setObjectName("canvasCam_LE")
        self.canvasCam_layout.addWidget(self.canvasCam_LE)
        self.canvasCamSetUp_PB = QtWidgets.QPushButton(main_widget)
        self.canvasCamSetUp_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.canvasCamSetUp_PB.setObjectName("canvasCamSetUp_PB")
        self.canvasCam_layout.addWidget(self.canvasCamSetUp_PB)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.canvasCam_layout.addItem(spacerItem3)
        self.flag_commend_layout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.canvasCam_layout)
        self.canvasSize_label = QtWidgets.QLabel(main_widget)
        self.canvasSize_label.setMinimumSize(QtCore.QSize(140, 0))
        self.canvasSize_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.canvasSize_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.canvasSize_label.setObjectName("canvasSize_label")
        self.flag_commend_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.canvasSize_label)
        self.canvasSize_layout = QtWidgets.QHBoxLayout()
        self.canvasSize_layout.setSpacing(4)
        self.canvasSize_layout.setObjectName("canvasSize_layout")
        self.canvasSizeW_label = QtWidgets.QLabel(main_widget)
        self.canvasSizeW_label.setMinimumSize(QtCore.QSize(30, 0))
        self.canvasSizeW_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canvasSizeW_label.setAlignment(QtCore.Qt.AlignCenter)
        self.canvasSizeW_label.setObjectName("canvasSizeW_label")
        self.canvasSize_layout.addWidget(self.canvasSizeW_label)
        self.canvasSizeW_LE = QtWidgets.QLineEdit(main_widget)
        self.canvasSizeW_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canvasSizeW_LE.setObjectName("canvasSizeW_LE")
        self.canvasSize_layout.addWidget(self.canvasSizeW_LE)
        self.canvasSizeH_label = QtWidgets.QLabel(main_widget)
        self.canvasSizeH_label.setMinimumSize(QtCore.QSize(30, 0))
        self.canvasSizeH_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canvasSizeH_label.setAlignment(QtCore.Qt.AlignCenter)
        self.canvasSizeH_label.setObjectName("canvasSizeH_label")
        self.canvasSize_layout.addWidget(self.canvasSizeH_label)
        self.canvasSizeH_LE = QtWidgets.QLineEdit(main_widget)
        self.canvasSizeH_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canvasSizeH_LE.setObjectName("canvasSizeH_LE")
        self.canvasSize_layout.addWidget(self.canvasSizeH_LE)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.canvasSize_layout.addItem(spacerItem4)
        self.flag_commend_layout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.canvasSize_layout)
        self.frameRange_label = QtWidgets.QLabel(main_widget)
        self.frameRange_label.setMinimumSize(QtCore.QSize(140, 0))
        self.frameRange_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frameRange_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.frameRange_label.setObjectName("frameRange_label")
        self.flag_commend_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.frameRange_label)
        self.frameRange_layout = QtWidgets.QHBoxLayout()
        self.frameRange_layout.setSpacing(4)
        self.frameRange_layout.setObjectName("frameRange_layout")
        self.frameRangeStart_label = QtWidgets.QLabel(main_widget)
        self.frameRangeStart_label.setMinimumSize(QtCore.QSize(30, 0))
        self.frameRangeStart_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStart_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frameRangeStart_label.setObjectName("frameRangeStart_label")
        self.frameRange_layout.addWidget(self.frameRangeStart_label)
        self.frameRangeStart_LE = QtWidgets.QLineEdit(main_widget)
        self.frameRangeStart_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStart_LE.setMaxLength(4)
        self.frameRangeStart_LE.setObjectName("frameRangeStart_LE")
        self.frameRange_layout.addWidget(self.frameRangeStart_LE)
        self.frameRangeEnd_label = QtWidgets.QLabel(main_widget)
        self.frameRangeEnd_label.setMinimumSize(QtCore.QSize(30, 0))
        self.frameRangeEnd_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeEnd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frameRangeEnd_label.setObjectName("frameRangeEnd_label")
        self.frameRange_layout.addWidget(self.frameRangeEnd_label)
        self.frameRangeEnd_LE = QtWidgets.QLineEdit(main_widget)
        self.frameRangeEnd_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeEnd_LE.setObjectName("frameRangeEnd_LE")
        self.frameRange_layout.addWidget(self.frameRangeEnd_LE)
        self.frameRangeStep_label = QtWidgets.QLabel(main_widget)
        self.frameRangeStep_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStep_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frameRangeStep_label.setObjectName("frameRangeStep_label")
        self.frameRange_layout.addWidget(self.frameRangeStep_label)
        self.frameRangeStep_LE = QtWidgets.QLineEdit(main_widget)
        self.frameRangeStep_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStep_LE.setObjectName("frameRangeStep_LE")
        self.frameRange_layout.addWidget(self.frameRangeStep_LE)
        self.time_label = QtWidgets.QLabel(main_widget)
        self.time_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.frameRange_layout.addWidget(self.time_label)
        self.frameRangeTime_CB = QtWidgets.QComboBox(main_widget)
        self.frameRangeTime_CB.setObjectName("frameRangeTime_CB")
        self.frameRangeTime_CB.addItem("")
        self.frameRangeTime_CB.addItem("")
        self.frameRangeTime_CB.addItem("")
        self.frameRange_layout.addWidget(self.frameRangeTime_CB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frameRange_layout.addItem(spacerItem5)
        self.flag_commend_layout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.frameRange_layout)
        self.label = QtWidgets.QLabel(main_widget)
        self.label.setMinimumSize(QtCore.QSize(140, 0))
        self.label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.flag_commend_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label)
        self.exportPath_label = QtWidgets.QLabel(main_widget)
        self.exportPath_label.setMinimumSize(QtCore.QSize(140, 0))
        self.exportPath_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.exportPath_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exportPath_label.setObjectName("exportPath_label")
        self.flag_commend_layout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.exportPath_label)
        self.outDir_layout = QtWidgets.QHBoxLayout()
        self.outDir_layout.setSpacing(4)
        self.outDir_layout.setObjectName("outDir_layout")
        self.outDir_LE = QtWidgets.QLineEdit(main_widget)
        self.outDir_LE.setObjectName("outDir_LE")
        self.outDir_layout.addWidget(self.outDir_LE)
        self.outDirBro_PB = QtWidgets.QPushButton(main_widget)
        self.outDirBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.outDirBro_PB.setObjectName("outDirBro_PB")
        self.outDir_layout.addWidget(self.outDirBro_PB)
        self.outDirOpen_PB = QtWidgets.QPushButton(main_widget)
        self.outDirOpen_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.outDirOpen_PB.setObjectName("outDirOpen_PB")
        self.outDir_layout.addWidget(self.outDirOpen_PB)
        self.flag_commend_layout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.outDir_layout)
        self.jsonName_label = QtWidgets.QLabel(main_widget)
        self.jsonName_label.setMinimumSize(QtCore.QSize(140, 0))
        self.jsonName_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.jsonName_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jsonName_label.setObjectName("jsonName_label")
        self.flag_commend_layout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.jsonName_label)
        self.jsonName_layout = QtWidgets.QHBoxLayout()
        self.jsonName_layout.setSpacing(4)
        self.jsonName_layout.setObjectName("jsonName_layout")
        self.json_LE = QtWidgets.QLineEdit(main_widget)
        self.json_LE.setMaximumSize(QtCore.QSize(160, 16777215))
        self.json_LE.setObjectName("json_LE")
        self.jsonName_layout.addWidget(self.json_LE)
        self.json_label = QtWidgets.QLabel(main_widget)
        self.json_label.setObjectName("json_label")
        self.jsonName_layout.addWidget(self.json_label)
        self.flag_commend_layout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.jsonName_layout)
        self.rootJoint_label = QtWidgets.QLabel(main_widget)
        self.rootJoint_label.setMinimumSize(QtCore.QSize(140, 0))
        self.rootJoint_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.rootJoint_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rootJoint_label.setObjectName("rootJoint_label")
        self.flag_commend_layout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.rootJoint_label)
        self.rootJoint_layout = QtWidgets.QHBoxLayout()
        self.rootJoint_layout.setSpacing(4)
        self.rootJoint_layout.setObjectName("rootJoint_layout")
        self.rootJoint_LE = QtWidgets.QLineEdit(main_widget)
        self.rootJoint_LE.setMaximumSize(QtCore.QSize(160, 16777215))
        self.rootJoint_LE.setObjectName("rootJoint_LE")
        self.rootJoint_layout.addWidget(self.rootJoint_LE)
        self.rootJointPick_PB = QtWidgets.QPushButton(main_widget)
        self.rootJointPick_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rootJointPick_PB.setObjectName("rootJointPick_PB")
        self.rootJoint_layout.addWidget(self.rootJointPick_PB)
        self.setSameKey_PB = QtWidgets.QPushButton(main_widget)
        self.setSameKey_PB.setObjectName("setSameKey_PB")
        self.rootJoint_layout.addWidget(self.setSameKey_PB)
        self.clearKey_PB = QtWidgets.QPushButton(main_widget)
        self.clearKey_PB.setObjectName("clearKey_PB")
        self.rootJoint_layout.addWidget(self.clearKey_PB)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rootJoint_layout.addItem(spacerItem6)
        self.flag_commend_layout.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.rootJoint_layout)
        self.exportOption_label = QtWidgets.QLabel(main_widget)
        self.exportOption_label.setMinimumSize(QtCore.QSize(140, 0))
        self.exportOption_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.exportOption_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exportOption_label.setObjectName("exportOption_label")
        self.flag_commend_layout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.exportOption_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.speed_label = QtWidgets.QLabel(main_widget)
        self.speed_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout.addWidget(self.speed_label)
        self.speed_doubleSpinBox = QtWidgets.QDoubleSpinBox(main_widget)
        self.speed_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.speed_doubleSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.speed_doubleSpinBox.setDecimals(1)
        self.speed_doubleSpinBox.setMaximum(8.0)
        self.speed_doubleSpinBox.setSingleStep(0.1)
        self.speed_doubleSpinBox.setProperty("value", 1.0)
        self.speed_doubleSpinBox.setObjectName("speed_doubleSpinBox")
        self.horizontalLayout.addWidget(self.speed_doubleSpinBox)
        self.scale_CB = QtWidgets.QCheckBox(main_widget)
        self.scale_CB.setChecked(True)
        self.scale_CB.setObjectName("scale_CB")
        self.horizontalLayout.addWidget(self.scale_CB)
        self.rotation_CB = QtWidgets.QCheckBox(main_widget)
        self.rotation_CB.setChecked(True)
        self.rotation_CB.setObjectName("rotation_CB")
        self.horizontalLayout.addWidget(self.rotation_CB)
        self.rgbpp_CB = QtWidgets.QCheckBox(main_widget)
        self.rgbpp_CB.setObjectName("rgbpp_CB")
        self.horizontalLayout.addWidget(self.rgbpp_CB)
        self.drawOrder_CB = QtWidgets.QCheckBox(main_widget)
        self.drawOrder_CB.setObjectName("drawOrder_CB")
        self.horizontalLayout.addWidget(self.drawOrder_CB)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.flag_commend_layout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.baseAnimLayer_layout = QtWidgets.QHBoxLayout()
        self.baseAnimLayer_layout.setSpacing(4)
        self.baseAnimLayer_layout.setContentsMargins(0, 0, 0, 0)
        self.baseAnimLayer_layout.setObjectName("baseAnimLayer_layout")
        self.none_label = QtWidgets.QLabel(main_widget)
        self.none_label.setMinimumSize(QtCore.QSize(80, 0))
        self.none_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.none_label.setObjectName("none_label")
        self.baseAnimLayer_layout.addWidget(self.none_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.baseAnimLayer_layout.addItem(spacerItem8)
        self.flag_commend_layout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.baseAnimLayer_layout)
        self.label_2 = QtWidgets.QLabel(main_widget)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.flag_commend_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.getChildJoint_PB = QtWidgets.QPushButton(main_widget)
        self.getChildJoint_PB.setObjectName("getChildJoint_PB")
        self.horizontalLayout_2.addWidget(self.getChildJoint_PB)
        self.clearAllKey_PB = QtWidgets.QPushButton(main_widget)
        self.clearAllKey_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.clearAllKey_PB.setObjectName("clearAllKey_PB")
        self.horizontalLayout_2.addWidget(self.clearAllKey_PB)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.flag_commend_layout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.flag_commend_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shaderSetToDefault_PB = QtWidgets.QPushButton(main_widget)
        self.shaderSetToDefault_PB.setObjectName("shaderSetToDefault_PB")
        self.horizontalLayout_3.addWidget(self.shaderSetToDefault_PB)
        self.exportJsonSpine_PB = QtWidgets.QPushButton(main_widget)
        self.exportJsonSpine_PB.setObjectName("exportJsonSpine_PB")
        self.horizontalLayout_3.addWidget(self.exportJsonSpine_PB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.info_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.info_label.setFont(font)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.create_plane_label.setText(QtWidgets.QApplication.translate("main_widget", "Set Create Plane", None, -1))
        self.createPlaneW_label.setText(QtWidgets.QApplication.translate("main_widget", "width", None, -1))
        self.createPlaneW_LE.setText(QtWidgets.QApplication.translate("main_widget", "20", None, -1))
        self.createPlaneH_label.setText(QtWidgets.QApplication.translate("main_widget", "height", None, -1))
        self.createPlaneH_LE.setText(QtWidgets.QApplication.translate("main_widget", "40", None, -1))
        self.nums_label.setText(QtWidgets.QApplication.translate("main_widget", "Nums", None, -1))
        self.nums_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.createPlane_PB.setText(QtWidgets.QApplication.translate("main_widget", "Create", None, -1))
        self.planeRenameEdit_label.setText(QtWidgets.QApplication.translate("main_widget", "Auto Rename", None, -1))
        self.autoRename_PB.setText(QtWidgets.QApplication.translate("main_widget", "Rename", None, -1))
        self.textureFile_label.setText(QtWidgets.QApplication.translate("main_widget", "Texture file", None, -1))
        self.textureFileBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.textureFileOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "Open", None, -1))
        self.shadeEdit_label.setText(QtWidgets.QApplication.translate("main_widget", "Shader Edit", None, -1))
        self.createLambert_PB.setText(QtWidgets.QApplication.translate("main_widget", "Create lambert", None, -1))
        self.planeEditFixSize_PB.setText(QtWidgets.QApplication.translate("main_widget", "Fix Mesh Size", None, -1))
        self.canvasCam_label.setText(QtWidgets.QApplication.translate("main_widget", "Canvas Camera", None, -1))
        self.canvasCam_LE.setText(QtWidgets.QApplication.translate("main_widget", "canvasCam", None, -1))
        self.canvasCamSetUp_PB.setText(QtWidgets.QApplication.translate("main_widget", "Set Up", None, -1))
        self.canvasSize_label.setText(QtWidgets.QApplication.translate("main_widget", "Canvas Size", None, -1))
        self.canvasSizeW_label.setText(QtWidgets.QApplication.translate("main_widget", "width", None, -1))
        self.canvasSizeW_LE.setText(QtWidgets.QApplication.translate("main_widget", "1920", None, -1))
        self.canvasSizeH_label.setText(QtWidgets.QApplication.translate("main_widget", "height", None, -1))
        self.canvasSizeH_LE.setText(QtWidgets.QApplication.translate("main_widget", "1080", None, -1))
        self.frameRange_label.setText(QtWidgets.QApplication.translate("main_widget", "Frame Range", None, -1))
        self.frameRangeStart_label.setText(QtWidgets.QApplication.translate("main_widget", "start", None, -1))
        self.frameRangeStart_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.frameRangeEnd_label.setText(QtWidgets.QApplication.translate("main_widget", "end", None, -1))
        self.frameRangeEnd_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.frameRangeStep_label.setText(QtWidgets.QApplication.translate("main_widget", "step", None, -1))
        self.frameRangeStep_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.time_label.setText(QtWidgets.QApplication.translate("main_widget", "time", None, -1))
        self.frameRangeTime_CB.setItemText(0, QtWidgets.QApplication.translate("main_widget", "24 fps", None, -1))
        self.frameRangeTime_CB.setItemText(1, QtWidgets.QApplication.translate("main_widget", "30 fps", None, -1))
        self.frameRangeTime_CB.setItemText(2, QtWidgets.QApplication.translate("main_widget", "60 fps", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("main_widget", "Animation Layer", None, -1))
        self.exportPath_label.setText(QtWidgets.QApplication.translate("main_widget", "Export Path", None, -1))
        self.outDirBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.outDirOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "open", None, -1))
        self.jsonName_label.setText(QtWidgets.QApplication.translate("main_widget", "Json Name", None, -1))
        self.json_label.setText(QtWidgets.QApplication.translate("main_widget", ".json", None, -1))
        self.rootJoint_label.setText(QtWidgets.QApplication.translate("main_widget", "Root Joint", None, -1))
        self.rootJointPick_PB.setText(QtWidgets.QApplication.translate("main_widget", "Pick", None, -1))
        self.setSameKey_PB.setText(QtWidgets.QApplication.translate("main_widget", "set same key", None, -1))
        self.clearKey_PB.setText(QtWidgets.QApplication.translate("main_widget", "clear key", None, -1))
        self.exportOption_label.setText(QtWidgets.QApplication.translate("main_widget", "Export Option", None, -1))
        self.speed_label.setText(QtWidgets.QApplication.translate("main_widget", "speed", None, -1))
        self.scale_CB.setText(QtWidgets.QApplication.translate("main_widget", "Scale", None, -1))
        self.rotation_CB.setText(QtWidgets.QApplication.translate("main_widget", "Rotation", None, -1))
        self.rgbpp_CB.setText(QtWidgets.QApplication.translate("main_widget", "RgbPP", None, -1))
        self.drawOrder_CB.setText(QtWidgets.QApplication.translate("main_widget", "DrawOrder", None, -1))
        self.none_label.setText(QtWidgets.QApplication.translate("main_widget", "none", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("main_widget", "Set key To aniLayer", None, -1))
        self.getChildJoint_PB.setText(QtWidgets.QApplication.translate("main_widget", "get child joint", None, -1))
        self.clearAllKey_PB.setText(QtWidgets.QApplication.translate("main_widget", "clear all key", None, -1))
        self.shaderSetToDefault_PB.setText(QtWidgets.QApplication.translate("main_widget", "Shader Set To Default Layer", None, -1))
        self.exportJsonSpine_PB.setText(QtWidgets.QApplication.translate("main_widget", "Export Json Spine", None, -1))
        self.info_label.setText(QtWidgets.QApplication.translate("main_widget", "Doing...", None, -1))

