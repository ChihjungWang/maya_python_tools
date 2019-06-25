# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/redShiftTools_objSet_objectId.ui'
#
# Created: Tue Jan 23 17:42:32 2018
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
        self.general_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.general_label.setFont(font)
        self.general_label.setAlignment(QtCore.Qt.AlignCenter)
        self.general_label.setObjectName("general_label")
        self.verticalLayout.addWidget(self.general_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.objectId_enable_CB = QtWidgets.QCheckBox(main_widget)
        self.objectId_enable_CB.setObjectName("objectId_enable_CB")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.objectId_enable_CB)
        self.objectId_label = QtWidgets.QLabel(main_widget)
        self.objectId_label.setMinimumSize(QtCore.QSize(150, 0))
        self.objectId_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.objectId_label.setObjectName("objectId_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.objectId_label)
        self.objectId_layout = QtWidgets.QHBoxLayout()
        self.objectId_layout.setObjectName("objectId_layout")
        self.objectId_LE = QtWidgets.QLineEdit(main_widget)
        self.objectId_LE.setMaximumSize(QtCore.QSize(80, 16777215))
        self.objectId_LE.setObjectName("objectId_LE")
        self.objectId_layout.addWidget(self.objectId_LE)
        self.objectId_slider = QtWidgets.QSlider(main_widget)
        self.objectId_slider.setMaximum(100)
        self.objectId_slider.setOrientation(QtCore.Qt.Horizontal)
        self.objectId_slider.setObjectName("objectId_slider")
        self.objectId_layout.addWidget(self.objectId_slider)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.objectId_layout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.general_label.setText(QtWidgets.QApplication.translate("main_widget", "General", None, -1))
        self.objectId_enable_CB.setText(QtWidgets.QApplication.translate("main_widget", "Enable", None, -1))
        self.objectId_label.setText(QtWidgets.QApplication.translate("main_widget", "Object ID", None, -1))

