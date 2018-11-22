# -*- coding: utf-8 -*-
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import maya.cmds as cmds
import pymel.core as pm
import json
import os
import getpass
import sys
import pprint
maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
py27_lib = 'C:/Python27/Lib/site-packages'
sys.path.append(py27_lib)
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")

import prmanR22_tools_archiveEdit_ui
reload(prmanR22_tools_archiveEdit_ui)

import prmanR22_tools_renderSets_ui
reload(prmanR22_tools_renderSets_ui)
dialog = None


# ------------------------------------------------------------------------------------
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('prman R22 tools'+' v0.'+u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800, 600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0, 0, 0, 0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.prmanR22_tools_archiveEdit_wid = prmanR22_tools_archiveEdit_ui()
        self.prmanR22_tools_renderSets_wid = prmanR22_tools_renderSets_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.prmanR22_tools_archiveEdit_wid, "Archive Editor")
        main_tab_Widget.addTab(self.prmanR22_tools_renderSets_wid, "Render Sets")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/pixiTools.csv'
        self.python_temp_json = self.python_temp+'/pixiTools.json'
        self.layout().addWidget(main_tab_Widget)
        self.save_UI_list = [
            self.prmanR22_tools_archiveEdit_wid.archiveExportPath_LE,
            self.prmanR22_tools_archiveEdit_wid.exportName_LE,
            self.prmanR22_tools_archiveEdit_wid.rootGroup_LE,
            self.prmanR22_tools_archiveEdit_wid.tagEditName_LE,
            self.prmanR22_tools_archiveEdit_wid.exportGpuCache_CB,
            self.prmanR22_tools_archiveEdit_wid.exportRlf_CB,
            self.prmanR22_tools_archiveEdit_wid.exportShader_CB,
            self.prmanR22_tools_archiveEdit_wid.importGpuCachePath_LE,
            self.prmanR22_tools_archiveEdit_wid.tagEditName2_LE,
            self.prmanR22_tools_archiveEdit_wid.importRlf_CB,
            self.prmanR22_tools_archiveEdit_wid.importShader_CB,
            self.prmanR22_tools_renderSets_wid.subDivisionOn_RB,
            self.prmanR22_tools_renderSets_wid.subDivisionOff_RB,
            self.prmanR22_tools_renderSets_wid.matteIdNum_combobox,
            self.prmanR22_tools_renderSets_wid.matteIdRed_RB,
            self.prmanR22_tools_renderSets_wid.matteIdGreen_RB,
            self.prmanR22_tools_renderSets_wid.matteIdBlue_RB,
            self.prmanR22_tools_renderSets_wid.commonAttr_comboBox,
            self.prmanR22_tools_renderSets_wid.commonAttrOn_RP,
            self.prmanR22_tools_renderSets_wid.commonAttrOn_RP
        ]
        self.setFromJson()

    def closeEvent(self, event):
        self.writeJson()

    def setFromJson(self):
        if os.path.exists(self.python_temp_json):
            file = open(self.python_temp_json, "r")
            json_dict = json.load(file)
            file.close()
            for index, widget in enumerate(self.save_UI_list):
                key = 'wid_'+str(index)
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

    def writeJson(self):
        if os.path.exists(self.python_temp) is False:
            os.mkdir(self.python_temp)
        data_dict = {}
        for index, obj in enumerate(self.save_UI_list):
            wid_index = "wid_"+str(index)
            data_dict[wid_index] = {}
            data_dict[wid_index]['value'] = self.getValue(obj)
            data_dict[wid_index]['name'] = obj.objectName()
            data_dict[wid_index]['type'] = str(type(obj))
        file2 = open(self.python_temp_json, 'w')
        json.dump(data_dict, file2, ensure_ascii=True, indent=4)
        file2.close()
# ------------------------------------------------------------------------------------


