# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/chihjung/Documents/maya/2017/scripts/ui/redShiftTools_objSet_visbility.ui'
#
# Created: Tue Jan 23 17:42:32 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(500, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.global_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.global_label.setFont(font)
        self.global_label.setAlignment(QtCore.Qt.AlignCenter)
        self.global_label.setObjectName("global_label")
        self.verticalLayout.addWidget(self.global_label)
        self.global_layout = QtWidgets.QFormLayout()
        self.global_layout.setObjectName("global_layout")
        self.empty_label = QtWidgets.QLabel(main_widget)
        self.empty_label.setMinimumSize(QtCore.QSize(150, 0))
        self.empty_label.setText("")
        self.empty_label.setObjectName("empty_label")
        self.global_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.empty_label)
        self.globalEnable_CB = QtWidgets.QCheckBox(main_widget)
        self.globalEnable_CB.setObjectName("globalEnable_CB")
        self.global_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.globalEnable_CB)
        self.verticalLayout.addLayout(self.global_layout)
        self.frame_2 = QtWidgets.QFrame(main_widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.general_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.general_label.setFont(font)
        self.general_label.setAlignment(QtCore.Qt.AlignCenter)
        self.general_label.setObjectName("general_label")
        self.verticalLayout.addWidget(self.general_label)
        self.general_layout = QtWidgets.QFormLayout()
        self.general_layout.setObjectName("general_layout")
        self.empty_label_2 = QtWidgets.QLabel(main_widget)
        self.empty_label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.empty_label_2.setText("")
        self.empty_label_2.setObjectName("empty_label_2")
        self.general_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.empty_label_2)
        self.primaryRayVis_CB = QtWidgets.QCheckBox(main_widget)
        self.primaryRayVis_CB.setObjectName("primaryRayVis_CB")
        self.general_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.primaryRayVis_CB)
        self.seconderayRayVis_CB = QtWidgets.QCheckBox(main_widget)
        self.seconderayRayVis_CB.setObjectName("seconderayRayVis_CB")
        self.general_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seconderayRayVis_CB)
        self.castShadow_CB = QtWidgets.QCheckBox(main_widget)
        self.castShadow_CB.setObjectName("castShadow_CB")
        self.general_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.castShadow_CB)
        self.receivesShadow_CB = QtWidgets.QCheckBox(main_widget)
        self.receivesShadow_CB.setObjectName("receivesShadow_CB")
        self.general_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.receivesShadow_CB)
        self.selfShadow_CB = QtWidgets.QCheckBox(main_widget)
        self.selfShadow_CB.setObjectName("selfShadow_CB")
        self.general_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.selfShadow_CB)
        self.castAo_CB = QtWidgets.QCheckBox(main_widget)
        self.castAo_CB.setObjectName("castAo_CB")
        self.general_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.castAo_CB)
        self.verticalLayout.addLayout(self.general_layout)
        self.frame = QtWidgets.QFrame(main_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.refl_and_refr_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.refl_and_refr_label.setFont(font)
        self.refl_and_refr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.refl_and_refr_label.setObjectName("refl_and_refr_label")
        self.verticalLayout.addWidget(self.refl_and_refr_label)
        self.refl_and_refr_layout = QtWidgets.QFormLayout()
        self.refl_and_refr_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.refl_and_refr_layout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.refl_and_refr_layout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.refl_and_refr_layout.setSpacing(4)
        self.refl_and_refr_layout.setObjectName("refl_and_refr_layout")
        self.visInRefl_CB = QtWidgets.QCheckBox(main_widget)
        self.visInRefl_CB.setObjectName("visInRefl_CB")
        self.refl_and_refr_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.visInRefl_CB)
        self.visInRefr_CB = QtWidgets.QCheckBox(main_widget)
        self.visInRefr_CB.setObjectName("visInRefr_CB")
        self.refl_and_refr_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.visInRefr_CB)
        self.castsRefl_CB = QtWidgets.QCheckBox(main_widget)
        self.castsRefl_CB.setObjectName("castsRefl_CB")
        self.refl_and_refr_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.castsRefl_CB)
        self.castsRefr_CB = QtWidgets.QCheckBox(main_widget)
        self.castsRefr_CB.setObjectName("castsRefr_CB")
        self.refl_and_refr_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.castsRefr_CB)
        self.empty_label_3 = QtWidgets.QLabel(main_widget)
        self.empty_label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.empty_label_3.setText("")
        self.empty_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.empty_label_3.setObjectName("empty_label_3")
        self.refl_and_refr_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.empty_label_3)
        self.verticalLayout.addLayout(self.refl_and_refr_layout)
        self.frame_3 = QtWidgets.QFrame(main_widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.gi_label = QtWidgets.QLabel(main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.gi_label.setFont(font)
        self.gi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gi_label.setObjectName("gi_label")
        self.verticalLayout.addWidget(self.gi_label)
        self.gi_layout = QtWidgets.QFormLayout()
        self.gi_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.gi_layout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.gi_layout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.gi_layout.setSpacing(4)
        self.gi_layout.setObjectName("gi_layout")
        self.empty_label_4 = QtWidgets.QLabel(main_widget)
        self.empty_label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.empty_label_4.setText("")
        self.empty_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.empty_label_4.setObjectName("empty_label_4")
        self.gi_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.empty_label_4)
        self.visToNonPhotonGi_CB = QtWidgets.QCheckBox(main_widget)
        self.visToNonPhotonGi_CB.setObjectName("visToNonPhotonGi_CB")
        self.gi_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.visToNonPhotonGi_CB)
        self.visToGiPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.visToGiPhotons_CB.setObjectName("visToGiPhotons_CB")
        self.gi_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.visToGiPhotons_CB)
        self.visCausticPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.visCausticPhotons_CB.setObjectName("visCausticPhotons_CB")
        self.gi_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.visCausticPhotons_CB)
        self.receivesGi_CB = QtWidgets.QCheckBox(main_widget)
        self.receivesGi_CB.setObjectName("receivesGi_CB")
        self.gi_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.receivesGi_CB)
        self.forceBruteForceGi_CB = QtWidgets.QCheckBox(main_widget)
        self.forceBruteForceGi_CB.setObjectName("forceBruteForceGi_CB")
        self.gi_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.forceBruteForceGi_CB)
        self.castsGiPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.castsGiPhotons_CB.setObjectName("castsGiPhotons_CB")
        self.gi_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.castsGiPhotons_CB)
        self.castsCausticPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.castsCausticPhotons_CB.setObjectName("castsCausticPhotons_CB")
        self.gi_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.castsCausticPhotons_CB)
        self.receivesGiPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.receivesGiPhotons_CB.setObjectName("receivesGiPhotons_CB")
        self.gi_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.receivesGiPhotons_CB)
        self.receivesCausticPhotons_CB = QtWidgets.QCheckBox(main_widget)
        self.receivesCausticPhotons_CB.setObjectName("receivesCausticPhotons_CB")
        self.gi_layout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.receivesCausticPhotons_CB)
        self.verticalLayout.addLayout(self.gi_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QtWidgets.QApplication.translate("main_widget", "Form", None, -1))
        self.global_label.setText(QtWidgets.QApplication.translate("main_widget", "global", None, -1))
        self.globalEnable_CB.setText(QtWidgets.QApplication.translate("main_widget", "Enable", None, -1))
        self.general_label.setText(QtWidgets.QApplication.translate("main_widget", "General", None, -1))
        self.primaryRayVis_CB.setText(QtWidgets.QApplication.translate("main_widget", "Primary Ray Visible", None, -1))
        self.seconderayRayVis_CB.setText(QtWidgets.QApplication.translate("main_widget", "Secondary Ray Visible", None, -1))
        self.castShadow_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts Shadows", None, -1))
        self.receivesShadow_CB.setText(QtWidgets.QApplication.translate("main_widget", "Receives Shadows", None, -1))
        self.selfShadow_CB.setText(QtWidgets.QApplication.translate("main_widget", "Self-Shadows", None, -1))
        self.castAo_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts AO", None, -1))
        self.refl_and_refr_label.setText(QtWidgets.QApplication.translate("main_widget", "Reflection & Refraction", None, -1))
        self.visInRefl_CB.setText(QtWidgets.QApplication.translate("main_widget", "Visible in Reflections", None, -1))
        self.visInRefr_CB.setText(QtWidgets.QApplication.translate("main_widget", "Visible in Refractions", None, -1))
        self.castsRefl_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts Reflections", None, -1))
        self.castsRefr_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts Refractions", None, -1))
        self.gi_label.setText(QtWidgets.QApplication.translate("main_widget", "Global illumination", None, -1))
        self.visToNonPhotonGi_CB.setText(QtWidgets.QApplication.translate("main_widget", "Visible to Non-Photon GI", None, -1))
        self.visToGiPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Visible to GI Photons", None, -1))
        self.visCausticPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Visible to Caustic Photons", None, -1))
        self.receivesGi_CB.setText(QtWidgets.QApplication.translate("main_widget", "Receives GI", None, -1))
        self.forceBruteForceGi_CB.setText(QtWidgets.QApplication.translate("main_widget", "Force Brute-Force GI", None, -1))
        self.castsGiPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts GI Photons", None, -1))
        self.castsCausticPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Casts Caustic Photons", None, -1))
        self.receivesGiPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Receives GI Photons", None, -1))
        self.receivesCausticPhotons_CB.setText(QtWidgets.QApplication.translate("main_widget", "Receives Caustic Photons", None, -1))
