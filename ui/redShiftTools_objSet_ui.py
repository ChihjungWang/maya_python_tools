# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/redShiftTools_objSet.ui'
#
# Created: Tue Jan 23 17:42:31 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setSpacing(2)
        self.top_layout.setContentsMargins(2, 2, 2, 2)
        self.top_layout.setObjectName("top_layout")
        self.createObj_label = QtWidgets.QLabel(main_widget)
        self.createObj_label.setObjectName("createObj_label")
        self.top_layout.addWidget(self.createObj_label)
        self.objectID_PB = QtWidgets.QPushButton(main_widget)
        self.objectID_PB.setObjectName("objectID_PB")
        self.top_layout.addWidget(self.objectID_PB)
        self.visibility_PB = QtWidgets.QPushButton(main_widget)
        self.visibility_PB.setObjectName("visibility_PB")
        self.top_layout.addWidget(self.visibility_PB)
        self.meshParameters_PB = QtWidgets.QPushButton(main_widget)
        self.meshParameters_PB.setObjectName("meshParameters_PB")
        self.top_layout.addWidget(self.meshParameters_PB)
        self.matte_PB = QtWidgets.QPushButton(main_widget)
        self.matte_PB.setObjectName("matte_PB")
        self.top_layout.addWidget(self.matte_PB)
        self.verticalLayout.addLayout(self.top_layout)
        self.line = QtWidgets.QFrame(main_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.obj_sets_gridLayout = QtWidgets.QGridLayout()
        self.obj_sets_gridLayout.setObjectName("obj_sets_gridLayout")
        self.objSets_label = QtWidgets.QLabel(main_widget)
        self.objSets_label.setObjectName("objSets_label")
        self.obj_sets_gridLayout.addWidget(self.objSets_label, 0, 0, 1, 1)
        self.attr_label = QtWidgets.QLabel(main_widget)
        self.attr_label.setObjectName("attr_label")
        self.obj_sets_gridLayout.addWidget(self.attr_label, 0, 1, 1, 1)
        self.attr_scrollArea = QtWidgets.QScrollArea(main_widget)
        self.attr_scrollArea.setWidgetResizable(True)
        self.attr_scrollArea.setObjectName("attr_scrollArea")
        self.attr_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.attr_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 572, 487))
        self.attr_scrollAreaWidgetContents.setObjectName("attr_scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.attr_scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.attr_scrollArea.setWidget(self.attr_scrollAreaWidgetContents)
        self.obj_sets_gridLayout.addWidget(self.attr_scrollArea, 1, 1, 1, 1)
        self.objSets_listWidget = QtWidgets.QListWidget(main_widget)
        self.objSets_listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.objSets_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.objSets_listWidget.setSpacing(0)
        self.objSets_listWidget.setModelColumn(0)
        self.objSets_listWidget.setObjectName("objSets_listWidget")
        self.obj_sets_gridLayout.addWidget(self.objSets_listWidget, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.obj_sets_gridLayout)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setSpacing(2)
        self.bottom_layout.setObjectName("bottom_layout")
        self.attach_PB = QtWidgets.QPushButton(main_widget)
        self.attach_PB.setObjectName("attach_PB")
        self.bottom_layout.addWidget(self.attach_PB)
        self.detach_PB = QtWidgets.QPushButton(main_widget)
        self.detach_PB.setObjectName("detach_PB")
        self.bottom_layout.addWidget(self.detach_PB)
        self.select_PB = QtWidgets.QPushButton(main_widget)
        self.select_PB.setObjectName("select_PB")
        self.bottom_layout.addWidget(self.select_PB)
        self.del_PB = QtWidgets.QPushButton(main_widget)
        self.del_PB.setObjectName("del_PB")
        self.bottom_layout.addWidget(self.del_PB)
        self.verticalLayout.addLayout(self.bottom_layout)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.createObj_label.setText(QtWidgets.QApplication.translate("main_widget", "create object properties : ", None, -1))
        self.objectID_PB.setText(QtWidgets.QApplication.translate("main_widget", "object ID", None, -1))
        self.visibility_PB.setText(QtWidgets.QApplication.translate("main_widget", "visibility", None, -1))
        self.meshParameters_PB.setText(QtWidgets.QApplication.translate("main_widget", "mesh parameters", None, -1))
        self.matte_PB.setText(QtWidgets.QApplication.translate("main_widget", "matte parameters", None, -1))
        self.objSets_label.setText(QtWidgets.QApplication.translate("main_widget", "obj properties", None, -1))
        self.attr_label.setText(QtWidgets.QApplication.translate("main_widget", "attribute", None, -1))
        self.attach_PB.setText(QtWidgets.QApplication.translate("main_widget", "attach", None, -1))
        self.detach_PB.setText(QtWidgets.QApplication.translate("main_widget", "detach", None, -1))
        self.select_PB.setText(QtWidgets.QApplication.translate("main_widget", "select", None, -1))
        self.del_PB.setText(QtWidgets.QApplication.translate("main_widget", "delete", None, -1))

