# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/prmanToolsShaderRename.ui'
#
# Created: Thu Nov 30 09:25:29 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shadeNode_layout = QtWidgets.QHBoxLayout()
        self.shadeNode_layout.setSpacing(4)
        self.shadeNode_layout.setContentsMargins(2, 2, 2, 2)
        self.shadeNode_layout.setObjectName("shadeNode_layout")
        self.shadeNode_PB = QtWidgets.QPushButton(main_widget)
        self.shadeNode_PB.setObjectName("shadeNode_PB")
        self.shadeNode_layout.addWidget(self.shadeNode_PB)
        self.shadeNode_label = QtWidgets.QLabel(main_widget)
        self.shadeNode_label.setObjectName("shadeNode_label")
        self.shadeNode_layout.addWidget(self.shadeNode_label)
        self.renema_LE = QtWidgets.QLineEdit(main_widget)
        self.renema_LE.setObjectName("renema_LE")
        self.shadeNode_layout.addWidget(self.renema_LE)
        self.shadeNodePreview_PB = QtWidgets.QPushButton(main_widget)
        self.shadeNodePreview_PB.setObjectName("shadeNodePreview_PB")
        self.shadeNode_layout.addWidget(self.shadeNodePreview_PB)
        self.verticalLayout.addLayout(self.shadeNode_layout)
        self.shaderNodesList_scrollArea = QtWidgets.QScrollArea(main_widget)
        self.shaderNodesList_scrollArea.setWidgetResizable(True)
        self.shaderNodesList_scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.shaderNodesList_scrollArea.setObjectName("shaderNodesList_scrollArea")
        self.shaderNodesList_widget = QtWidgets.QWidget()
        self.shaderNodesList_widget.setGeometry(QtCore.QRect(0, 0, 790, 532))
        self.shaderNodesList_widget.setObjectName("shaderNodesList_widget")
        self.shaderNodesList_layout = QtWidgets.QVBoxLayout(self.shaderNodesList_widget)
        self.shaderNodesList_layout.setSpacing(4)
        self.shaderNodesList_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.shaderNodesList_layout.setContentsMargins(2, 2, 2, 2)
        self.shaderNodesList_layout.setObjectName("shaderNodesList_layout")
        self.shaderNodesList_scrollArea.setWidget(self.shaderNodesList_widget)
        self.verticalLayout.addWidget(self.shaderNodesList_scrollArea)
        self.run_rename_PB = QtWidgets.QPushButton(main_widget)
        self.run_rename_PB.setObjectName("run_rename_PB")
        self.verticalLayout.addWidget(self.run_rename_PB)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.shadeNode_PB.setText(QtWidgets.QApplication.translate("main_widget", "get the selected nodes", None, -1))
        self.shadeNode_label.setText(QtWidgets.QApplication.translate("main_widget", "rename to >>", None, -1))
        self.shadeNodePreview_PB.setText(QtWidgets.QApplication.translate("main_widget", "preview", None, -1))
        self.run_rename_PB.setText(QtWidgets.QApplication.translate("main_widget", "run rename", None, -1))

