# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/prmanDenoiseToolsCmdR23.ui',
# licensing of 'C:/Users/chihjung/Documents/maya/2023/scripts/ui/prmanDenoiseToolsCmdR23.ui' applies.
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
        self.flag_commend_layout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.flag_commend_layout.setContentsMargins(2, 2, 2, 2)
        self.flag_commend_layout.setSpacing(4)
        self.flag_commend_layout.setObjectName("flag_commend_layout")
        self.varianceFile_label = QtWidgets.QLabel(main_widget)
        self.varianceFile_label.setMinimumSize(QtCore.QSize(140, 0))
        self.varianceFile_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.varianceFile_label.setObjectName("varianceFile_label")
        self.flag_commend_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.varianceFile_label)
        self.varianceFile_layout = QtWidgets.QHBoxLayout()
        self.varianceFile_layout.setSpacing(2)
        self.varianceFile_layout.setObjectName("varianceFile_layout")
        self.varianceFile_LE = QtWidgets.QLineEdit(main_widget)
        self.varianceFile_LE.setObjectName("varianceFile_LE")
        self.varianceFile_layout.addWidget(self.varianceFile_LE)
        self.varianceFileBro_PB = QtWidgets.QPushButton(main_widget)
        self.varianceFileBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.varianceFileBro_PB.setBaseSize(QtCore.QSize(0, 0))
        self.varianceFileBro_PB.setObjectName("varianceFileBro_PB")
        self.varianceFile_layout.addWidget(self.varianceFileBro_PB)
        self.varianceFileOpen_PB = QtWidgets.QPushButton(main_widget)
        self.varianceFileOpen_PB.setObjectName("varianceFileOpen_PB")
        self.varianceFile_layout.addWidget(self.varianceFileOpen_PB)
        self.flag_commend_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.varianceFile_layout)
        self.denoiseFile_label = QtWidgets.QLabel(main_widget)
        self.denoiseFile_label.setMinimumSize(QtCore.QSize(140, 0))
        self.denoiseFile_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.denoiseFile_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.denoiseFile_label.setObjectName("denoiseFile_label")
        self.flag_commend_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.denoiseFile_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.denoiseFile_LE = QtWidgets.QLineEdit(main_widget)
        self.denoiseFile_LE.setObjectName("denoiseFile_LE")
        self.horizontalLayout.addWidget(self.denoiseFile_LE)
        self.denoiseFileBro_PB = QtWidgets.QPushButton(main_widget)
        self.denoiseFileBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.denoiseFileBro_PB.setBaseSize(QtCore.QSize(0, 0))
        self.denoiseFileBro_PB.setObjectName("denoiseFileBro_PB")
        self.horizontalLayout.addWidget(self.denoiseFileBro_PB)
        self.denoiseFileOpen_PB = QtWidgets.QPushButton(main_widget)
        self.denoiseFileOpen_PB.setObjectName("denoiseFileOpen_PB")
        self.horizontalLayout.addWidget(self.denoiseFileOpen_PB)
        self.flag_commend_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.frameRange_label = QtWidgets.QLabel(main_widget)
        self.frameRange_label.setMinimumSize(QtCore.QSize(140, 0))
        self.frameRange_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frameRange_label.setObjectName("frameRange_label")
        self.flag_commend_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.frameRange_label)
        self.frameRange_layout = QtWidgets.QHBoxLayout()
        self.frameRange_layout.setSpacing(2)
        self.frameRange_layout.setObjectName("frameRange_layout")
        self.frameRangeStart_label = QtWidgets.QLabel(main_widget)
        self.frameRangeStart_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStart_label.setObjectName("frameRangeStart_label")
        self.frameRange_layout.addWidget(self.frameRangeStart_label)
        self.frameRangeStart_LE = QtWidgets.QLineEdit(main_widget)
        self.frameRangeStart_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeStart_LE.setMaxLength(4)
        self.frameRangeStart_LE.setObjectName("frameRangeStart_LE")
        self.frameRange_layout.addWidget(self.frameRangeStart_LE)
        self.frameRangeEnd_label = QtWidgets.QLabel(main_widget)
        self.frameRangeEnd_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeEnd_label.setObjectName("frameRangeEnd_label")
        self.frameRange_layout.addWidget(self.frameRangeEnd_label)
        self.frameRangeEnd_LE = QtWidgets.QLineEdit(main_widget)
        self.frameRangeEnd_LE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameRangeEnd_LE.setObjectName("frameRangeEnd_LE")
        self.frameRange_layout.addWidget(self.frameRangeEnd_LE)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frameRange_layout.addItem(spacerItem)
        self.flag_commend_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.frameRange_layout)
        self.newName_CB = QtWidgets.QCheckBox(main_widget)
        self.newName_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.newName_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.newName_CB.setObjectName("newName_CB")
        self.flag_commend_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newName_CB)
        self.newName_layout = QtWidgets.QHBoxLayout()
        self.newName_layout.setSpacing(2)
        self.newName_layout.setObjectName("newName_layout")
        self.imageName_label = QtWidgets.QLabel(main_widget)
        self.imageName_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imageName_label.setObjectName("imageName_label")
        self.newName_layout.addWidget(self.imageName_label)
        self.newName_LE = QtWidgets.QLineEdit(main_widget)
        self.newName_LE.setEnabled(True)
        self.newName_LE.setMinimumSize(QtCore.QSize(100, 0))
        self.newName_LE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.newName_LE.setObjectName("newName_LE")
        self.newName_layout.addWidget(self.newName_LE)
        self.newName_label = QtWidgets.QLabel(main_widget)
        self.newName_label.setObjectName("newName_label")
        self.newName_layout.addWidget(self.newName_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.newName_layout.addItem(spacerItem1)
        self.flag_commend_layout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.newName_layout)
        self.outputBasename_CB = QtWidgets.QCheckBox(main_widget)
        self.outputBasename_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.outputBasename_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.outputBasename_CB.setObjectName("outputBasename_CB")
        self.flag_commend_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.outputBasename_CB)
        self.output_dir_CB = QtWidgets.QCheckBox(main_widget)
        self.output_dir_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.output_dir_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.output_dir_CB.setObjectName("output_dir_CB")
        self.flag_commend_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.output_dir_CB)
        self.outDir_layout = QtWidgets.QHBoxLayout()
        self.outDir_layout.setSpacing(2)
        self.outDir_layout.setObjectName("outDir_layout")
        self.outDir_LE = QtWidgets.QLineEdit(main_widget)
        self.outDir_LE.setObjectName("outDir_LE")
        self.outDir_layout.addWidget(self.outDir_LE)
        self.outDirBro_PB = QtWidgets.QPushButton(main_widget)
        self.outDirBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.outDirBro_PB.setObjectName("outDirBro_PB")
        self.outDir_layout.addWidget(self.outDirBro_PB)
        self.outDirOpen_PB = QtWidgets.QPushButton(main_widget)
        self.outDirOpen_PB.setObjectName("outDirOpen_PB")
        self.outDir_layout.addWidget(self.outDirOpen_PB)
        self.flag_commend_layout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.outDir_layout)
        self.filterVariance_CB = QtWidgets.QCheckBox(main_widget)
        self.filterVariance_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.filterVariance_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.filterVariance_CB.setObjectName("filterVariance_CB")
        self.flag_commend_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.filterVariance_CB)
        self.crossFrame_CB = QtWidgets.QCheckBox(main_widget)
        self.crossFrame_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.crossFrame_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.crossFrame_CB.setObjectName("crossFrame_CB")
        self.flag_commend_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.crossFrame_CB)
        self.skipFirst_CB = QtWidgets.QCheckBox(main_widget)
        self.skipFirst_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.skipFirst_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.skipFirst_CB.setObjectName("skipFirst_CB")
        self.flag_commend_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.skipFirst_CB)
        self.skipLast_CB = QtWidgets.QCheckBox(main_widget)
        self.skipLast_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.skipLast_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.skipLast_CB.setObjectName("skipLast_CB")
        self.flag_commend_layout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.skipLast_CB)
        self.filterLayersIndependently_CB = QtWidgets.QCheckBox(main_widget)
        self.filterLayersIndependently_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.filterLayersIndependently_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.filterLayersIndependently_CB.setObjectName("filterLayersIndependently_CB")
        self.flag_commend_layout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.filterLayersIndependently_CB)
        self.layer_CB = QtWidgets.QCheckBox(main_widget)
        self.layer_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.layer_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.layer_CB.setObjectName("layer_CB")
        self.flag_commend_layout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.layer_CB)
        self.layer_LE = QtWidgets.QLineEdit(main_widget)
        self.layer_LE.setText("")
        self.layer_LE.setObjectName("layer_LE")
        self.flag_commend_layout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.layer_LE)
        self.motionVector_CB = QtWidgets.QCheckBox(main_widget)
        self.motionVector_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.motionVector_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.motionVector_CB.setObjectName("motionVector_CB")
        self.flag_commend_layout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.motionVector_CB)
        self.motionVector_LE = QtWidgets.QLineEdit(main_widget)
        self.motionVector_LE.setText("")
        self.motionVector_LE.setObjectName("motionVector_LE")
        self.flag_commend_layout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.motionVector_LE)
        self.configFile_CB = QtWidgets.QCheckBox(main_widget)
        self.configFile_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.configFile_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.configFile_CB.setObjectName("configFile_CB")
        self.flag_commend_layout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.configFile_CB)
        self.json_layut = QtWidgets.QHBoxLayout()
        self.json_layut.setSpacing(2)
        self.json_layut.setObjectName("json_layut")
        self.json_LE = QtWidgets.QLineEdit(main_widget)
        self.json_LE.setObjectName("json_LE")
        self.json_layut.addWidget(self.json_LE)
        self.json_window_PB = QtWidgets.QPushButton(main_widget)
        self.json_window_PB.setObjectName("json_window_PB")
        self.json_layut.addWidget(self.json_window_PB)
        self.flag_commend_layout.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.json_layut)
        self.nOfThreads_CB = QtWidgets.QCheckBox(main_widget)
        self.nOfThreads_CB.setMinimumSize(QtCore.QSize(140, 0))
        self.nOfThreads_CB.setMaximumSize(QtCore.QSize(140, 16777215))
        self.nOfThreads_CB.setObjectName("nOfThreads_CB")
        self.flag_commend_layout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.nOfThreads_CB)
        self.nOfThreads_SB = QtWidgets.QSpinBox(main_widget)
        self.nOfThreads_SB.setObjectName("nOfThreads_SB")
        self.flag_commend_layout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.nOfThreads_SB)
        self.GPU_CB = QtWidgets.QCheckBox(main_widget)
        self.GPU_CB.setObjectName("GPU_CB")
        self.flag_commend_layout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.GPU_CB)
        self.verticalLayout.addLayout(self.flag_commend_layout)
        self.runCommend_textEdit = QtWidgets.QTextEdit(main_widget)
        self.runCommend_textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.runCommend_textEdit.setObjectName("runCommend_textEdit")
        self.verticalLayout.addWidget(self.runCommend_textEdit)
        self.runCommend_layout = QtWidgets.QHBoxLayout()
        self.runCommend_layout.setSpacing(4)
        self.runCommend_layout.setContentsMargins(2, 2, 2, 2)
        self.runCommend_layout.setObjectName("runCommend_layout")
        self.deadlineSet_CB = QtWidgets.QCheckBox(main_widget)
        self.deadlineSet_CB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.deadlineSet_CB.setObjectName("deadlineSet_CB")
        self.runCommend_layout.addWidget(self.deadlineSet_CB)
        self.mergeExr_CB = QtWidgets.QCheckBox(main_widget)
        self.mergeExr_CB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mergeExr_CB.setObjectName("mergeExr_CB")
        self.runCommend_layout.addWidget(self.mergeExr_CB)
        self.jobName_label = QtWidgets.QLabel(main_widget)
        self.jobName_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.jobName_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jobName_label.setObjectName("jobName_label")
        self.runCommend_layout.addWidget(self.jobName_label)
        self.jobName_LE = QtWidgets.QLineEdit(main_widget)
        self.jobName_LE.setMaximumSize(QtCore.QSize(200, 16777215))
        self.jobName_LE.setObjectName("jobName_LE")
        self.runCommend_layout.addWidget(self.jobName_LE)
        self.rebuildBat_PB = QtWidgets.QPushButton(main_widget)
        self.rebuildBat_PB.setObjectName("rebuildBat_PB")
        self.runCommend_layout.addWidget(self.rebuildBat_PB)
        self.exportBat_PB = QtWidgets.QPushButton(main_widget)
        self.exportBat_PB.setObjectName("exportBat_PB")
        self.runCommend_layout.addWidget(self.exportBat_PB)
        self.verticalLayout.addLayout(self.runCommend_layout)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.varianceFile_label.setText(QtWidgets.QApplication.translate("main_widget", "variance file", None, -1))
        self.varianceFileBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.varianceFileOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "open", None, -1))
        self.denoiseFile_label.setText(QtWidgets.QApplication.translate("main_widget", "denoise file", None, -1))
        self.denoiseFileBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.denoiseFileOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "open", None, -1))
        self.frameRange_label.setText(QtWidgets.QApplication.translate("main_widget", "frame range", None, -1))
        self.frameRangeStart_label.setText(QtWidgets.QApplication.translate("main_widget", "start", None, -1))
        self.frameRangeStart_LE.setText(QtWidgets.QApplication.translate("main_widget", "0001", None, -1))
        self.frameRangeEnd_label.setText(QtWidgets.QApplication.translate("main_widget", "end", None, -1))
        self.frameRangeEnd_LE.setText(QtWidgets.QApplication.translate("main_widget", "0001", None, -1))
        self.newName_CB.setText(QtWidgets.QApplication.translate("main_widget", "name", None, -1))
        self.imageName_label.setText(QtWidgets.QApplication.translate("main_widget", "imageName", None, -1))
        self.newName_label.setText(QtWidgets.QApplication.translate("main_widget", ".####.exr", None, -1))
        self.outputBasename_CB.setText(QtWidgets.QApplication.translate("main_widget", "output basename", None, -1))
        self.output_dir_CB.setText(QtWidgets.QApplication.translate("main_widget", "output directory", None, -1))
        self.outDirBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.outDirOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "open", None, -1))
        self.filterVariance_CB.setText(QtWidgets.QApplication.translate("main_widget", "filter variance", None, -1))
        self.crossFrame_CB.setText(QtWidgets.QApplication.translate("main_widget", "cross-frame", None, -1))
        self.skipFirst_CB.setText(QtWidgets.QApplication.translate("main_widget", "skip first", None, -1))
        self.skipLast_CB.setText(QtWidgets.QApplication.translate("main_widget", "skip last", None, -1))
        self.filterLayersIndependently_CB.setText(QtWidgets.QApplication.translate("main_widget", "filterLayersIndependently", None, -1))
        self.layer_CB.setText(QtWidgets.QApplication.translate("main_widget", "layer", None, -1))
        self.motionVector_CB.setText(QtWidgets.QApplication.translate("main_widget", "motion vector", None, -1))
        self.configFile_CB.setText(QtWidgets.QApplication.translate("main_widget", "config files", None, -1))
        self.json_window_PB.setText(QtWidgets.QApplication.translate("main_widget", "show json", None, -1))
        self.nOfThreads_CB.setText(QtWidgets.QApplication.translate("main_widget", "n of threads", None, -1))
        self.GPU_CB.setText(QtWidgets.QApplication.translate("main_widget", "GPU", None, -1))
        self.deadlineSet_CB.setText(QtWidgets.QApplication.translate("main_widget", "Deadline Set", None, -1))
        self.mergeExr_CB.setText(QtWidgets.QApplication.translate("main_widget", "Merge exr", None, -1))
        self.jobName_label.setText(QtWidgets.QApplication.translate("main_widget", "Job Name", None, -1))
        self.rebuildBat_PB.setText(QtWidgets.QApplication.translate("main_widget", "rebuild bat", None, -1))
        self.exportBat_PB.setText(QtWidgets.QApplication.translate("main_widget", "export bat", None, -1))

