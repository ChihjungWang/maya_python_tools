# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/shadingToolsCreateNodes.ui'
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
        self.verticalLayout.setObjectName("verticalLayout")
        self.texturePath_layout = QtWidgets.QHBoxLayout()
        self.texturePath_layout.setSpacing(4)
        self.texturePath_layout.setContentsMargins(2, 2, 2, 2)
        self.texturePath_layout.setObjectName("texturePath_layout")
        self.texturePath_label = QtWidgets.QLabel(main_widget)
        self.texturePath_label.setObjectName("texturePath_label")
        self.texturePath_layout.addWidget(self.texturePath_label)
        self.texturePath_LE = QtWidgets.QLineEdit(main_widget)
        self.texturePath_LE.setObjectName("texturePath_LE")
        self.texturePath_layout.addWidget(self.texturePath_LE)
        self.texturePathBro_PB = QtWidgets.QPushButton(main_widget)
        self.texturePathBro_PB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.texturePathBro_PB.setObjectName("texturePathBro_PB")
        self.texturePath_layout.addWidget(self.texturePathBro_PB)
        self.texturePathOpen_PB = QtWidgets.QPushButton(main_widget)
        self.texturePathOpen_PB.setObjectName("texturePathOpen_PB")
        self.texturePath_layout.addWidget(self.texturePathOpen_PB)
        self.verticalLayout.addLayout(self.texturePath_layout)
        self.analyzeTextureSets_PB = QtWidgets.QPushButton(main_widget)
        self.analyzeTextureSets_PB.setObjectName("analyzeTextureSets_PB")
        self.verticalLayout.addWidget(self.analyzeTextureSets_PB)
        self.scrollArea = QtWidgets.QScrollArea(main_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 467))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setSpacing(4)
        self.scrollAreaLayout.setContentsMargins(2, 2, 2, 2)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.bottom_label = QtWidgets.QLabel(main_widget)
        self.bottom_label.setObjectName("bottom_label")
        self.verticalLayout.addWidget(self.bottom_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prman_PB = QtWidgets.QPushButton(main_widget)
        self.prman_PB.setObjectName("prman_PB")
        self.horizontalLayout_2.addWidget(self.prman_PB)
        self.stingray_PB = QtWidgets.QPushButton(main_widget)
        self.stingray_PB.setObjectName("stingray_PB")
        self.horizontalLayout_2.addWidget(self.stingray_PB)
        self.redShift_PB = QtWidgets.QPushButton(main_widget)
        self.redShift_PB.setObjectName("redShift_PB")
        self.horizontalLayout_2.addWidget(self.redShift_PB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.texturePath_label.setText(QtWidgets.QApplication.translate("main_widget", "SP textures path :", None, -1))
        self.texturePathBro_PB.setText(QtWidgets.QApplication.translate("main_widget", "...", None, -1))
        self.texturePathOpen_PB.setText(QtWidgets.QApplication.translate("main_widget", "open", None, -1))
        self.analyzeTextureSets_PB.setText(QtWidgets.QApplication.translate("main_widget", "analyze texture sets", None, -1))
        self.bottom_label.setText(QtWidgets.QApplication.translate("main_widget", "creating shader graphs", None, -1))
        self.prman_PB.setText(QtWidgets.QApplication.translate("main_widget", "renderman", None, -1))
        self.stingray_PB.setText(QtWidgets.QApplication.translate("main_widget", "stingray", None, -1))
        self.redShift_PB.setText(QtWidgets.QApplication.translate("main_widget", "redShift", None, -1))

