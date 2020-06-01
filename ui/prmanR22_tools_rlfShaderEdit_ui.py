# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2020/scripts/ui/prmanR22_tools_rlfShaderEdit.ui',
# licensing of 'C:/Users/chihjung/Documents/maya/2020/scripts/ui/prmanR22_tools_rlfShaderEdit.ui' applies.
#
# Created: Wed May 27 11:27:58 2020
#      by: pyside2-uic  running on PySide2 5.12.5
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
        self.texture_info_treeWidget.setIndentation(20)
        self.texture_info_treeWidget.setColumnCount(3)
        self.texture_info_treeWidget.setObjectName("texture_info_treeWidget")
        self.texture_info_treeWidget.headerItem().setText(0, "Object")
        self.texture_info_treeWidget.headerItem().setText(1, "Shading Group")
        self.texture_info_treeWidget.header().setVisible(True)
        self.texture_info_treeWidget.header().setCascadingSectionResizes(False)
        self.texture_info_treeWidget.header().setDefaultSectionSize(260)
        self.texture_info_treeWidget.header().setHighlightSections(False)
        self.texture_info_treeWidget.header().setMinimumSectionSize(50)
        self.texture_info_treeWidget.header().setSortIndicatorShown(False)
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
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.anlyse_PB.setText(QtWidgets.QApplication.translate("main_widget", "analyse mesh with shader", None, -1))
        self.top_text_label.setText(QtWidgets.QApplication.translate("main_widget", "select file you want to rename (ex. map01_*, map02_*, ...)", None, -1))
        self.texture_info_treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("main_widget", "Path Expression", None, -1))
        self.expanded_all_PB.setText(QtWidgets.QApplication.translate("main_widget", "expanded all", None, -1))
        self.expanded_off_PB.setText(QtWidgets.QApplication.translate("main_widget", "expanded off", None, -1))

