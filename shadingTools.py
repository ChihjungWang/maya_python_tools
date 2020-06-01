# -*- coding: utf-8 -*-
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import maya.cmds as cmds
import pymel.core as pm
import os
import getpass
import subprocess
import inspect
import json
import csv
import time
import sys
maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/' + username + '/Documents/maya/' + maya_version + '/scripts/ui'
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
import shadingToolsCreateNodes_ui
reload(shadingToolsCreateNodes_ui)
import shadingToolsMeshLink_ui
reload(shadingToolsMeshLink_ui)


dialog = None

# ---------------------------------------------------------------------------------------------------#


class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('shading tools' + ' v0.5' + u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800, 600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0, 0, 0, 0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.shadingToolsCreateNodes_wid = shadingToolsCreateNodes_ui()
        self.shadingToolsMeshLink_wid = shadingToolsMeshLink_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.shadingToolsCreateNodes_wid, "createNode")
        main_tab_Widget.addTab(self.shadingToolsMeshLink_wid, "meshLink")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/pixiTools.csv'
        self.python_temp_json = self.python_temp + '/pixiTools.json'
        self.save_UI_list = [
            self.shadingToolsCreateNodes_wid.texturePath_LE,
            self.shadingToolsCreateNodes_wid.dot_CB,
            self.shadingToolsCreateNodes_wid.udim_CB,
            self.shadingToolsCreateNodes_wid.ext_CB,
            self.shadingToolsMeshLink_wid.cachePath_LE,
            self.shadingToolsMeshLink_wid.objName_LE,
            self.shadingToolsMeshLink_wid.nameSpace_LE
        ]
        self.layout().addWidget(main_tab_Widget)
        self.setFromJson()

    def closeEvent(self, event):
        self.writeJson()

    def writeJson(self):
        if os.path.exists(self.python_temp) is False:
            os.mkdir(self.python_temp)
        data_dict = {}
        for index, obj in enumerate(self.save_UI_list):
            wid_index = "wid_" + str(index)
            data_dict[wid_index] = {}
            data_dict[wid_index]['value'] = self.getValue(obj)
            data_dict[wid_index]['name'] = obj.objectName()
            data_dict[wid_index]['type'] = str(type(obj))
        file2 = open(self.python_temp_json, 'w')
        json.dump(data_dict, file2, ensure_ascii=True, indent=4)
        file2.close()

    def setFromJson(self):
        if os.path.exists(self.python_temp_json):
            file = open(self.python_temp_json, "r")
            json_dict = json.load(file)
            file.close()
            for index, widget in enumerate(self.save_UI_list):
                key = 'wid_' + str(index)
                if key in json_dict:
                    value = json_dict[key]['value']
                    try:
                        self.setValue(widget, value)
                    except:
                        pass

    def setValue(self, widget, value):
        wid_type = type(widget)
        if wid_type == QtWidgets.QLineEdit:
            widget.setText(value)
        elif wid_type == QtWidgets.QRadioButton:
            widget.setChecked(value)
        elif wid_type == QtWidgets.QCheckBox:
            widget.setChecked(value)
        elif wid_type == QtWidgets.QButtonGroup:
            button = widget.button(value)
            button.setChecked(True)
        elif wid_type == QtWidgets.QComboBox:
            widget.setCurrentIndex(value)

    def getValue(self, widget):
        widget_type = type(widget)
        if widget_type == QtWidgets.QLineEdit:
            return widget.text()
        elif widget_type == QtWidgets.QRadioButton:
            return widget.isChecked()
        elif widget_type == QtWidgets.QCheckBox:
            return widget.isChecked()
        elif widget_type == QtWidgets.QButtonGroup:
            return widget.checkedId()
        elif widget_type == QtWidgets.QComboBox:
            return widget.currentIndex()


