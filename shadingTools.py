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
ui_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
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
        self.setWindowTitle('shading tools'+' v0.5'+u' by 小黑')
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
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/shadingTools.csv'
        self.save_UI_list = [self.shadingToolsCreateNodes_wid.texturePath_LE, self.shadingToolsMeshLink_wid.cachePath_LE, self.shadingToolsMeshLink_wid.objName_LE]
        self.layout().addWidget(main_tab_Widget)
        self.setFromCsv()

    def closeEvent(self, event):
        self.writeCsv()

    def writeCsv(self):
        if os.path.exists(self.python_temp) == False:
            os.mkdir(self.python_temp)
        data = [['var_name', 'value']]
        for obj in self.save_UI_list:
            obj_info = [obj.objectName(), self.getValue(obj)]
            data.append(obj_info)
        file = open(self.python_temp_csv, 'w')
        w = csv.writer(file)
        w.writerows(data)
        file.close()

    def setFromCsv(self):
        if os.path.exists(self.python_temp_csv):
            cache_value_list = []
            file = open(self.python_temp_csv, 'r')
            for i in csv.DictReader(file):
                cache_value_list.append(i['value'])
            file.close()
            for index, value in enumerate(cache_value_list):
                self.save_UI_list[index].setText(value)

    def getValue(self, widget):
        if type(widget) == QtWidgets.QLineEdit:
            return widget.text()