class prmanR22_tools_archiveEdit_ui(QtWidgets.QWidget, prmanR22_tools_archiveEdit_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanR22_tools_archiveEdit_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        self.setDefault()
        self.info_label.setText("info bar")
        regx = QtCore.QRegExp("[0-9]+$")
        self.onlyInt = QtGui.QRegExpValidator(regx)
        self.startFrame_LE.setValidator(self.onlyInt)
        self.endFrame_LE.setValidator(self.onlyInt)

    def connectInterface(self):
        self.archiveExportBro_PB.clicked.connect(self.archiveExportBro_PB_hit)
        self.archiveExportOpen_PB.clicked.connect(self.archiveExportOpen_PB_hit)
        self.importGpuCachePathBro_PB.clicked.connect(self.importGpuCachePathBro_PB_hit)
        self.importGpuCachePathOpen_PB.clicked.connect(self.importGpuCachePathOpen_PB_hit)
        self.rootGroup_pick_PB.clicked.connect(self.rootGroup_pick_PB_hit)
        self.exportArchive_PB.clicked.connect(self.exportArchive_PB_hit)
        self.tagEditAdd_PB.clicked.connect(self.tagEditAdd_PB_hit)
        self.selectSg_PB.clicked.connect(self.selectSg_PB_hit)
        self.selSgWithTag_PB.clicked.connect(self.selSgWithTag_PB_hit)
        self.tagEditDelShader_PB.clicked.connect(self.tagEditDelShader_PB_hit)

    def setDefault(self):
        pass

    def archiveExportBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.archiveExportPath_LE.setText(path)

    def archiveExportOpen_PB_hit(self):
        path = self.archiveExportPath_LE.text()
        path = path.replace('/', '\\')
        os.startfile(path)

    def importGpuCachePathBro_PB_hit(self):
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        if file != "":
            self.importGpuCachePath_LE.setText(file)

    def importGpuCachePathOpen_PB_hit(self):
        file = self.importGpuCachePath_LE.text()
        path = os.path.split(file)[0]
        path = path.replace('/', '\\')
        os.startfile(path)

    def rootGroup_pick_PB_hit(self):
        root = pm.ls(selection=True, tail=True, allPaths=True)[0]
        self.rootGroup_LE.setText(root.name())

    def selectSg_PB_hit(self):
        SG_list = self.getUsedShaderSg()
        pm.select(SG_list, r=True, noExpand=True)

    def tagEditAdd_PB_hit(self):
        tag_name = self.tagEditName_LE.text()
        SG_list = self.getUsedShaderSg()
        for sg in SG_list:
            exists = pm.attributeQuery('gpuCacheShaderTag', node=sg, ex=True)
            if exists is False:
                pm.addAttr(sg, longName='gpuCacheShaderTag', dataType='string')
            sg.setAttr('gpuCacheShaderTag', tag_name)

    def getUsedShaderSg(self):
        group = self.rootGroup_LE.text()
        children_list = pm.listRelatives(group, ad=True, type='mesh')
        SG_list = []
        for meshShape in children_list:
            SG = pm.listConnections(meshShape, type='shadingEngine')[0]
            if SG not in SG_list:
                SG_list.append(SG)
        return SG_list

    def exportArchive_PB_hit(self):
        path = self.archiveExportPath_LE.text()
        name = self.exportName_LE.text()
        group = self.rootGroup_LE.text()
        if self.exportGpuCache_CB.isChecked():
            self.exportArchive_abc(path, name, group)
        if self.exportRlf_CB.isChecked():
            self.exportArchive_rlf(path, name, group)
        if self.exportShader_CB.isChecked():
            self.exportArchive_mb(path, name, group)

    def exportArchive_abc(self, path, name, group):
        frame_mode = self.frameRange_comboBox.currentText()
        if frame_mode == "Current Frame":
            frame = pm.currentTime(query=True)
            s_frame = frame
            e_frame = frame
        elif frame_mode == "Animation":
            s_frame = self.startFrame_LE.text()
            e_frame = self.endFrame_LE.text()
        save_abc = path+'/'+name+'.abc'
        frame_range = "-frameRange " + s_frame + " " + e_frame
        prman_preset = "-attrPrefix rman__torattr -attrPrefix rman__riattr -attrPrefix rman_emitFaceIDs -uvWrite -writeColorSets -writeFaceSets -writeVisibility -autoSubd -writeUVSets -dataFormat ogawa"
        root = "-root " + group
        file = "-file " + save_abc
        command = frame_range + " " + prman_preset + " " + root + " "+file
        pm.AbcExport(j=command)

    def exportArchive_rlf(self, path, name, group):
        SG_list = self.getUsedShaderSg()
        shade_link_dict = {}
        for sg in SG_list:
            shade_link_dict[sg.nodeName()] = []
            member_list = pm.listConnections(sg.dagSetMembers, type='mesh', s=True, d=False)
            member_list.sort()
            member_list_b = sorted(member_list)
            for member in member_list_b:
                shade_link_dict[sg.nodeName()].append(member.fullPathName())
        export_rif = {
            "Format": "RenderMan Look Data",
            "ReferenceURL": "",
            "UserDescription": "",
            "Version": 2,
            "RuleSet": [],
            "AssemblyName": ""
        }
        for sg in shade_link_dict:
            mesh_list = shade_link_dict[sg]
            for mesh in mesh_list:
                mesh_fix_name = mesh.replace('|', '/')
                shade_data = {
                    "MatchMethod": "glob",
                    "Notes": "",
                    "Enabled": 1,
                    "MaterialId": sg,
                    "DisplacementId": None,
                    "Rule": mesh_fix_name,
                    "FlowControl": "break",
                    "Id": sg
                }
                export_rif['RuleSet'].append(shade_data)

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(export_rif)
        json_path = path.replace('\\', '/')
        if os.path.exists(json_path) is False:
            os.mkdir(json_path)
        json_file = json_path+"/"+name+".json"
        file2 = open(json_file, 'w')
        json.dump(export_rif, file2, ensure_ascii=True, indent=4)
        file2.close()
        rlf_name = json_path+"/"+name+'.rlf'
        rlf_name.replace("/", "\\")
        json_file.replace("/", "\\")
        if os.path.exists(rlf_name) is True:
            os.remove(rlf_name)
        os.rename(json_file, rlf_name)

    def exportArchive_mb(self, path, name, group):
        '''  pymel沒有.file指令, 只能用cmds'''
        children_list = cmds.listRelatives(group, ad=True, type='mesh')
        SG_list = []
        for meshShape in children_list:
            SG = cmds.listConnections(meshShape, type='shadingEngine')[0]
            if SG not in SG_list:
                SG_list.append(SG)
        cmds.select(SG_list, r=True, noExpand=True)
        cmds.file(path+"/"+name+"_shaders.mb", force=True, options="v=0;", type='mayaBinary', exportSelected=True)

    def selSgWithTag_PB_hit(self):
        SG_list = self.getSgWithTag()
        pm.select(SG_list, r=True, noExpand=True)

    def getSgWithTag(self):
        tag_name = self.tagEditName2_LE.text()
        SG_list = pm.ls(type='shadingEngine')
        sg_with_sg_list = []
        for sg in SG_list:
            exists = pm.attributeQuery('gpuCacheShaderTag', node=sg, ex=True)
            if exists is True:
                value = sg.getAttr('gpuCacheShaderTag')
                if value == tag_name:
                    sg_with_sg_list.append(sg)
        return sg_with_sg_list

    def tagEditDelShader_PB_hit(self):
        SG_list = self.getSgWithTag()
        shader_list = []
        self.child_all_list = []
        for sg in SG_list:
            shader = pm.listConnections(sg.rman__surface, source=True, scn=True)
            if len(shader) > 0:
                shader_list.append(shader[0])
                self.allChildNode(shader[0], self.child_all_list)
            dm_shader = pm.listConnections(sg.rman__displacement, source=True, scn=True)
            if len(dm_shader) > 0:
                shader_list.append(dm_shader[0])
                self.allChildNode(dm_shader[0], self.child_all_list)

        self.child_all_list = list(set(self.child_all_list))
        self.child_all_list = self.child_all_list + SG_list + shader_list
        self.child_all_list.remove('global_matteID')
        num = len(self.child_all_list)
        print '#####################################################################################################'
        print 'total of ' + str(num) + ' node(s) will be deleted'
        for node in self.child_all_list:
            print str(node) + ' (' + str(node.type())+')'

        pm.undoInfo(ock=True)
        pm.delete(self.child_all_list)
        pm.undoInfo(cck=True)

    def allChildNode(self, node, child_all_list):
        children_list = pm.listConnections(node, destination=False, source=True, scn=True)
        if len(children_list) > 0:
            for child in children_list:
                child_all_list.append(child)
                self.allChildNode(child, child_all_list)


class prmanR22_tools_renderSets_ui(QtWidgets.QWidget, prmanR22_tools_renderSets_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanR22_tools_renderSets_ui, self).__init__(parent)
        self.setupUi(self)
        self.setDefault()
        self.connectInterface()
        self.info_label.setText("info bar")
        matte_color_butGrp = QtWidgets.QButtonGroup()
        matte_color_butGrp.addButton(self.matteIdRed_RB)
        matte_color_butGrp.addButton(self.matteIdGreen_RB)
        matte_color_butGrp.addButton(self.matteIdBlue_RB)
        subD_butGrp = QtWidgets.QButtonGroup()
        subD_butGrp.addButton(self.subDivisionOn_RB)
        subD_butGrp.addButton(self.subDivisionOff_RB)

    def connectInterface(self):
        self.subdivisionSet_PB.clicked.connect(self.subdivisionSet_PB_hit)
        self.subdivisionSelect_PB.clicked.connect(self.subdivisionSelect_PB_hit)
        self.matteIdAttach_PB.clicked.connect(self.matteIdAttach_PB_hit)
        self.matteIdDetach_PB.clicked.connect(self.matteIdDetach_PB_hit)
        self.matteIdSelect_PB.clicked.connect(self.matteIdSelect_PB_hit)
        self.matteIdPxrMatteId_PB.clicked.connect(self.matteIdPxrMatteId_PB_hit)
        self.commonAttrSet_PB.clicked.connect(self.commonAttrSet_PB_hit)
        self.commonAttrOverrideSet_PB.clicked.connect(self.commonAttrOverrideSet_PB_hit)
        self.commonAttrOverrideRemove_PB.clicked.connect(self.commonAttrOverrideRemove_PB_hit)
        self.commonAttrSelectObj_PB.clicked.connect(self.commonAttrSelectObj_PB_hit)
        self.hideInRlHide_PB.clicked.connect(self.hideInRlHide_PB_hit)
        self.hideInRlSelect_PB.clicked.connect(self.hideInRlSelect_PB_hit)
        self.hideInRlDetach_PB.clicked.connect(self.hideInRlDetach_PB_hit)

    def setDefault(self):
        self.matteIdRed_RB.setStyleSheet("font: 18pt; color: rgb(255, 0, 0);")
        self.matteIdGreen_RB.setStyleSheet("font: 18pt; color: rgb(0, 255, 0);")
        self.matteIdBlue_RB.setStyleSheet("font: 18pt; color: rgb(0, 0, 255);")
        pass

    def subdivisionSet_PB_hit(self):
        if self.subDivisionOn_RB.isChecked():
            option = True
        elif self.subDivisionOff_RB.isChecked():
            option = False
        mesh_list = self.getSelMeshList()
        for mesh in mesh_list:
            if option is True:
                mesh.getShape().setAttr('rman_subdivScheme', 1)
            else:
                mesh.getShape().setAttr('rman_subdivScheme', 0)

    def subdivisionSelect_PB_hit(self):
        if self.subDivisionOn_RB.isChecked():
            option = True
        elif self.subDivisionOff_RB.isChecked():
            option = False
        mesh_list = pm.ls(type='mesh')
        action_list = []
        for mesh in mesh_list:
            if option is True:
                if mesh.getAttr('rman_subdivScheme') == 1:
                    action_list.append(mesh)
            if option is False:
                if mesh.getAttr('rman_subdivScheme') == 0:
                    action_list.append(mesh)
        pm.select(action_list)

    def getSelMeshList(self):
        mesh_list = []
        obj_list = pm.ls(sl=True)
        for obj in obj_list:
            if obj.getShape().type() == 'mesh':
                mesh_list.append(obj)
        return mesh_list

    def matteIdAttach_PB_hit(self):
        attr_name, matteIdColor = self.checkMatteIdData()
        mesh_list = self.getSelMeshList()
        for mesh in mesh_list:
            exists = pm.attributeQuery(attr_name, node=mesh, ex=True)
            if exists is False:
                pm.addAttr(mesh, longName=attr_name, usedAsColor=True, attributeType='float3', keyable=True)
                pm.addAttr(mesh, longName=attr_name+'R', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                pm.addAttr(mesh, longName=attr_name+'G', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                pm.addAttr(mesh, longName=attr_name+'B', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
            if matteIdColor == 'red':
                mesh.setAttr(attr_name, (1, 0, 0))
            if matteIdColor == 'green':
                mesh.setAttr(attr_name, (0, 1, 0))
            if matteIdColor == 'blue':
                mesh.setAttr(attr_name, (0, 0, 1))

    def matteIdDetach_PB_hit(self):
        mesh_list = self.getSelMeshList()
        attr_name, matteIdColor = self.checkMatteIdData()
        for mesh in mesh_list:
            exists = pm.attributeQuery(attr_name, node=mesh, ex=True)
            if exists is True:
                pm.deleteAttr(mesh, at=attr_name)

    def checkMatteIdData(self):
        matteIdNum = self.matteIdNum_combobox.currentText()
        attr_name = 'rmanC' + matteIdNum
        if self.matteIdRed_RB.isChecked():
            matteIdColor = 'red'
        elif self.matteIdGreen_RB.isChecked():
            matteIdColor = 'green'
        elif self.matteIdBlue_RB.isChecked():
            matteIdColor = 'blue'
        return attr_name, matteIdColor

    def matteIdSelect_PB_hit(self):
        mesh_list = pm.ls(type='mesh')
        attr_name, matteIdColor = self.checkMatteIdData()
        action_list = []
        for mesh in mesh_list:
            mesh_t = mesh.getTransform()
            exists = pm.attributeQuery(attr_name, node=mesh_t, ex=True)
            if exists is True:
                value = mesh_t.getAttr(attr_name)
                print value
                if matteIdColor == 'red':
                    if value == (1, 0, 0):
                        action_list.append(mesh_t)
                elif matteIdColor == 'green':
                    if value == (0, 1, 0):
                        action_list.append(mesh_t)
                elif matteIdColor == 'blue':
                    if value == (0, 0, 1):
                        action_list.append(mesh_t)
        pm.select(action_list)

    def matteIdPxrMatteId_PB_hit(self):
        if pm.objExists('global_matteID'):
            print 'global_matteID already exists '
        else:
            pm.shadingNode('PxrMatteID', at=True, n='global_matteID')
        PxrSurface_shaders = pm.ls(type='PxrSurface')
        PxrLayerSurface_shaders = pm.ls(type='PxrLayerSurface')
        PxrDisney_shaders = pm.ls(type='PxrDisney')
        for i in PxrSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i+'.utilityPattern[0]', f=True)
        for i in PxrLayerSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i+'.utilityPattern[0]', f=True)
        for i in PxrDisney_shaders:
            pm.connectAttr('global_matteID.resultAOV', i+'.inputAOV', f=True)

    def checkCommonAttrData(self):
        text = self.commonAttr_comboBox.currentText()
        if text == 'Matte Object':
            attr = 'rman_matteObject'
        elif text == 'Camera Visibility':
            attr = 'primaryVisibility'
        elif text == 'Indirect Visibility':
            attr = 'rman_visibilityIndirect'
        elif text == 'Transmission Visibility':
            attr = 'rman_visibilityTransmission'
        elif text == 'Hold Out':
            attr = 'rman_holdout'
        if self.commonAttrOn_RP.isChecked():
            option = 1
        elif self.commonAttrOff_RP.isChecked():
            option = 0
        elif self.commonAttrInherit_RP.isChecked():
            option = -1
        return attr, option

    def commonAttrSet_PB_hit(self):
        attr, option = self.checkCommonAttrData()
        mesh_list = self.getSelMeshList()
        if attr is 'primaryVisibility':
            if option != -1:
                for mesh in mesh_list:
                    mesh.setAttr(attr, option)
        else:
            for mesh in mesh_list:
                mesh_t = mesh.getTransform()
                mesh_t.setAttr(attr, option)

    def commonAttrOverrideSet_PB_hit(self):
        attr, option = self.checkCommonAttrData()
        mesh_list = self.getSelMeshList()
        if attr is 'primaryVisibility':
            if option != -1:
                for mesh in mesh_list:
                    pm.editRenderLayerAdjustment(mesh.name()+'.'+attr)
                    mesh.setAttr(attr, option)
        else:
            for mesh in mesh_list:
                mesh_t = mesh.getTransform()
                pm.editRenderLayerAdjustment(mesh_t.name()+'.'+attr)
                mesh_t.setAttr(attr, option)


    def commonAttrOverrideRemove_PB_hit(self):
        current_RL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        if current_RL is 'defaultRenderLayer':
            pass
        else:
            attr, option = self.checkCommonAttrData()
            mesh_list = self.getSelMeshList()
            if attr is 'primaryVisibility':
                for mesh in mesh_list:
                    pm.editRenderLayerAdjustment(mesh.name()+'.'+attr, remove=True)
            else:
                for mesh in mesh_list:
                    mesh_t = mesh.getTransform()
                    pm.editRenderLayerAdjustment(mesh_t.name()+'.'+attr, remove=True)

    def commonAttrSelectObj_PB_hit(self):
        attr, option = self.checkCommonAttrData()
        mesh_list = pm.ls(type='mesh')
        action_list = []
        if attr is 'primaryVisibility':
            if option != -1:
                for mesh in mesh_list:
                    value = mesh.getAttr('primaryVisibility')
                    if value == option:
                        mesh_t = mesh.getTransform()
                        action_list.append(mesh_t)
        else:
            for mesh in mesh_list:
                mesh_t = mesh.getTransform()
                value = mesh_t.getAttr(attr)
                if value == option:
                    action_list.append(mesh_t)
        pm.select(action_list)

    def hideInRlHide_PB_hit(self):
        self.createVisAttrNode()
        render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        node = pm.PyNode(render_layer)
        rlid = node.getAttr('rlid')
        sel_list = pm.ls(selection=True)
        for obj in sel_list:
            obj_s = obj.getShape()
            attr_node = pm.PyNode('rlid_'+str(rlid)+'_vis_off_pxrAttr')
            if rlid != 0:
                pm.editRenderLayerAdjustment(obj_s.visibility)
            pm.connectAttr(attr_node.defaultInt, obj_s.visibility, f=True)

    def hideInRlSelect_PB_hit(self):
        render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        node = pm.PyNode(render_layer)
        rlid = node.getAttr('rlid')
        if rlid != 0:
            attr_node = pm.PyNode('rlid_'+str(rlid)+'_vis_off_pxrAttr')
            node_list = pm.listConnections(attr_node.defaultInt, s=False, d=True)
            sel_list = []
            for node in node_list:
                if node.type() != 'renderLayer':
                    sel_list.append(node)
            pm.select(sel_list, replace=True)

    def hideInRlDetach_PB_hit(self):
        render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        node = pm.PyNode(render_layer)
        rlid = node.getAttr('rlid')
        if rlid != 0:
            sel_list = pm.ls(selection=True)
            for obj in sel_list:
                try:
                    obj = obj.getShape()
                except AttributeError:
                    pass
                pm.editRenderLayerAdjustment(obj.visibility, remove=True)

    def createVisAttrNode(self):
        rl_list = pm.ls(type='renderLayer')
        for rl in rl_list:
            rlid = rl.getAttr('rlid')
            if rlid != 0:
                if pm.objExists('rlid_'+str(rlid)+'_vis_off_pxrAttr'):
                    print 'rlid '+str(rlid)+' vis_off_pxrAttr already exists'
                else:
                    node = pm.shadingNode('PxrAttribute', at=True, n='rlid_'+str(rlid)+'_vis_off_pxrAttr')
                    node.setAttr('defaultInt', 0)


# ------------------------------------------------------------------------------------

def create():
    global dialog
    if dialog is None:
        dialog.show()


def main():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()


def prmanR22_toolsMain():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()