class shadingToolsCreateNodes_ui(QtWidgets.QWidget, shadingToolsCreateNodes_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(shadingToolsCreateNodes_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        self.rman_folder = os.getenv('RMANTREE')
        self.pbr_name_list = ['BaseColor', 'Metallic', 'Roughness', 'Normal', 'Height', 'Emissive']

    def connectInterface(self):
        self.texturePathBro_PB.clicked.connect(self.texturePathBro_PB_hit)
        self.texturePathOpen_PB.clicked.connect(self.texturePathOpen_PB_hit)
        self.analyzeTextureSets_PB.clicked.connect(self.analyzeTextureSets_PB_hit)
        self.prman_PB.clicked.connect(self.prman_PB_hit)
        self.stingray_PB.clicked.connect(self.stingray_PB_hit)
        self.redShift_PB.clicked.connect(self.redShift_PB_hit)
        self.dot_CB.currentIndexChanged.connect(self.checkBaseName)
        self.udim_CB.stateChanged.connect(self.checkBaseName)
        self.ext_CB.currentIndexChanged.connect(self.checkBaseName)

    def texturePathBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.texturePath_LE.setText(path)

    def texturePathOpen_PB_hit(self):
        texture_path = self.texturePath_LE.text()
        texture_file = texture_path.replace('/', '\\')
        os.startfile(texture_file)

    def checkBaseName(self):
        base_name = 'ex. dog_BaseColor'
        ext = self.ext_CB.currentText()
        if self.udim_CB.isChecked():
            dot = self.dot_CB.currentText()
            exText = base_name + dot + '1001' + '.' + ext
        else:
            exText = base_name + '.' + ext
        self.exName_LE.setText(exText)

    def imgList(self, path):
        file_list = os.listdir(path)
        img_list = []
        for i in file_list:
            if os.path.isfile(path + "/" + i):
                if os.path.splitext(i)[1] == "." + self.ext_CB.currentText():
                    img_list.append(i)
        img_list.sort()
        return img_list

    def checkTextureInfo(self):
        texture_path = self.texturePath_LE.text()
        texture_path = texture_path.replace('\\', '/')
        img_list = self.imgList(texture_path)
        textures_sets = []
        ext = self.ext_CB.currentText()
        dot = self.dot_CB.currentText()
        if self.udim_CB.isChecked():
            textures_sets = []
            for img in img_list:
                name = os.path.splitext(img)[0]
                suffix = 'BaseColor'
                check_name = suffix + dot + '1001'
                file_name = name[-len(suffix) - 5:len(name)]
                if file_name.lower() == check_name.lower():
                    baseName = name[0:-len(suffix) - 6]
                    if baseName not in textures_sets:
                        textures_sets.append(baseName)
            texture_info = []
            for texture_name in textures_sets:
                texture_dic = {}
                texture_dic['BaseName'] = texture_name
                texture_dic['UDIM'] = 'yes'
                texture_dic['ext'] = ext
                texture_dic['dot'] = dot
                for suffix in self.pbr_name_list:
                    texture_dic[suffix] = 'no'
                    file_name = texture_name + "_" + suffix + dot + '1001' + '.' + ext
                    if os.path.exists(texture_path + '/' + file_name):
                        texture_dic[suffix] = 'yes'
                texture_info.append(texture_dic)
            return texture_info

        else:
            textures_sets = []
            for img in img_list:
                name = os.path.splitext(img)[0]
                suffix = 'BaseColor'
                if name[-len(suffix):len(name)].lower() == suffix.lower():
                    baseName = name[0:-len(suffix) - 1]
                    if baseName not in textures_sets:
                        textures_sets.append(baseName)
            texture_info = []
            for texture_name in textures_sets:
                texture_dic = {}
                texture_dic['BaseName'] = texture_name
                texture_dic['UDIM'] = 'no'
                texture_dic['ext'] = ext
                texture_dic['dot'] = dot
                for suffix in self.pbr_name_list:
                    texture_dic[suffix] = 'no'
                    file_name = texture_name + "_" + suffix + '.' + ext
                    if os.path.exists(texture_path + '/' + file_name):
                        texture_dic[suffix] = 'yes'
                texture_info.append(texture_dic)
            return texture_info

    def analyzeTextureSets_PB_hit(self):
        self.clearLayout(self.scrollAreaLayout)
        self.texture_info = self.checkTextureInfo()

        set_info_layout = QtWidgets.QGridLayout()
        set_info_layout.setAlignment(QtCore.Qt.AlignLeft)
        set_info_layout.setContentsMargins(0, 0, 0, 0)
        set_list_widget = QtWidgets.QWidget()
        set_list_widget.setLayout(set_info_layout)
        self.scrollAreaLayout.addWidget(set_list_widget)

        self.set_CB_list = []
        texture_set_label = QtWidgets.QLabel('texture Set')
        texture_set_label.setStyleSheet("font: bold;")
        set_info_layout.addWidget(texture_set_label, 0, 0)

        for index, name in enumerate(self.pbr_name_list):
            label = QtWidgets.QLabel(name)
            label.setStyleSheet("font: bold;")
            set_info_layout.addWidget(label, 0, index + 1)

        for index, imgSet in enumerate(self.texture_info):
            basename_CB = checkBox_class(self, imgSet['BaseName'], index)
            set_info_layout.addWidget(basename_CB, index + 1, 0)
            for index2, pbrName in enumerate(self.pbr_name_list):
                label = QtWidgets.QLabel(imgSet[pbrName])
                set_info_layout.addWidget(label, index + 1, index2 + 1)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaLayout.addSpacerItem(self.spacerItem)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

    def prman_PB_hit(self):
        for index in self.set_CB_list:
            disney_shade = pm.shadingNode('PxrDisney', n=self.texture_info[index]['BaseName'] + '_PxrDisney', asShader=True)
            for pbrName in self.pbr_name_list:
                self.creatPrmanNode(
                    disney_shade,
                    self.texture_info[index]['BaseName'],
                    pbrName,
                    self.texture_info[index][pbrName],
                    self.texture_info[index]['UDIM'],
                    self.texture_info[index]['dot'],
                    self.texture_info[index]['ext']
                )

    def creatPrmanNode(self, shader, texSet, pbrName, exist, udim, dot, ext):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Normal' and pbrName != 'Height':
                tex_node = pm.shadingNode('PxrTexture', n=texSet + '_' + pbrName + '_PxrTexture', asTexture=True)
                if udim == 'yes':
                    img_name = texSet + '_' + pbrName
                    img_list = self.udimFileList(texture_path, img_name, dot, ext)
                    for img in img_list:
                        path_img = texture_path + '/' + img
                        self.txmakeCMD(path_img, udim)
                    tex = texture_path + '/' + img_name + dot + '_MAPID_.tex'
                    pm.setAttr(tex_node + '.atlasStyle', 1)
                else:
                    img = texture_path + '/' + texSet + '_' + pbrName + '.' + ext
                    tex = self.txmakeCMD(img, udim)
                pm.setAttr(tex_node + '.filename', tex, type="string")
                if pbrName == 'BaseColor':
                    pm.setAttr(tex_node + '.linearize', 1)
                    pm.connectAttr(tex_node + '.resultRGB', shader + '.baseColor')
                    # pm.connectAttr(tex_node + '.resultA', shader + '.presence')
                elif pbrName == 'Metallic':
                    pm.setAttr(tex_node + '.linearize', 0)
                    pm.connectAttr(tex_node + '.resultR', shader + '.metallic')
                elif pbrName == 'Roughness':
                    pm.setAttr(tex_node + '.linearize', 0)
                    pm.connectAttr(tex_node + '.resultR', shader + '.roughness')
                elif pbrName == 'Emissive':
                    pm.setAttr(tex_node + '.linearize', 0)
                    pm.connectAttr(tex_node + '.resultRGB', shader + '.emitColor')
            elif pbrName == 'Normal':
                tex_node = pm.shadingNode('PxrNormalMap', n=texSet + '_' + pbrName + '_PxrNormalMap', asTexture=True)
                if udim == 'yes':
                    img_name = texSet + '_' + pbrName
                    img_list = self.udimFileList(texture_path, img_name, dot, ext)
                    for img in img_list:
                        path_img = texture_path + '/' + img
                        self.txmakeCMD(path_img, udim)
                    tex = texture_path + '/' + img_name + dot + '_MAPID_.tex'
                    pm.setAttr(tex_node + '.atlasStyle', 1)
                else:
                    img = texture_path + '/' + texSet + '_' + pbrName + '.' + ext
                    tex = self.txmakeCMD(img, udim)
                pm.setAttr(tex_node + '.filename', tex, type="string")
                pm.connectAttr(tex_node + '.resultN', shader + '.bumpNormal')

    def udimFileList(self, texture_path, img_name, dot, ext):
        file_list = os.listdir(texture_path)
        texture_list = []
        for file in file_list:
            if os.path.splitext(file)[1] == "." + ext:
                if file[0:len(img_name)].lower() == img_name.lower():
                    name = os.path.splitext(file)[0]
                    number = name[-4:]
                    if self.is_number(number):
                        texture_list.append(file)
        return texture_list

    def txmakeCMD(self, img, udim):
        img = img.replace('/', '\\')
        tex = os.path.splitext(img)[0] + '.tex'
        if udim == 'no':
            txmakeCMD = "\"" + self.rman_folder + "\\bin\\txmake.exe" + "\"" + " -newer" + " -mode periodic " + " " + img + " " + tex
            subprocess.call(txmakeCMD, shell=True)
        else:
            txmakeCMD = "\"" + self.rman_folder + "\\bin\\txmake.exe" + "\"" + " -newer" + " -mode black" + " " + img + " " + tex
            subprocess.call(txmakeCMD, shell=True)
        return tex

    def stingray_PB_hit(self):
        for index in self.set_CB_list:
            stingray_shade = pm.shadingNode('StingrayPBS', n=self.texture_info[index]['BaseName'] + '_StingrayPBS', asShader=True)
            pm.setAttr(stingray_shade + '.initgraph', True)
            for pbrName in self.pbr_name_list:
                self.creatStingrayNode(
                    stingray_shade,
                    self.texture_info[index]['BaseName'],
                    pbrName,
                    self.texture_info[index][pbrName],
                    self.texture_info[index]['UDIM'],
                    self.texture_info[index]['dot'],
                    self.texture_info[index]['ext']
                )

    def creatStingrayNode(self, shader, texSet, pbrName, exist, udim, dot, ext):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Height':
                tex_node = pm.shadingNode('file', n=texSet + '_' + pbrName + '_file', asTexture=True, isColorManaged=True)
                if udim == 'yes':
                    file = texture_path + '/' + texSet + '_' + pbrName + dot + '1001.' + ext
                    pm.setAttr(tex_node + '.fileTextureName', file, type="string")
                    pm.setAttr(tex_node + '.uvTilingMode', 3)
                else:
                    file = texture_path + '/' + texSet + '_' + pbrName + '.' + ext
                    pm.setAttr(tex_node + '.fileTextureName', file, type="string")
                if pbrName == 'BaseColor':
                    pm.setAttr(shader + '.use_color_map', 1)
                    pm.connectAttr(tex_node + '.outColor', shader + '.TEX_color_map')
                elif pbrName == 'Metallic':
                    pm.setAttr(shader + '.use_metallic_map', 1)
                    pm.connectAttr(tex_node + '.outColor', shader + '.TEX_metallic_map')
                elif pbrName == 'Roughness':
                    pm.setAttr(shader + '.use_roughness_map', 1)
                    pm.connectAttr(tex_node + '.outColor', shader + '.TEX_roughness_map')
                elif pbrName == 'Normal':
                    pm.setAttr(shader + '.use_normal_map', 1)
                    pm.connectAttr(tex_node + '.outColor', shader + '.TEX_normal_map')
                elif pbrName == 'Emissive':
                    pm.setAttr(shader + '.use_emissive_map', 1)
                    pm.connectAttr(tex_node + '.outColor', shader + '.TEX_emissive_map')

    def redShift_PB_hit(self):
        for index in self.set_CB_list:
            redShift_shade = pm.shadingNode('RedshiftMaterial', n=self.texture_info[index]['BaseName'] + '_RedshiftMaterial', asShader=True)
            pm.setAttr(redShift_shade + '.refl_brdf', 1)
            pm.setAttr(redShift_shade + '.refl_fresnel_mode', 2)
            for pbrName in self.pbr_name_list:
                self.creatRedShiftNode(
                    redShift_shade,
                    self.texture_info[index]['BaseName'],
                    pbrName,
                    self.texture_info[index][pbrName],
                    self.texture_info[index]['UDIM'],
                    self.texture_info[index]['dot'],
                    self.texture_info[index]['ext']
                )

    def creatRedShiftNode(self, shader, texSet, pbrName, exist, udim, dot, ext):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Normal' and pbrName != 'Height':
                tex_node = pm.shadingNode('file', n=texSet + '_' + pbrName + '_file', asTexture=True, isColorManaged=True)
                if udim == 'yes':
                    file = texture_path + '/' + texSet + '_' + pbrName + dot + '1001.' + ext
                    pm.setAttr(tex_node + '.fileTextureName', file, type="string")
                    pm.setAttr(tex_node + '.uvTilingMode', 3)
                else:
                    file = texture_path + '/' + texSet + '_' + pbrName + '.' + ext
                    pm.setAttr(tex_node + '.fileTextureName', file, type="string")
                if pbrName == 'BaseColor':
                    pm.setAttr(tex_node + '.colorSpace', 'sRGB', type='string')
                    pm.connectAttr(tex_node + '.outColor', shader + '.diffuse_color')
                elif pbrName == 'Metallic':
                    pm.setAttr(tex_node + '.colorSpace', 'Raw', type='string')
                    pm.connectAttr(tex_node + '.outColorR', shader + '.refl_metalness')
                elif pbrName == 'Roughness':
                    pm.setAttr(tex_node + '.colorSpace', 'Raw', type='string')
                    pm.connectAttr(tex_node + '.outColorR', shader + '.refl_roughness')
                elif pbrName == 'Emissive':
                    pm.setAttr(tex_node + '.colorSpace', 'sRGB', type='string')
                    pm.connectAttr(tex_node + '.outColor', shader + '.emission_color')
            elif pbrName == 'Normal':
                tex_node = pm.shadingNode('RedshiftNormalMap', n=texSet + '_' + pbrName + '_RedshiftNormalMap', asUtility=True)
                if udim == 'yes':
                    file = texture_path + '/' + texSet + '_' + pbrName + dot + '<UDIM>.' + ext
                    pm.setAttr(tex_node + '.tex0', file, type="string")
                else:
                    file = texture_path + '/' + texSet + '_' + pbrName + '.' + ext
                    pm.setAttr(tex_node + '.tex0', file, type="string")
                pm.connectAttr(tex_node + '.outDisplacementVector', shader + '.bump_input')

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False


class checkBox_class(QtWidgets.QCheckBox):
    def __init__(self, parent, name, index):
        QtWidgets.QCheckBox.__init__(self)
        self.parent = parent
        self.name = name
        self.index = index
        self.setText(self.name)
        self.stateChanged.connect(self.checkValue)

    def checkValue(self):
        if self.checkState():
            if self.index not in self.parent.set_CB_list:
                self.parent.set_CB_list.append(self.index)
        if self.checkState() is False:
            if self.index in self.parent.set_CB_list:
                self.parent.set_CB_list.remove(self.index)
        self.parent.set_CB_list.sort()


class shadingToolsMeshLink_ui(QtWidgets.QWidget, shadingToolsMeshLink_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(shadingToolsMeshLink_ui, self).__init__(parent)
        self.setupUi(self)
        self.shading_link_treeWidget.header().resizeSection(0, 500)
        self.export_prman_PB.setEnabled(False)
        self.convert_prman_PB.setEnabled(False)
        self.export_stingray_PB.setEnabled(False)
        self.convert_stingray_PB.setEnabled(False)
        self.export_redShift_PB.setEnabled(False)
        self.convert_redShift_PB.setEnabled(False)
        self.connectInterface()

    def connectInterface(self):
        self.analyzeShadingLink_PB.clicked.connect(self.analyzeShadingLink_PB_hit)
        self.expanded_all_PB.clicked.connect(self.expanded_all_PB_hit)
        self.expanded_off_PB.clicked.connect(self.expanded_off_PB_hit)
        self.select_all_PB.clicked.connect(self.select_all_PB_hit)
        self.select_clean_PB.clicked.connect(self.select_clean_PB_hit)
        self.shading_link_treeWidget.itemChanged.connect(self.treeWidgetItem_changed)
        self.shading_link_treeWidget.itemClicked.connect(self.treeWidgetItem_hit)
        self.cachePath_bro_PB.clicked.connect(self.cachePath_bro_PB_hit)
        self.cachePath_open_PB.clicked.connect(self.cachePath_open_PB_hit)
        self.export_stingray_PB.clicked.connect(self.export_stingray_PB_hit)
        self.export_redShift_PB.clicked.connect(self.export_redShift_PB_hit)
        self.export_prman_PB.clicked.connect(self.export_prman_PB_hit)
        self.convert_stingray_PB.clicked.connect(self.convert_stingray_PB_hit)
        self.convert_redShift_PB.clicked.connect(self.convert_redShift_PB_hit)
        self.convert_prman_PB.clicked.connect(self.convert_prman_PB_hit)

    def getShader(self, meshShape_list):
        default_mat = ['initialParticleSE', 'initialShadingGroup']
        shadingInfo = []
        shadingGrp_list = []
        for meshShape in meshShape_list:
            SG = pm.listConnections(meshShape, type='shadingEngine')
            if len(SG) != 0:
                if SG[0] not in shadingGrp_list:
                    shadingGrp_list.append(SG[0])
        for shadingGrp in shadingGrp_list:
            if shadingGrp not in default_mat:
                shading_dict = {}
                shading_dict['SG'] = shadingGrp
                shading_dict['mesh'] = []
                for meshShape in meshShape_list:
                    SG = pm.listConnections(meshShape, type='shadingEngine')
                    if len(SG) != 0:
                        if SG[0] == shadingGrp:
                            mesh_t = meshShape.getTransform()
                            if mesh_t not in shading_dict['mesh']:
                                shading_dict['mesh'].append(mesh_t)
                shadingInfo.append(shading_dict)
        return shadingInfo

    def getMeshShape(self):
        meshShape_list = []
        seleted_list = pm.ls(sl=True)
        for node in seleted_list:
            node_s_list = pm.listRelatives(node)
            for node_s in node_s_list:
                if node_s.type() == 'mesh':
                    meshShape_list.append(node_s)
        return meshShape_list

    def isGroup(self, node):
        children = pm.listRelatives(node, c=True, f=True)
        if children is None:
            return True
        for c in children:
            if pm.nodeType(c) != 'transform':
                return False
        else:
            return True

    def cachePath_bro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.cachePath_LE.setText(path)

    def cachePath_open_PB_hit(self):
        cache_path = self.cachePath_LE.text()
        cache_file = cache_path.replace('/', '\\')
        os.startfile(cache_file)

    def analyzeShadingLink_PB_hit(self):
        self.deleteTreeItem(self.shading_link_treeWidget)
        meshShape_list = self.getMeshShape()
        self.shaderInfo = self.getShader(meshShape_list)
        self.checked_node = []
        self.top_tree_item = []
        for shaderDict in self.shaderInfo:
            pathTreeItem = pathTreeItem_class(self, shaderDict)
            self.top_tree_item.append(pathTreeItem)
            self.shading_link_treeWidget.addTopLevelItem(pathTreeItem)
        self.checkEngine(self.top_tree_item)
        self.checkJson_file()
        self.export_json_dict = {}

    def export_stingray_PB_hit(self):
        self.exportJsonShader('stingray')
        self.checkJson_file()

    def export_prman_PB_hit(self):
        self.exportJsonShader('renderman')
        self.checkJson_file()

    def export_redShift_PB_hit(self):
        self.exportJsonShader('redShift')
        self.checkJson_file()

    def convert_stingray_PB_hit(self):
        self.cleanOldSG()
        self.linking_shaders('stingray')

    def convert_redShift_PB_hit(self):
        self.cleanOldSG()
        self.linking_shaders('redShift')

    def convert_prman_PB_hit(self):
        self.cleanOldSG()
        self.linking_shaders('renderman')

    def cleanOldSG(self):
        objName = self.objName_LE.text()
        engine_list = ['redShift', 'renderman', 'stingray']
        for engine in engine_list:
            name_space = objName + "_" + engine + '_SG'
            if pm.namespace(exists=name_space):
                old_nodes = pm.ls(name_space + ":*")
                pm.delete(old_nodes)
                pm.namespace(removeNamespace=name_space)

    def checkJson_file(self):
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        stingray_file = cache_path + "/" + objName + "_stingray_linking.json"
        renderman_file = cache_path + "/" + objName + "_renderman_linking.json"
        redShift_file = cache_path + "/" + objName + "_redShift_linking.json"
        if os.path.exists(stingray_file):
            self.convert_stingray_PB.setEnabled(True)
        if os.path.exists(renderman_file):
            self.convert_prman_PB.setEnabled(True)
        if os.path.exists(redShift_file):
            self.convert_redShift_PB.setEnabled(True)

    def exportJsonShader(self, engine):
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        name_space = objName + "_" + engine + '_SG'
        linking_dict = {}
        sg_list = []
        '''
        for meshShape in self.checked_node:
            SG = pm.listConnections(meshShape, type='shadingEngine')[0]
            linking_dict[meshShape] = SG
            if SG not in SG_list:
                SG_list.append(SG)
        '''
        for key in self.export_json_dict:
            sg = self.export_json_dict[key]
            if sg not in sg_list:
                sg_list.append(sg)

        json_file = open(cache_path + "/" + objName + "_" + engine + "_linking.json", "w")
        json.dump(self.export_json_dict, json_file, ensure_ascii=False, indent=4)
        json_file.close()
        pm.select(sg_list, r=True, noExpand=True)
        print sg_list
        cmds.file(cache_path + "/" + name_space + ".mb", force=True, options="v=0;", type='mayaBinary', exportSelected=True)
        self.checkJson_file()

    def linking_shaders(self, engine):
        abc_nameSpace = self.nameSpace_LE.text()
        if abc_nameSpace != "":
            prefix = abc_nameSpace + ":"
        else:
            prefix = ""
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        name_space = objName + "_" + engine + '_SG'
        json_file = open(cache_path + "/" + objName + "_" + engine + "_linking.json", "r")
        data = json.load(json_file)
        json_file.close()
        cmds.file(cache_path + "/" + name_space + ".mb", i=True, ra=True, type="mayaBinary", ignoreVersion=True, mergeNamespacesOnClash=False, namespace=name_space, options="v=0;p=17;f=0", pr=True)
        for key in data:
            cmds.sets(prefix + key, edit=True, forceElement=name_space + ":" + data[key])

    def checkEngine(self, treeItemList):
        total_num = len(treeItemList)
        redShift_list = []
        renderman_list = []
        stingray_list = []
        for item in treeItemList:
            if item.text(1) == 'RenaderMan':
                renderman_list.append(item.text(1))
            elif item.text(1) == 'RedShift':
                redShift_list.append(item.text(1))
            elif item.text(1) == 'Stingray':
                stingray_list.append(item.text(1))

        if len(redShift_list) == total_num:
            self.export_prman_PB.setEnabled(False)
            self.export_stingray_PB.setEnabled(False)
            self.export_redShift_PB.setEnabled(True)

        elif len(renderman_list) == total_num:
            self.export_prman_PB.setEnabled(True)
            self.export_stingray_PB.setEnabled(False)
            self.export_redShift_PB.setEnabled(False)

        elif len(stingray_list) == total_num:
            self.export_prman_PB.setEnabled(False)
            self.export_stingray_PB.setEnabled(True)
            self.export_redShift_PB.setEnabled(False)

    def deleteTreeItem(self, tree):
        while tree.topLevelItemCount():
            item = tree.takeTopLevelItem(0)

    def expanded_all_PB_hit(self):
        for item in self.top_tree_item:
            item.setExpanded(True)
            number = item.childCount()
            for i in range(number):
                item.child(i).setExpanded(True)

    def expanded_off_PB_hit(self):
        for item in self.top_tree_item:
            item.setExpanded(False)
            number = item.childCount()
            for i in range(number):
                item.child(i).setExpanded(False)

    def select_all_PB_hit(self):
        for item in self.top_tree_item:
            item.setCheckState(0, QtCore.Qt.Checked)

    def select_clean_PB_hit(self):
        for item in self.top_tree_item:
            item.setCheckState(0, QtCore.Qt.Unchecked)
            number = item.childCount()
            for i in range(number):
                item.child(i).setCheckState(0, QtCore.Qt.Unchecked)

    def treeWidgetItem_hit(self, item, column):
        item_index = self.shading_link_treeWidget.indexOfTopLevelItem(item)
        if item_index == -1:
            pm.select(item.text(0), r=True)
        if item_index >= 0:
            node_list = self.shaderInfo[item_index]['mesh']
            pm.select(node_list, r=True)

    def treeWidgetItem_changed(self, item, column):
        item_index = self.shading_link_treeWidget.indexOfTopLevelItem(item)
        childred_list = []
        if item_index == -1:
            mesh = item.text(0)
            childred_list.append(mesh)
            sg = item.text(1)
            sg = sg.split('---> ')[1]
        elif item_index >= 0:
            mesh_list = self.shaderInfo[item_index]['mesh']
            for mesh in mesh_list:
                if mesh not in childred_list:
                    childred_list.append(mesh.name())
            sg = item.text(0)
            sg = sg.split(' ---> ')[1]

        if item.checkState(0) == QtCore.Qt.Checked:
            item.setExpanded(False)
            number = item.childCount()
            if number > 0:
                for i in range(number):
                    item.child(i).setCheckState(0, QtCore.Qt.Unchecked)
            if item_index == -1:
                item.parent().setCheckState(0, QtCore.Qt.Unchecked)
            for mesh in childred_list:
                if self.export_json_dict.has_key(mesh) is False:
                    self.export_json_dict[mesh] = sg

        elif item.checkState(0) == QtCore.Qt.Unchecked:
            for mesh in childred_list:
                if self.export_json_dict.has_key(mesh) is True:
                    del self.export_json_dict[mesh]

        for key in self.export_json_dict:
            print "mesh: %s, sg: %s" % (key, self.export_json_dict[key])


class pathTreeItem_class(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, shading_dict):
        self.parent = parent
        self.shading_dict = shading_dict
        QtWidgets.QTreeWidgetItem.__init__(self)
        used_num = len(self.shading_dict['mesh'])
        self.setText(0, str(used_num) + " mesh(s) point to ---> " + self.shading_dict['SG'])
        self.setText(1, self.checkRenderEngine(self.shading_dict['SG']))
        self.setCheckState(0, QtCore.Qt.Unchecked)
        for node in self.shading_dict['mesh']:
            self.createChild(node.name(), self)
        # self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)

    def createChild(self, node, parent):
        node_item = QtWidgets.QTreeWidgetItem([node])
        node_item.setText(0, node)
        node_item.setText(1, "---> " + self.shading_dict['SG'].nodeName())
        node_item.setCheckState(0, QtCore.Qt.Unchecked)
        parent.addChild(node_item)

    def checkRenderEngine(self, shadingGrp):
        node_list = pm.listConnections(shadingGrp)
        mat_list = pm.ls(node_list, materials=1)
        mat_type_list = []
        for mat in mat_list:
            node_type = mat.type()
            if node_type not in mat_type_list:
                mat_type_list.append(node_type)
        redShift_list = ['RedshiftMaterial', 'RedshiftArchitectural', 'RedshiftMaterialBlender', 'RedshiftSkin']
        renderman_list = ['PxrSurface', 'PxrDisney', 'PxrDisplace']
        stingray_list = ['StingrayPBS']
        redShift_num = self.repeatObj(mat_type_list, redShift_list)
        renderman_num = self.repeatObj(mat_type_list, renderman_list)
        stingray_num = self.repeatObj(mat_type_list, stingray_list)
        max_render_engine = max(redShift_num, renderman_num, stingray_num)
        if max_render_engine == redShift_num:
            return 'RedShift'
        elif max_render_engine == renderman_num:
            return 'RenaderMan'
        elif max_render_engine == stingray_num:
            return 'Stingray'


    def repeatObj(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        set3 = set1.intersection(set2)
        list1 = list(set3)
        return len(list1)

    def cleanNum(self, name):
        while self.is_number(name[-1]):
            name = name[0:-1]
        return name

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

##################################################################################################################


def create():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()


def delete():
    global dialog
    if dialog is None:
        return
    dialog.deleteLater()
    dialog = None


def main():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()


def shadingToolsMain():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()
