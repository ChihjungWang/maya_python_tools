# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/prmanToolsTexureEdit.ui'
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
        self.anlyse_PB = QtWidgets.QPushButton(main_widget)
        self.anlyse_PB.setObjectName("anlyse_PB")
        self.verticalLayout.addWidget(self.anlyse_PB)
        self.top_text_label = QtWidgets.QLabel(main_widget)
        self.top_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_text_label.setObjectName("top_text_label")
        self.verticalLayout.addWidget(self.top_text_label)
        self.texture_info_treeWidget = QtWidgets.QTreeWidget(main_widget)
        self.texture_info_treeWidget.setObjectName("texture_info_treeWidget")
        self.verticalLayout.addWidget(self.texture_info_treeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.expanded_all_PB = QtWidgets.QPushButton(main_widget)
        self.expanded_all_PB.setObjectName("expanded_all_PB")
        self.horizontalLayout.addWidget(self.expanded_all_PB)
        self.expanded_off_PB = QtWidgets.QPushButton(main_widget)
        self.expanded_off_PB.setObjectName("expanded_off_PB")
        self.horizontalLayout.addWidget(self.expanded_off_PB)
        self.select_all_PB = QtWidgets.QPushButton(main_widget)
        self.select_all_PB.setObjectName("select_all_PB")
        self.horizontalLayout.addWidget(self.select_all_PB)
        self.select_clean_PB = QtWidgets.QPushButton(main_widget)
        self.select_clean_PB.setObjectName("select_clean_PB")
        self.horizontalLayout.addWidget(self.select_clean_PB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.project_layout = QtWidgets.QHBoxLayout()
        self.project_layout.setSpacing(4)
        self.project_layout.setContentsMargins(2, 2, 2, 2)
        self.project_layout.setObjectName("project_layout")
        self.project_label = QtWidgets.QLabel(main_widget)
        self.project_label.setMinimumSize(QtCore.QSize(100, 0))
        self.project_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.project_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName("project_label")
        self.project_layout.addWidget(self.project_label)
        self.project_LE = QtWidgets.QLineEdit(main_widget)
        self.project_LE.setReadOnly(True)
        self.project_LE.setObjectName("project_LE")
        self.project_layout.addWidget(self.project_LE)
        self.verticalLayout.addLayout(self.project_layout)
        self.subsitute_label = QtWidgets.QLabel(main_widget)
        self.subsitute_label.setObjectName("subsitute_label")
        self.verticalLayout.addWidget(self.subsitute_label)
        self.substitute_layout = QtWidgets.QGridLayout()
        self.substitute_layout.setContentsMargins(2, 2, 2, 2)
        self.substitute_layout.setSpacing(4)
        self.substitute_layout.setObjectName("substitute_layout")
        self.old_root_label = QtWidgets.QLabel(main_widget)
        self.old_root_label.setMinimumSize(QtCore.QSize(100, 0))
        self.old_root_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.old_root_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.old_root_label.setObjectName("old_root_label")
        self.substitute_layout.addWidget(self.old_root_label, 0, 0, 1, 1)
        self.new_root_label = QtWidgets.QLabel(main_widget)
        self.new_root_label.setMinimumSize(QtCore.QSize(100, 0))
        self.new_root_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.new_root_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_root_label.setObjectName("new_root_label")
        self.substitute_layout.addWidget(self.new_root_label, 1, 0, 1, 1)
        self.old_root_LE = QtWidgets.QLineEdit(main_widget)
        self.old_root_LE.setObjectName("old_root_LE")
        self.substitute_layout.addWidget(self.old_root_LE, 0, 1, 1, 1)
        self.new_root_LE = QtWidgets.QLineEdit(main_widget)
        self.new_root_LE.setObjectName("new_root_LE")
        self.substitute_layout.addWidget(self.new_root_LE, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.substitute_layout)
        self.substitute_PB = QtWidgets.QPushButton(main_widget)
        self.substitute_PB.setObjectName("substitute_PB")
        self.verticalLayout.addWidget(self.substitute_PB)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.anlyse_PB.setText(QtWidgets.QApplication.translate("main_widget", "analyse scence file textures", None, -1))
        self.top_text_label.setText(QtWidgets.QApplication.translate("main_widget", "select file you want to manager.<Multi-Selectable>", None, -1))
        self.texture_info_treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("main_widget", "path", None, -1))
        self.texture_info_treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("main_widget", "imgName", None, -1))
        self.texture_info_treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("main_widget", "multipleUV", None, -1))
        self.texture_info_treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("main_widget", "nodeType", None, -1))
        self.expanded_all_PB.setText(QtWidgets.QApplication.translate("main_widget", "expanded all", None, -1))
        self.expanded_off_PB.setText(QtWidgets.QApplication.translate("main_widget", "expanded off", None, -1))
        self.select_all_PB.setText(QtWidgets.QApplication.translate("main_widget", "select all", None, -1))
        self.select_clean_PB.setText(QtWidgets.QApplication.translate("main_widget", "select clean", None, -1))
        self.project_label.setText(QtWidgets.QApplication.translate("main_widget", "current project : ", None, -1))
        self.subsitute_label.setText(QtWidgets.QApplication.translate("main_widget", "substitute path root", None, -1))
        self.old_root_label.setText(QtWidgets.QApplication.translate("main_widget", "old root : ", None, -1))
        self.new_root_label.setText(QtWidgets.QApplication.translate("main_widget", "new root : ", None, -1))
        self.substitute_PB.setText(QtWidgets.QApplication.translate("main_widget", "substitute", None, -1))