class shadingToolsCreateNodes_ui(QtWidgets.QWidget, shadingToolsCreateNodes_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(shadingToolsCreateNodes_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        self.rman_folder = os.getenv('RMANTREE')
        self.pbr_name_list = ['BaseColor', 'Metallic', 'Roughness', 'Normal', 'Height', 'Emissive']
        # self.texturePath_LE.setText('//mcd-one/3d_project/fox_spirit_v01/assets/character/role_vixen_b/texture/sourceimages/exr')

    def connectInterface(self):
        self.texturePathBro_PB.clicked.connect(self.texturePathBro_PB_hit)
        self.texturePathOpen_PB.clicked.connect(self.texturePathOpen_PB_hit)
        self.analyzeTextureSets_PB.clicked.connect(self.analyzeTextureSets_PB_hit)
        self.prman_PB.clicked.connect(self.prman_PB_hit)
        self.stingray_PB.clicked.connect(self.stingray_PB_hit)
        self.redShift_PB.clicked.connect(self.redShift_PB_hit)

    def texturePathBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.texturePath_LE.setText(path)

    def texturePathOpen_PB_hit(self):
        texture_path = self.texturePath_LE.text()
        texture_file = texture_path.replace('/', '\\')
        os.startfile(texture_file)

    def exrList(self, path):
        file_list = os.listdir(path)
        exr_list = []
        for i in file_list:
            if os.path.isfile(path+"/"+i):
                if os.path.splitext(i)[1] == ".exr":
                    exr_list.append(i)
        exr_list.sort()
        return exr_list

    def checkTextureInfo(self):
        texture_path = self.texturePath_LE.text()
        texture_path = texture_path.replace('\\', '/')
        exr_list = self.exrList(texture_path)
        textures_sets = []
        for exr in exr_list:
            name = os.path.splitext(exr)[0]
            for suffix in self.pbr_name_list:
                if name[-len(suffix):len(name)] == suffix:
                    baseName = name[0:-len(suffix)-1]
                    if baseName not in textures_sets:
                        textures_sets.append(baseName)
        texture_info = []
        for texture_name in textures_sets:
            texture_dic = {}
            texture_dic['BaseName'] = texture_name
            for suffix in self.pbr_name_list:
                texture_dic[suffix] = 'no'
                if os.path.exists(texture_path+'/'+texture_name+"_"+suffix+'.exr'):
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
            set_info_layout.addWidget(label, 0, index+1)

        for index, imgSet in enumerate(self.texture_info):
            basename_CB = checkBox_class(self, imgSet['BaseName'], index)
            set_info_layout.addWidget(basename_CB, index+1, 0)
            for index2, pbrName in enumerate(self.pbr_name_list):
                label = QtWidgets.QLabel(imgSet[pbrName])
                set_info_layout.addWidget(label, index+1, index2+1)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaLayout.addSpacerItem(self.spacerItem)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())

    def prman_PB_hit(self):
        for index in self.set_CB_list:
            disney_shade = cmds.shadingNode('PxrDisney', n=self.texture_info[index]['BaseName']+'_PxrDisney', asShader=True)
            for pbrName in self.pbr_name_list:
                self.creatPrmanNode(disney_shade, self.texture_info[index]['BaseName'], pbrName, self.texture_info[index][pbrName])

    def creatPrmanNode(self, shader, texSet, pbrName, exist):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Normal' and pbrName != 'Height':
                tex_node = cmds.shadingNode('PxrTexture', n=texSet+'_'+pbrName+'_PxrTexture', asTexture=True)
                exr = texture_path+'/'+texSet+'_'+pbrName+'.exr'
                tex = texture_path+'/'+texSet+'_'+pbrName+'.tex'
                self.txmakeCMD(exr, tex)
                cmds.setAttr(tex_node+'.filename', tex, type="string")
                if pbrName == 'BaseColor':
                    cmds.setAttr(tex_node+'.linearize', 1)
                    cmds.connectAttr(tex_node+'.resultRGB', shader+'.baseColor')
                    cmds.connectAttr(tex_node+'.resultA', shader+'.presence')
                elif pbrName == 'Metallic':
                    cmds.setAttr(tex_node+'.linearize', 0)
                    cmds.connectAttr(tex_node+'.resultR', shader+'.metallic')
                elif pbrName == 'Roughness':
                    cmds.setAttr(tex_node+'.linearize', 0)
                    cmds.connectAttr(tex_node+'.resultR', shader+'.roughness')
                elif pbrName == 'Emissive':
                    cmds.setAttr(tex_node+'.linearize', 0)
                    cmds.connectAttr(tex_node+'.resultRGB', shader+'.emitColor')
            elif pbrName == 'Normal':
                tex_node = cmds.shadingNode('PxrNormalMap', n=texSet+'_'+pbrName+'_PxrNormalMap', asTexture=True)
                exr = texture_path+'/'+texSet+'_'+pbrName+'.exr'
                tex = texture_path+'/'+texSet+'_'+pbrName+'.tex'
                self.txmakeCMD(exr, tex)
                cmds.setAttr(tex_node+'.filename', tex, type="string")
                cmds.connectAttr(tex_node+'.resultN', shader+'.bumpNormal')

        # self.pbr_name_list=['BaseColor','Metallic','Roughness','Normal','Height','Emissive']
    def txmakeCMD(self, exr, tex):
        txmakeCMD = "\""+self.rman_folder+"bin\\txmake.exe"+"\""+" -newer"+" -mode black"+" "+exr+" "+tex
        subprocess.call(txmakeCMD, shell=True)

    def stingray_PB_hit(self):
        for index in self.set_CB_list:
            stingray_shade = cmds.shadingNode('StingrayPBS', n=self.texture_info[index]['BaseName']+'_StingrayPBS', asShader=True)
            cmds.setAttr(stingray_shade+'.initgraph', True)
            for pbrName in self.pbr_name_list:
                self.creatStingrayNode(stingray_shade, self.texture_info[index]['BaseName'], pbrName, self.texture_info[index][pbrName])

    def creatStingrayNode(self, shader, texSet, pbrName, exist):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Height':
                tex_node = cmds.shadingNode('file', n=texSet+'_'+pbrName+'_file', asTexture=True, isColorManaged=True)
                cmds.setAttr(tex_node+'.fileTextureName', texture_path+'/'+texSet+'_'+pbrName+'.exr', type="string")
                if pbrName == 'BaseColor':
                    cmds.setAttr(shader+'.use_color_map', 1)
                    cmds.connectAttr(tex_node+'.outColor', shader+'.TEX_color_map')
                elif pbrName == 'Metallic':
                    cmds.setAttr(shader+'.use_metallic_map', 1)
                    cmds.connectAttr(tex_node+'.outColor', shader+'.TEX_metallic_map')
                elif pbrName == 'Roughness':
                    cmds.setAttr(shader+'.use_roughness_map', 1)
                    cmds.connectAttr(tex_node+'.outColor', shader+'.TEX_roughness_map')
                elif pbrName == 'Normal':
                    cmds.setAttr(shader+'.use_normal_map', 1)
                    cmds.connectAttr(tex_node+'.outColor', shader+'.TEX_normal_map')
                elif pbrName == 'Emissive':
                    cmds.setAttr(shader+'.use_emissive_map', 1)
                    cmds.connectAttr(tex_node+'.outColor', shader+'.TEX_emissive_map')

    def redShift_PB_hit(self):
        for index in self.set_CB_list:
            redShift_shade = cmds.shadingNode('RedshiftMaterial', n=self.texture_info[index]['BaseName']+'_RedshiftMaterial', asShader=True)
            cmds.setAttr(redShift_shade+'.refl_brdf', 1)
            cmds.setAttr(redShift_shade+'.refl_fresnel_mode', 2)
            for pbrName in self.pbr_name_list:
                self.creatRedShiftNode(redShift_shade, self.texture_info[index]['BaseName'], pbrName, self.texture_info[index][pbrName])

    def creatRedShiftNode(self, shader, texSet, pbrName, exist):
        texture_path = self.texturePath_LE.text()
        if exist == 'yes':
            if pbrName != 'Normal' and pbrName != 'Height':
                tex_node = cmds.shadingNode('file', n=texSet+'_'+pbrName+'_file', asTexture=True, isColorManaged=True)
                cmds.setAttr(tex_node+'.fileTextureName', texture_path+'/'+texSet+'_'+pbrName+'.exr', type="string")
                if pbrName == 'BaseColor':
                    cmds.setAttr(tex_node+'.colorSpace', 'sRGB', type='string')
                    cmds.connectAttr(tex_node+'.outColor', shader+'.diffuse_color')
                elif pbrName == 'Metallic':
                    cmds.setAttr(tex_node+'.colorSpace', 'Raw', type='string')
                    cmds.connectAttr(tex_node+'.outColorR', shader+'.refl_metalness')
                elif pbrName == 'Roughness':
                    cmds.setAttr(tex_node+'.colorSpace', 'Raw', type='string')
                    cmds.connectAttr(tex_node+'.outColorR', shader+'.refl_roughness')
                elif pbrName == 'Emissive':
                    cmds.setAttr(tex_node+'.colorSpace', 'sRGB', type='string')
                    cmds.connectAttr(tex_node+'.outColor', shader+'.emission_color')
            elif pbrName == 'Normal':
                tex_node = cmds.shadingNode('RedshiftNormalMap', n=texSet+'_'+pbrName+'_RedshiftNormalMap', asUtility=True)
                cmds.setAttr(tex_node+'.tex0', texture_path+'/'+texSet+'_'+pbrName+'.exr', type="string")
                cmds.connectAttr(tex_node+'.outDisplacementVector', shader+'.bump_input')


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
        if self.checkState() == False:
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
        shadingInfo = []
        shadingGrp_list = []
        for meshShape in meshShape_list:
            SG = cmds.listConnections(meshShape, type='shadingEngine')[0]
            if SG not in shadingGrp_list:
                shadingGrp_list.append(SG)
        for shadingGrp in shadingGrp_list:
            shading_dict = {}
            shading_dict['SG'] = shadingGrp
            shading_dict['meshShape'] = []
            for meshShape in meshShape_list:
                SG = cmds.listConnections(meshShape, type='shadingEngine')[0]
                if SG == shadingGrp:
                    shading_dict['meshShape'].append(meshShape)
            shadingInfo.append(shading_dict)
        return shadingInfo

    def getMeshShape(self):
        transform_list = []
        meshShape_list = []
        seleted_list = cmds.ls(sl=True)
        for node in seleted_list:
            if cmds.nodeType(node) == 'transform':
                transform_list.append(node)
        transform_list.sort()

        for node in transform_list:
            shape = cmds.listRelatives(node, shapes=True)
            if shape != None and cmds.nodeType(shape[0]) == 'mesh':
                meshShape_list.append(shape[0])
        group_list = []
        group_transform = []
        for node in transform_list:
            if self.isGroup(node):
                group_list.append(node)
        for group in group_list:
            children = cmds.listRelatives(group, c=True, type='transform')
            group_transform.extend(children)
        group_transform = list(set(group_transform))
        for node in group_transform:
            shape = cmds.listRelatives(node, shapes=True)
            if shape != None and cmds.nodeType(shape[0]) == 'mesh':
                meshShape_list.append(shape[0])
        meshShape_list = list(set(meshShape_list))
        meshShape_list.sort()
        return meshShape_list

    def isGroup(self, node):
        children = cmds.listRelatives(node, c=True, f=True)
        if children == None:
            return True
        for c in children:
            if cmds.nodeType(c) != 'transform':
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
            name_space = objName+"_"+engine+'_SG'
            if cmds.namespace(exists=name_space):
                old_nodes = cmds.ls(name_space+":*")
                cmds.delete(old_nodes)
                cmds.namespace(removeNamespace=name_space)

    def checkJson_file(self):
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        stingray_file = cache_path+"/"+objName+"_stingray_linking.json"
        renderman_file = cache_path+"/"+objName+"_renderman_linking.json"
        redShift_file = cache_path+"/"+objName+"_redShift_linking.json"
        if os.path.exists(stingray_file):
            self.convert_stingray_PB.setEnabled(True)
        if os.path.exists(renderman_file):
            self.convert_prman_PB.setEnabled(True)
        if os.path.exists(redShift_file):
            self.convert_redShift_PB.setEnabled(True)

    def exportJsonShader(self, engine):
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        name_space = objName+"_"+engine+'_SG'
        linking_dict = {}
        SG_list = []
        for meshShape in self.checked_node:
            SG = cmds.listConnections(meshShape, type='shadingEngine')[0]
            linking_dict[meshShape] = SG
            if SG not in SG_list:
                SG_list.append(SG)
        json_file = open(cache_path+"/"+objName+"_"+engine+"_linking.json", "w")
        json.dump(linking_dict, json_file, ensure_ascii=False, indent=4)
        json_file.close()
        cmds.select(SG_list, r=True, noExpand=True)
        cmds.file(cache_path+"/"+name_space+".mb", force=True, options="v=0;", type='mayaBinary', exportSelected=True)
        self.checkJson_file()

    def linking_shaders(self, engine):
        cache_path = self.cachePath_LE.text()
        objName = self.objName_LE.text()
        name_space = objName+"_"+engine+'_SG'
        json_file = open(cache_path+"/"+objName+"_"+engine+"_linking.json", "r")
        data = json.load(json_file)
        json_file.close()
        cmds.file(cache_path+"/"+name_space+".mb", i=True, ra=True, type="mayaBinary", ignoreVersion=True, mergeNamespacesOnClash=False, namespace=name_space, options="v=0;p=17;f=0", pr=True)
        for key in data:
            cmds.sets(key, edit=True, forceElement=name_space+":"+data[key])

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
            node_list = self.shaderInfo[item_index]['meshShape']
            pm.select(node_list, r=True)

    def treeWidgetItem_changed(self, item, column):
        item_index = self.shading_link_treeWidget.indexOfTopLevelItem(item)
        childred_list = []
        if item_index == -1:
            childred_list.append(item.text(0))
        elif item_index >= 0:
            node_list = self.shaderInfo[item_index]['meshShape']
            for node in node_list:
                childred_list.append(node)
        if item.checkState(0) == QtCore.Qt.Checked:
            item.setExpanded(False)
            number = item.childCount()
            if number > 0:
                for i in range(number):
                    item.child(i).setCheckState(0, QtCore.Qt.Unchecked)
            if item_index == -1:
                item.parent().setCheckState(0, QtCore.Qt.Unchecked)
            for node in childred_list:
                if node not in self.checked_node:
                    self.checked_node.append(node)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            for node in childred_list:
                if node in self.checked_node:
                    self.checked_node.remove(node)


class pathTreeItem_class(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, shading_dict):
        self.parent = parent
        self.shading_dict = shading_dict
        QtWidgets.QTreeWidgetItem.__init__(self)
        used_num = len(self.shading_dict['meshShape'])
        self.setText(0, str(used_num)+" mesh(s) point to ---> "+self.shading_dict['SG'])
        self.setText(1, self.checkRenderEngine(self.shading_dict['SG']))
        self.setCheckState(0, QtCore.Qt.Unchecked)
        for node in self.shading_dict['meshShape']:
            self.createChild(node, self)

    def createChild(self, node, parent):
        node_item = QtWidgets.QTreeWidgetItem([node])
        node_item.setCheckState(0, QtCore.Qt.Unchecked)
        parent.addChild(node_item)

    def checkRenderEngine(self, shadingGrp):
        shader = cmds.listConnections(shadingGrp+'.surfaceShader', d=False, s=True)[0]
        shader = cmds.nodeType(shader)
        redShift_list = ['RedshiftMaterial', 'RedshiftArchitectural', 'RedshiftArchitectural', 'RedshiftMaterialBlender', 'RedshiftSkin']
        renderman_list = ['PxrSurface', 'PxrDisney']
        if shader == 'StingrayPBS':
            return 'Stingray'
        if shader in renderman_list:
            return 'RenaderMan'
        if shader in redShift_list:
            return 'RedShift'

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
