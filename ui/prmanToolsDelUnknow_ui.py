# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2018/scripts/ui/prmanToolsDelUnknow.ui'
#
# Created: Tue Jun 11 13:36:50 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(800, 516)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.analyseUnknowNodes_PB = QtWidgets.QPushButton(main_widget)
        self.analyseUnknowNodes_PB.setObjectName("analyseUnknowNodes_PB")
        self.horizontalLayout.addWidget(self.analyseUnknowNodes_PB)
        self.analyseUnknowPlugins_PB = QtWidgets.QPushButton(main_widget)
        self.analyseUnknowPlugins_PB.setObjectName("analyseUnknowPlugins_PB")
        self.horizontalLayout.addWidget(self.analyseUnknowPlugins_PB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.infoBar_label = QtWidgets.QLabel(main_widget)
        self.infoBar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.infoBar_label.setObjectName("infoBar_label")
        self.verticalLayout.addWidget(self.infoBar_label)
        self.nodeCheck_scrollArea = QtWidgets.QScrollArea(main_widget)
        self.nodeCheck_scrollArea.setWidgetResizable(True)
        self.nodeCheck_scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nodeCheck_scrollArea.setObjectName("nodeCheck_scrollArea")
        self.nodeCheck_widget = QtWidgets.QWidget()
        self.nodeCheck_widget.setGeometry(QtCore.QRect(0, 0, 790, 430))
        self.nodeCheck_widget.setObjectName("nodeCheck_widget")
        self.nodeCheck_layout = QtWidgets.QVBoxLayout(self.nodeCheck_widget)
        self.nodeCheck_layout.setSpacing(4)
        self.nodeCheck_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.nodeCheck_layout.setContentsMargins(2, 2, 2, 2)
        self.nodeCheck_layout.setObjectName("nodeCheck_layout")
        self.nodeCheck_scrollArea.setWidget(self.nodeCheck_widget)
        self.verticalLayout.addWidget(self.nodeCheck_scrollArea)
        self.PB_layout = QtWidgets.QHBoxLayout()
        self.PB_layout.setSpacing(4)
        self.PB_layout.setContentsMargins(2, 2, 2, 2)
        self.PB_layout.setObjectName("PB_layout")
        self.setAllOn_PB = QtWidgets.QPushButton(main_widget)
        self.setAllOn_PB.setObjectName("setAllOn_PB")
        self.PB_layout.addWidget(self.setAllOn_PB)
        self.setAllOff_PB = QtWidgets.QPushButton(main_widget)
        self.setAllOff_PB.setObjectName("setAllOff_PB")
        self.PB_layout.addWidget(self.setAllOff_PB)
        self.selectNode_PB = QtWidgets.QPushButton(main_widget)
        self.selectNode_PB.setObjectName("selectNode_PB")
        self.PB_layout.addWidget(self.selectNode_PB)
        self.deleteNode_PB = QtWidgets.QPushButton(main_widget)
        self.deleteNode_PB.setObjectName("deleteNode_PB")
        self.PB_layout.addWidget(self.deleteNode_PB)
        self.verticalLayout.addLayout(self.PB_layout)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.analyseUnknowNodes_PB.setText(QtWidgets.QApplication.translate("main_widget", "analyse scene unknowNodes", None, -1))
        self.analyseUnknowPlugins_PB.setText(QtWidgets.QApplication.translate("main_widget", "analyse scene unknowPlugins", None, -1))
        self.infoBar_label.setText(QtWidgets.QApplication.translate("main_widget", "select the node you want to delete.<multi-selectable>", None, -1))
        self.setAllOn_PB.setText(QtWidgets.QApplication.translate("main_widget", "set all on", None, -1))
        self.setAllOff_PB.setText(QtWidgets.QApplication.translate("main_widget", "set all off", None, -1))
        self.selectNode_PB.setText(QtWidgets.QApplication.translate("main_widget", "select node", None, -1))
        self.deleteNode_PB.setText(QtWidgets.QApplication.translate("main_widget", "delete node", None, -1))

