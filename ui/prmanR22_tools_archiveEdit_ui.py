# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/prmanR22_tools_archiveEdit.ui',
# licensing of 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/prmanR22_tools_archiveEdit.ui' applies.
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
        self.archiveExportPath_label = QtWidgets.QLabel(main_widget)
        self.archiveExportPath_label.setMinimumSize(QtCore.QSize(140, 0))
        self.archiveExportPath_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.archiveExportPath_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.archiveExportPath_label.setObjectName("archiveExportPath_label")
        self.flag_commend_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.archiveExportPath_label)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.archiveExportPath_LE = QtWidgets.QLineEdit(main_widget)
        self.archiveExportPath_LE.setObjectName("archiveExportPath_LE")
        self.horizontalLayout_11.addWidget(self.archiveExportPath_LE)
        self.archiveExportBro_PB = QtWidgets.QPushButton(main_widget)
        self.archiveExportBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.archiveExportBro_PB.setObjectName("archiveExportBro_PB")
        self.horizontalLayout_11.addWidget(self.archiveExportBro_PB)
        self.archiveExportOpen_PB = QtWidgets.QPushButton(main_widget)
        self.archiveExportOpen_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.archiveExportOpen_PB.setObjectName("archiveExportOpen_PB")
        self.horizontalLayout_11.addWidget(self.archiveExportOpen_PB)
        self.flag_commend_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.exportName_label = QtWidgets.QLabel(main_widget)
        self.exportName_label.setMinimumSize(QtCore.QSize(140, 0))
        self.exportName_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.exportName_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exportName_label.setObjectName("exportName_label")
        self.flag_commend_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.exportName_label)
        self.exportName_layout = QtWidgets.QHBoxLayout()
        self.exportName_layout.setSpacing(2)
        self.exportName_layout.setObjectName("exportName_layout")
        self.exportName_LE = QtWidgets.QLineEdit(main_widget)
        self.exportName_LE.setMinimumSize(QtCore.QSize(150, 0))
        self.exportName_LE.setMaximumSize(QtCore.QSize(150, 16777215))
        self.exportName_LE.setObjectName("exportName_LE")
        self.exportName_layout.addWidget(self.exportName_LE)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.exportName_layout.addItem(spacerItem)
        self.flag_commend_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.exportName_layout)
        self.rootGroup_label = QtWidgets.QLabel(main_widget)
        self.rootGroup_label.setMinimumSize(QtCore.QSize(140, 0))
        self.rootGroup_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.rootGroup_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rootGroup_label.setObjectName("rootGroup_label")
        self.flag_commend_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rootGroup_label)
        self.rootGroup_layout = QtWidgets.QHBoxLayout()
        self.rootGroup_layout.setSpacing(2)
        self.rootGroup_layout.setObjectName("rootGroup_layout")
        self.rootGroup_LE = QtWidgets.QLineEdit(main_widget)
        self.rootGroup_LE.setMinimumSize(QtCore.QSize(150, 0))
        self.rootGroup_LE.setMaximumSize(QtCore.QSize(150, 16777215))
        self.rootGroup_LE.setObjectName("rootGroup_LE")
        self.rootGroup_layout.addWidget(self.rootGroup_LE)
        self.rootGroup_pick_PB = QtWidgets.QPushButton(main_widget)
        self.rootGroup_pick_PB.setMinimumSize(QtCore.QSize(80, 0))
        self.rootGroup_pick_PB.setMaximumSize(QtCore.QSize(80, 16777215))
        self.rootGroup_pick_PB.setObjectName("rootGroup_pick_PB")
        self.rootGroup_layout.addWidget(self.rootGroup_pick_PB)
        self.selectSg_PB = QtWidgets.QPushButton(main_widget)
        self.selectSg_PB.setMinimumSize(QtCore.QSize(80, 0))
        self.selectSg_PB.setMaximumSize(QtCore.QSize(80, 16777215))
        self.selectSg_PB.setObjectName("selectSg_PB")
        self.rootGroup_layout.addWidget(self.selectSg_PB)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rootGroup_layout.addItem(spacerItem1)
        self.flag_commend_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.rootGroup_layout)
        self.shaderTagEdit_label = QtWidgets.QLabel(main_widget)
        self.shaderTagEdit_label.setMinimumSize(QtCore.QSize(140, 0))
        self.shaderTagEdit_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.shaderTagEdit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shaderTagEdit_label.setObjectName("shaderTagEdit_label")
        self.flag_commend_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.shaderTagEdit_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tagEditTagNme_label = QtWidgets.QLabel(main_widget)
        self.tagEditTagNme_label.setObjectName("tagEditTagNme_label")
        self.horizontalLayout_4.addWidget(self.tagEditTagNme_label)
        self.tagEditName_LE = QtWidgets.QLineEdit(main_widget)
        self.tagEditName_LE.setMinimumSize(QtCore.QSize(100, 0))
        self.tagEditName_LE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tagEditName_LE.setObjectName("tagEditName_LE")
        self.horizontalLayout_4.addWidget(self.tagEditName_LE)
        self.tagEditAdd_PB = QtWidgets.QPushButton(main_widget)
        self.tagEditAdd_PB.setMinimumSize(QtCore.QSize(80, 0))
        self.tagEditAdd_PB.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tagEditAdd_PB.setObjectName("tagEditAdd_PB")
        self.horizontalLayout_4.addWidget(self.tagEditAdd_PB)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.flag_commend_layout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(main_widget)
        self.label.setMinimumSize(QtCore.QSize(140, 0))
        self.label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.flag_commend_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameRange_comboBox = QtWidgets.QComboBox(main_widget)
        self.frameRange_comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.frameRange_comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frameRange_comboBox.setObjectName("frameRange_comboBox")
        self.frameRange_comboBox.addItem("")
        self.frameRange_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.frameRange_comboBox)
        self.startFrame_label = QtWidgets.QLabel(main_widget)
        self.startFrame_label.setObjectName("startFrame_label")
        self.horizontalLayout_2.addWidget(self.startFrame_label)
        self.startFrame_LE = QtWidgets.QLineEdit(main_widget)
        self.startFrame_LE.setMinimumSize(QtCore.QSize(50, 0))
        self.startFrame_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.startFrame_LE.setObjectName("startFrame_LE")
        self.horizontalLayout_2.addWidget(self.startFrame_LE)
        self.end_frame_label = QtWidgets.QLabel(main_widget)
        self.end_frame_label.setObjectName("end_frame_label")
        self.horizontalLayout_2.addWidget(self.end_frame_label)
        self.endFrame_LE = QtWidgets.QLineEdit(main_widget)
        self.endFrame_LE.setMinimumSize(QtCore.QSize(50, 0))
        self.endFrame_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.endFrame_LE.setObjectName("endFrame_LE")
        self.horizontalLayout_2.addWidget(self.endFrame_LE)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.flag_commend_layout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.exportData_label = QtWidgets.QLabel(main_widget)
        self.exportData_label.setMinimumSize(QtCore.QSize(140, 0))
        self.exportData_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.exportData_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exportData_label.setObjectName("exportData_label")
        self.flag_commend_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.exportData_label)
        self.exportdata_layout = QtWidgets.QHBoxLayout()
        self.exportdata_layout.setSpacing(2)
        self.exportdata_layout.setObjectName("exportdata_layout")
        self.exportGpuCache_CB = QtWidgets.QCheckBox(main_widget)
        self.exportGpuCache_CB.setObjectName("exportGpuCache_CB")
        self.exportdata_layout.addWidget(self.exportGpuCache_CB)
        self.exportRlf_CB = QtWidgets.QCheckBox(main_widget)
        self.exportRlf_CB.setObjectName("exportRlf_CB")
        self.exportdata_layout.addWidget(self.exportRlf_CB)
        self.exportShader_CB = QtWidgets.QCheckBox(main_widget)
        self.exportShader_CB.setObjectName("exportShader_CB")
        self.exportdata_layout.addWidget(self.exportShader_CB)
        self.exportArchive_PB = QtWidgets.QPushButton(main_widget)
        self.exportArchive_PB.setObjectName("exportArchive_PB")
        self.exportdata_layout.addWidget(self.exportArchive_PB)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.exportdata_layout.addItem(spacerItem4)
        self.flag_commend_layout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.exportdata_layout)
        self.verticalLayout.addLayout(self.flag_commend_layout)
        self.line = QtWidgets.QFrame(main_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.importGpuCache_label = QtWidgets.QLabel(main_widget)
        self.importGpuCache_label.setMinimumSize(QtCore.QSize(140, 0))
        self.importGpuCache_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.importGpuCache_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.importGpuCache_label.setObjectName("importGpuCache_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.importGpuCache_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.importGpuCachePath_LE = QtWidgets.QLineEdit(main_widget)
        self.importGpuCachePath_LE.setObjectName("importGpuCachePath_LE")
        self.horizontalLayout_3.addWidget(self.importGpuCachePath_LE)
        self.importGpuCachePathBro_PB = QtWidgets.QPushButton(main_widget)
        self.importGpuCachePathBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.importGpuCachePathBro_PB.setObjectName("importGpuCachePathBro_PB")
        self.horizontalLayout_3.addWidget(self.importGpuCachePathBro_PB)
        self.importGpuCachePathOpen_PB = QtWidgets.QPushButton(main_widget)
        self.importGpuCachePathOpen_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.importGpuCachePathOpen_PB.setObjectName("importGpuCachePathOpen_PB")
        self.horizontalLayout_3.addWidget(self.importGpuCachePathOpen_PB)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tagEditTagNme2_label = QtWidgets.QLabel(main_widget)
        self.tagEditTagNme2_label.setObjectName("tagEditTagNme2_label")
        self.horizontalLayout_5.addWidget(self.tagEditTagNme2_label)
        self.tagEditName2_LE = QtWidgets.QLineEdit(main_widget)
        self.tagEditName2_LE.setMinimumSize(QtCore.QSize(100, 0))
        self.tagEditName2_LE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tagEditName2_LE.setObjectName("tagEditName2_LE")
        self.horizontalLayout_5.addWidget(self.tagEditName2_LE)
        self.selSgWithTag_PB = QtWidgets.QPushButton(main_widget)
        self.selSgWithTag_PB.setMinimumSize(QtCore.QSize(120, 0))
        self.selSgWithTag_PB.setMaximumSize(QtCore.QSize(120, 16777215))
        self.selSgWithTag_PB.setObjectName("selSgWithTag_PB")
        self.horizontalLayout_5.addWidget(self.selSgWithTag_PB)
        self.tagEditDelShader_PB = QtWidgets.QPushButton(main_widget)
        self.tagEditDelShader_PB.setMinimumSize(QtCore.QSize(120, 0))
        self.tagEditDelShader_PB.setMaximumSize(QtCore.QSize(120, 16777215))
        self.tagEditDelShader_PB.setObjectName("tagEditDelShader_PB")
        self.horizontalLayout_5.addWidget(self.tagEditDelShader_PB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.loadData_label = QtWidgets.QLabel(main_widget)
        self.loadData_label.setMinimumSize(QtCore.QSize(140, 0))
        self.loadData_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.loadData_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loadData_label.setObjectName("loadData_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.loadData_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importGpuCache_CB = QtWidgets.QCheckBox(main_widget)
        self.importGpuCache_CB.setObjectName("importGpuCache_CB")
        self.horizontalLayout.addWidget(self.importGpuCache_CB)
        self.importShader_CB = QtWidgets.QCheckBox(main_widget)
        self.importShader_CB.setObjectName("importShader_CB")
        self.horizontalLayout.addWidget(self.importShader_CB)
        self.importArchive_PB = QtWidgets.QPushButton(main_widget)
        self.importArchive_PB.setObjectName("importArchive_PB")
        self.horizontalLayout.addWidget(self.importArchive_PB)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.shaderTagEdit2_label = QtWidgets.QLabel(main_widget)
        self.shaderTagEdit2_label.setMinimumSize(QtCore.QSize(140, 0))
        self.shaderTagEdit2_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.shaderTagEdit2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shaderTagEdit2_label.setObjectName("shaderTagEdit2_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.shaderTagEdit2_label)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(main_widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(2, 2, 2, 2)
        self.formLayout_2.setHorizontalSpacing(8)
        self.formLayout_2.setVerticalSpacing(4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.importGpuCache_label_2 = QtWidgets.QLabel(main_widget)
        self.importGpuCache_label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.importGpuCache_label_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.importGpuCache_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.importGpuCache_label_2.setObjectName("importGpuCache_label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.importGpuCache_label_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.delArnold_PB = QtWidgets.QPushButton(main_widget)
        self.delArnold_PB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delArnold_PB.setObjectName("delArnold_PB")
        self.horizontalLayout_6.addWidget(self.delArnold_PB)
        self.delRenderLayer_PB = QtWidgets.QPushButton(main_widget)
        self.delRenderLayer_PB.setObjectName("delRenderLayer_PB")
        self.horizontalLayout_6.addWidget(self.delRenderLayer_PB)
        self.delRenderSetUp_PB = QtWidgets.QPushButton(main_widget)
        self.delRenderSetUp_PB.setObjectName("delRenderSetUp_PB")
        self.horizontalLayout_6.addWidget(self.delRenderSetUp_PB)
        self.delAov_PB = QtWidgets.QPushButton(main_widget)
        self.delAov_PB.setObjectName("delAov_PB")
        self.horizontalLayout_6.addWidget(self.delAov_PB)
        self.getSgWithRlf_PB = QtWidgets.QPushButton(main_widget)
        self.getSgWithRlf_PB.setObjectName("getSgWithRlf_PB")
        self.horizontalLayout_6.addWidget(self.getSgWithRlf_PB)
        self.setAniForAbc_PB = QtWidgets.QPushButton(main_widget)
        self.setAniForAbc_PB.setObjectName("setAniForAbc_PB")
        self.horizontalLayout_6.addWidget(self.setAniForAbc_PB)
        self.copyUvRigged_PB = QtWidgets.QPushButton(main_widget)
        self.copyUvRigged_PB.setObjectName("copyUvRigged_PB")
        self.horizontalLayout_6.addWidget(self.copyUvRigged_PB)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.line_3 = QtWidgets.QFrame(main_widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.info_label = QtWidgets.QLabel(main_widget)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.archiveExportPath_label.setText(QtWidgets.QApplication.translate("main_widget", "Archive Export Path", None, -1))
        self.archiveExportBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.archiveExportOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "Open", None, -1))
        self.exportName_label.setText(QtWidgets.QApplication.translate("main_widget", "Export Name", None, -1))
        self.rootGroup_label.setText(QtWidgets.QApplication.translate("main_widget", "Root Group", None, -1))
        self.rootGroup_pick_PB.setText(QtWidgets.QApplication.translate("main_widget", "Pick", None, -1))
        self.selectSg_PB.setText(QtWidgets.QApplication.translate("main_widget", "Select SG", None, -1))
        self.shaderTagEdit_label.setText(QtWidgets.QApplication.translate("main_widget", "Shader Tag Edit", None, -1))
        self.tagEditTagNme_label.setText(QtWidgets.QApplication.translate("main_widget", "Tag Name", None, -1))
        self.tagEditAdd_PB.setText(QtWidgets.QApplication.translate("main_widget", "Add Tag", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("main_widget", "Frame Range", None, -1))
        self.frameRange_comboBox.setItemText(0, QtWidgets.QApplication.translate("main_widget", "Current Frame", None, -1))
        self.frameRange_comboBox.setItemText(1, QtWidgets.QApplication.translate("main_widget", "Animation", None, -1))
        self.startFrame_label.setText(QtWidgets.QApplication.translate("main_widget", "Start Frame", None, -1))
        self.startFrame_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.end_frame_label.setText(QtWidgets.QApplication.translate("main_widget", "End Frame", None, -1))
        self.endFrame_LE.setText(QtWidgets.QApplication.translate("main_widget", "1", None, -1))
        self.exportData_label.setText(QtWidgets.QApplication.translate("main_widget", "Export Data", None, -1))
        self.exportGpuCache_CB.setText(QtWidgets.QApplication.translate("main_widget", ".abc", None, -1))
        self.exportRlf_CB.setText(QtWidgets.QApplication.translate("main_widget", ".rlf", None, -1))
        self.exportShader_CB.setText(QtWidgets.QApplication.translate("main_widget", ".mb ( shader )", None, -1))
        self.exportArchive_PB.setText(QtWidgets.QApplication.translate("main_widget", "export", None, -1))
        self.importGpuCache_label.setText(QtWidgets.QApplication.translate("main_widget", "Import Gpu Cache File", None, -1))
        self.importGpuCachePathBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.importGpuCachePathOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "Open", None, -1))
        self.tagEditTagNme2_label.setText(QtWidgets.QApplication.translate("main_widget", "Tag name", None, -1))
        self.selSgWithTag_PB.setText(QtWidgets.QApplication.translate("main_widget", "Select SG With Tag", None, -1))
        self.tagEditDelShader_PB.setText(QtWidgets.QApplication.translate("main_widget", "Delete Old Shader", None, -1))
        self.loadData_label.setText(QtWidgets.QApplication.translate("main_widget", "Load Data", None, -1))
        self.importGpuCache_CB.setText(QtWidgets.QApplication.translate("main_widget", "abc", None, -1))
        self.importShader_CB.setText(QtWidgets.QApplication.translate("main_widget", ".mb (shader)", None, -1))
        self.importArchive_PB.setText(QtWidgets.QApplication.translate("main_widget", "import", None, -1))
        self.shaderTagEdit2_label.setText(QtWidgets.QApplication.translate("main_widget", "Shader Tag Edit", None, -1))
        self.importGpuCache_label_2.setText(QtWidgets.QApplication.translate("main_widget", "Common Functions", None, -1))
        self.delArnold_PB.setText(QtWidgets.QApplication.translate("main_widget", "Del Arnold", None, -1))
        self.delRenderLayer_PB.setText(QtWidgets.QApplication.translate("main_widget", "Del renderLayer", None, -1))
        self.delRenderSetUp_PB.setText(QtWidgets.QApplication.translate("main_widget", "Del renderSetUp", None, -1))
        self.delAov_PB.setText(QtWidgets.QApplication.translate("main_widget", "Del Aov", None, -1))
        self.getSgWithRlf_PB.setText(QtWidgets.QApplication.translate("main_widget", "get SG with Rlf", None, -1))
        self.setAniForAbc_PB.setText(QtWidgets.QApplication.translate("main_widget", "Set ani for abc", None, -1))
        self.copyUvRigged_PB.setText(QtWidgets.QApplication.translate("main_widget", "copyUV(Rigged)", None, -1))
        self.info_label.setText(QtWidgets.QApplication.translate("main_widget", "info bar", None, -1))

