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
ui_path = 'C:/Users/' + username + '/Documents/maya/' + maya_version + '/scripts/ui'
py27_lib = 'C:/Python27/Lib/site-packages'
sys.path.append(py27_lib)
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")

import prmanR22_tools_archiveEdit_ui
reload(prmanR22_tools_archiveEdit_ui)

import prmanR22_tools_renderSets_ui
reload(prmanR22_tools_renderSets_ui)

import prmanR22_tools_renderSetUp_ui
reload(prmanR22_tools_renderSetUp_ui)

import prmanR22_tools_objReplacement_ui
reload(prmanR22_tools_objReplacement_ui)

import prmanR22_tools_rlfShaderEdit_ui
reload(prmanR22_tools_rlfShaderEdit_ui)


dialog = None


# ------------------------------------------------------------------------------------
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('prman R22 tools' + ' v0.5' + u' by 小黑')
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
        self.prmanR22_tools_renderSetUp_wid = prmanR22_tools_renderSetUp_ui()
        self.prmanR22_tools_objReplacement_wid = prmanR22_tools_objReplacement_ui()
        self.prmanR22_tools_rlfShaderEdit_wid = prmanR22_tools_rlfShaderEdit_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.prmanR22_tools_archiveEdit_wid, "Archive Editor")
        main_tab_Widget.addTab(self.prmanR22_tools_renderSets_wid, "Render Sets")
        main_tab_Widget.addTab(self.prmanR22_tools_renderSetUp_wid, "Render SetUp")
        main_tab_Widget.addTab(self.prmanR22_tools_objReplacement_wid, "Obj Replacement")
        main_tab_Widget.addTab(self.prmanR22_tools_rlfShaderEdit_wid, "Rif shader Editor")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/prmanR22_tools.csv'
        self.python_temp_json = self.python_temp + '/prmanR22_tools.json'
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
            self.prmanR22_tools_archiveEdit_wid.importGpuCache_CB,
            self.prmanR22_tools_archiveEdit_wid.importShader_CB,
            self.prmanR22_tools_renderSets_wid.subDivisionOn_RB,
            self.prmanR22_tools_renderSets_wid.subDivisionOff_RB,
            self.prmanR22_tools_renderSets_wid.matteIdNum_combobox,
            self.prmanR22_tools_renderSets_wid.matteIdRed_RB,
            self.prmanR22_tools_renderSets_wid.matteIdGreen_RB,
            self.prmanR22_tools_renderSets_wid.matteIdBlue_RB,
            self.prmanR22_tools_renderSets_wid.commonAttr_comboBox,
            self.prmanR22_tools_renderSets_wid.commonAttrOn_RP,
            self.prmanR22_tools_renderSets_wid.commonAttrOn_RP,
            self.prmanR22_tools_objReplacement_wid.targetGetObj_LE,
            self.prmanR22_tools_objReplacement_wid.replaceGetObj_LE,
            self.prmanR22_tools_objReplacement_wid.targetVdb_LE,
            self.prmanR22_tools_objReplacement_wid.vdbFile_LE,
            self.prmanR22_tools_objReplacement_wid.vdbSg_LE
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
        self.importArchive_PB.clicked.connect(self.importArchive_PB_hit)

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
        group = self.rootGroup_LE.text()
        mesh_ren_list = self.groupFix(group)
        shadingInfo = self.getShader(mesh_ren_list)
        SG_list = []
        for i in shadingInfo:
            SG_list.append(i['SG'])
        pm.select(SG_list, r=True, noExpand=True)

    def tagEditAdd_PB_hit(self):
        tag_name = self.tagEditName_LE.text()
        group = self.rootGroup_LE.text()
        mesh_ren_list = self.groupFix(group)
        shadingInfo = self.getShader(mesh_ren_list)
        SG_list = []
        for i in shadingInfo:
            SG_list.append(i['SG'])
        for SG in SG_list:
            exists = pm.attributeQuery('gpuCacheShaderTag', node=SG, ex=True)
            if exists is False:
                pm.addAttr(SG, longName='gpuCacheShaderTag', dataType='string')
            SG.setAttr('gpuCacheShaderTag', tag_name)

    def getUsedShaderSg(self):
        group = self.rootGroup_LE.text()
        children_list = pm.listRelatives(group, ad=True, children=True, type='mesh')
        SG_list = []
        for meshShape in children_list:
            SG = pm.listConnections(meshShape.name(), type='shadingEngine')
            if SG != []:
                if SG[0] != 'initialShadingGroup':
                    print str(meshShape.name()) + ' SG: %s' % (SG[0])
                    if SG[0] not in SG_list:
                        SG_list.append(SG[0])
        for SG in SG_list:
            print 'SG : %s' % (SG)
        return SG_list

    def groupFix(self, group):
        group = pm.PyNode(group)
        '''
        transform_list = pm.listRelatives(group, allDescendents=True, type='transform', fullPath=True)
        transform_list.append(group)
        for tran_node in transform_list:
            tran_node.setAttr('translateX', lock=0)
            tran_node.setAttr('translateY', lock=0)
            tran_node.setAttr('translateZ', lock=0)
            tran_node.setAttr('rotateX', lock=0)
            tran_node.setAttr('rotateY', lock=0)
            tran_node.setAttr('rotateZ', lock=0)
            tran_node.setAttr('scaleX', lock=0)
            tran_node.setAttr('scaleY', lock=0)
            tran_node.setAttr('scaleZ', lock=0)
        '''

        mesh_ren_list = []
        mesh_list = pm.listRelatives(group, allDescendents=True, type='mesh', fullPath=True)
        mesh_t_list = []
        for mesh in mesh_list:
            mesh_t = mesh.getTransform()
            mesh_t_list.append(mesh_t)
        mesh_t_list = list(set(mesh_t_list))
        for mesh_t in mesh_t_list:
            if self.mesh_vis_check(mesh_t) is True:
                mesh_ren_list.append(mesh_t)
        mesh_ren_list.sort()
        mesh_s_list = []
        for mesh_t in mesh_ren_list:
            mesh_s = pm.listRelatives(mesh_t, shapes=True)
            mesh_s_list = mesh_s_list + mesh_s
        mesh_s_list.sort()
        return mesh_s_list

    def mesh_vis_check(self, node):
        parent_list = []
        while len(pm.listRelatives(node, parent=True, type='transform')) == 1:
            node_p = pm.listRelatives(node, parent=True, type='transform')[0]
            parent_list.append(node_p)
            node = node_p
        for parent in parent_list:
            if parent.getAttr('visibility') is False:
                return False
        return True

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
            if shadingGrp.name() not in default_mat:
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

    def exportArchive_PB_hit(self):
        path = self.archiveExportPath_LE.text()
        name = self.exportName_LE.text()
        group = self.rootGroup_LE.text()
        mesh_ren_list = self.groupFix(group)
        shadingInfo = self.getShader(mesh_ren_list)
        if self.exportGpuCache_CB.isChecked():
            self.exportArchive_abc(path, name, shadingInfo)
        if self.exportRlf_CB.isChecked():
            self.exportArchive_rlf(path, name, shadingInfo)
        if self.exportShader_CB.isChecked():
            self.exportArchive_mb(path, name, shadingInfo)

    def exportArchive_abc(self, path, name, shadingInfo):
        mesh_s_list = []
        for i in shadingInfo:
            mesh_s_list = mesh_s_list + i['mesh']
        mesh_t_list = []
        for mesh_s in mesh_s_list:
            mesh_t = mesh_s.getTransform()
            if mesh_t not in mesh_t_list:
                mesh_t_list.append(mesh_t)

        frame_mode = self.frameRange_comboBox.currentText()
        if frame_mode == "Current Frame":
            frame = pm.currentTime(query=True)
            s_frame = frame
            e_frame = frame
        elif frame_mode == "Animation":
            s_frame = self.startFrame_LE.text()
            e_frame = self.endFrame_LE.text()
        frame_range = "-frameRange " + str(s_frame) + " " + str(e_frame)
        save_abc = path + '/' + name + '.abc'
        prman_preset = "-attrPrefix rman_ -attrPrefix __ -attrPrefix rman_emitFaceIDs -attrPrefix rman_subdivScheme -attrPrefix rman_subdivInterp -attrPrefix rman_subdivFacevaryingInterp -ro -uvWrite -writeColorSets -writeFaceSets -worldSpace -writeVisibility -autoSubd -writeUVSets -dataFormat ogawa"
        for index, mesh in enumerate(mesh_t_list):
            if index == 0:
                root_tex = "-root " + mesh.name()
            else:
                root_tex = root_tex + " -root " + mesh.name()
        file = "-file " + save_abc
        command = frame_range + " " + prman_preset + " " + root_tex + " " + file
        pm.AbcExport(j=command)

    def exportArchive_rlf(self, path, name, shadingInfo):
        sg_list = []
        for i in shadingInfo:
            sg_list.append(i['SG'])
        export_rif = {
            "Format": "RenderMan Look Data",
            "ReferenceURL": "",
            "UserDescription": "",
            "Version": 3,
            "RuleSet": [],
            "AssemblyName": ""
        }
        for sg in sg_list:
            exists = pm.attributeQuery('rlfPathExpTag', node=sg, ex=True)
            if exists is True:
                rlf_path_exp = sg.getAttr('rlfPathExpTag')
                shade_data = {
                    "MatchMethod": "glob",
                    "Notes": "",
                    "Enabled": True,
                    "MaterialId": sg.name(),
                    "DisplacementId": sg.name(),
                    "Rule": rlf_path_exp,
                    "FlowControl": "break",
                    "Id": sg.name(),
                }
                export_rif['RuleSet'].append(shade_data)

        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(export_rif)
        json_path = path.replace('\\', '/')
        if os.path.exists(json_path) is False:
            os.mkdir(json_path)
        json_file = json_path + "/" + name + ".json"
        file2 = open(json_file, 'w')
        json.dump(export_rif, file2, ensure_ascii=True, indent=4)
        file2.close()
        rlf_name = json_path + "/" + name + '.rlf'
        rlf_name.replace("/", "\\")
        json_file.replace("/", "\\")
        if os.path.exists(rlf_name) is True:
            os.remove(rlf_name)
        os.rename(json_file, rlf_name)

    def exportArchive_mb(self, path, name, shadingInfo):
        '''  pymel沒有.file指令, 只能用cmds'''
        SG_list = []
        for i in shadingInfo:
            SG_list.append(i['SG'])
        option = True
        for SG in SG_list:
            exists = pm.attributeQuery('gpuCacheShaderTag', node=SG, ex=True)
            if exists is True:
                tag = SG.getAttr('gpuCacheShaderTag')
                if tag == "":
                    option = False
            else:
                option = False

        if option is True:
            cmds.select(SG_list, r=True, noExpand=True)
            cmds.file(path + "/" + name + "_shaders.mb", force=True, options="v=0;", type='mayaBinary', exportSelected=True)
        else:
            print "error : some shaders wihtout tag"

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
        if 'global_matteID' in self.child_all_list:
            self.child_all_list.remove('global_matteID')
        num = len(self.child_all_list)
        print '#####################################################################################################'
        print 'total of ' + str(num) + ' node(s) will be deleted'
        for node in self.child_all_list:
            print str(node) + ' (' + str(node.type()) + ')'

        pm.undoInfo(ock=True)
        pm.delete(self.child_all_list)
        pm.undoInfo(cck=True)

    def allChildNode(self, node, child_all_list):
        children_list = pm.listConnections(node, destination=False, source=True, scn=True)
        if len(children_list) > 0:
            for child in children_list:
                child_all_list.append(child)
                self.allChildNode(child, child_all_list)

    def importArchive_PB_hit(self):
        cmds.loadPlugin('RenderMan_for_Maya', quiet=True)
        cmds.setAttr("defaultRenderGlobals.currentRenderer", "renderman", type="string")
        pm.setAttr("rmanGlobals.outputAllShaders", 1)
        abc_file = self.importGpuCachePath_LE.text()
        path, abc_name = os.path.split(abc_file)
        name, ext = os.path.splitext(abc_name)
        if self.importGpuCache_CB.isChecked():
            self.importGpu(name, abc_file)
        if self.importShader_CB.isChecked():
            mb_file = path + '/' + name + '_shaders.mb'
            name_shader = name + '_shaders'
            self.importShader(mb_file, name_shader)

    def importGpu(self, name, abc_file):
        gpu_node = pm.createNode('gpuCache', name=name + 'Shape')
        gpu_node.setAttr('cacheFileName', abc_file)
        gpu_node_t = gpu_node.getTransform()
        gpu_node_t.rename(name)

    def importShader(self, mb_file, name_shader):
        cmds.file(mb_file, i=True, ignoreVersion=True, rpr=name_shader, options="v=0;p=17;f=0", pr=True, mergeNamespacesOnClash=False)


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
            node_type = obj.getShape().type()
            if node_type == 'mesh' or 'RenderManArchive':
                mesh_list.append(obj)
        return mesh_list

    def matteIdAttach_PB_hit(self):
        self.createMatteAttrNode()
        attr_name, matteIdColor, attr_node = self.checkMatteIdData()
        mesh_list = self.getSelMeshList()
        for mesh in mesh_list:
            exists = pm.attributeQuery(attr_name, node=mesh, ex=True)
            if exists is False:
                pm.addAttr(mesh, longName=attr_name, usedAsColor=True, attributeType='float3', keyable=True)
                pm.addAttr(mesh, longName=attr_name + 'R', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                pm.addAttr(mesh, longName=attr_name + 'G', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                pm.addAttr(mesh, longName=attr_name + 'B', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
            pm.connectAttr(attr_node.defaultFloat3, mesh.name() + '.' + attr_name, f=True)

    def matteIdDetach_PB_hit(self):
        self.createMatteAttrNode()
        mesh_list = self.getSelMeshList()
        attr_name, matteIdColor, attr_node = self.checkMatteIdData()
        for mesh in mesh_list:
            exists = pm.attributeQuery(attr_name, node=mesh, ex=True)
            if exists is True:
                pm.deleteAttr(mesh, at=attr_name)

    def checkMatteIdData(self):
        matteID_num = self.matteIdNum_combobox.currentText()
        attr_name = 'rmanC' + matteID_num
        if self.matteIdRed_RB.isChecked():
            matteIdColor = 'red'
            attr_node = pm.PyNode(matteID_num + '_red_pxrAttr')
        elif self.matteIdGreen_RB.isChecked():
            matteIdColor = 'green'
            attr_node = pm.PyNode(matteID_num + '_green_pxrAttr')
        elif self.matteIdBlue_RB.isChecked():
            matteIdColor = 'blue'
            attr_node = pm.PyNode(matteID_num + '_blue_pxrAttr')
        return attr_name, matteIdColor, attr_node

    def createMatteAttrNode(self):
        for num in range(8):
            matteID_r = 'MatteID' + str(num) + '_red_pxrAttr'
            matteID_g = 'MatteID' + str(num) + '_green_pxrAttr'
            matteID_b = 'MatteID' + str(num) + '_blue_pxrAttr'
            if pm.objExists(matteID_r):
                print str(matteID_r) + ' already exists'
            else:
                node_r = pm.shadingNode('PxrAttribute', at=True, n=matteID_r)
            node_r = pm.PyNode(matteID_r)
            node_r.setAttr('defaultFloat3', (1, 0, 0))

            if pm.objExists(matteID_g):
                print str(matteID_g) + ' already exists'
            else:
                node_g = pm.shadingNode('PxrAttribute', at=True, n=matteID_g)
            node_g = pm.PyNode(matteID_g)
            node_g.setAttr('defaultFloat3', (0, 1, 0))

            if pm.objExists(matteID_b):
                print str(matteID_b) + ' already exists'
            else:
                node_b = pm.shadingNode('PxrAttribute', at=True, n=matteID_b)
            node_b = pm.PyNode(matteID_b)
            node_b.setAttr('defaultFloat3', (0, 0, 1))

    def matteIdSelect_PB_hit(self):
        attr_name, matteIdColor, attr_node = self.checkMatteIdData()
        node_list = pm.listConnections(attr_node.defaultFloat3, s=False, d=True)
        sel_list = []
        for node in node_list:
            if node.type() != 'renderLayer':
                sel_list.append(node)
        pm.select(sel_list, replace=True)

    def matteIdPxrMatteId_PB_hit(self):
        if pm.objExists('global_matteID'):
            print 'global_matteID already exists '
        else:
            pm.shadingNode('PxrMatteID', at=True, n='global_matteID')
        PxrSurface_shaders = pm.ls(type='PxrSurface')
        PxrLayerSurface_shaders = pm.ls(type='PxrLayerSurface')
        PxrDisney_shaders = pm.ls(type='PxrDisney')
        PxrMarschnerHair_shaders = pm.ls(type='PxrMarschnerHair')
        for i in PxrSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)
        for i in PxrLayerSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)
        for i in PxrDisney_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.inputAOV', f=True)
        for i in PxrMarschnerHair_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)

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
        if attr == 'primaryVisibility':
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
        if attr == 'primaryVisibility':
            if option != -1:
                for mesh in mesh_list:
                    pm.editRenderLayerAdjustment(mesh.name() + '.' + attr)
                    mesh.setAttr(attr, option)
        else:
            for mesh in mesh_list:
                mesh_t = mesh.getTransform()
                pm.editRenderLayerAdjustment(mesh_t.name() + '.' + attr)
                mesh_t.setAttr(attr, option)

    def commonAttrOverrideRemove_PB_hit(self):
        current_RL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        if current_RL == 'defaultRenderLayer':
            pass
        else:
            attr, option = self.checkCommonAttrData()
            mesh_list = self.getSelMeshList()
            if attr == 'primaryVisibility':
                for mesh in mesh_list:
                    pm.editRenderLayerAdjustment(mesh.name() + '.' + attr, remove=True)
            else:
                for mesh in mesh_list:
                    mesh_t = mesh.getTransform()
                    pm.editRenderLayerAdjustment(mesh_t.name() + '.' + attr, remove=True)

    def commonAttrSelectObj_PB_hit(self):
        attr, option = self.checkCommonAttrData()
        mesh_list = pm.ls(type='mesh')
        action_list = []
        if attr == 'primaryVisibility':
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
            attr_node = pm.PyNode('rlid_' + str(rlid) + '_vis_off_pxrAttr')
            if rlid != 0:
                pm.editRenderLayerAdjustment(obj_s.visibility)
            pm.connectAttr(attr_node.defaultInt, obj_s.visibility, f=True)

    def hideInRlSelect_PB_hit(self):
        render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        node = pm.PyNode(render_layer)
        rlid = node.getAttr('rlid')
        if rlid != 0:
            attr_node = pm.PyNode('rlid_' + str(rlid) + '_vis_off_pxrAttr')
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
                if pm.objExists('rlid_' + str(rlid) + '_vis_off_pxrAttr'):
                    print 'rlid ' + str(rlid) + ' vis_off_pxrAttr already exists'
                else:
                    node = pm.shadingNode('PxrAttribute', at=True, n='rlid_' + str(rlid) + '_vis_off_pxrAttr')
                    node.setAttr('defaultInt', 0)


class prmanR22_tools_renderSetUp_ui(QtWidgets.QWidget, prmanR22_tools_renderSetUp_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanR22_tools_renderSetUp_ui, self).__init__(parent)
        self.setupUi(self)
        self.setDefault()
        self.connectInterface()
        self.info_label.setText("info bar")

    def connectInterface(self):
        # self.serverJsonPathBro_PB.clicked.connect(self.serverJsonPathBro_PB_hit)
        self.serverJsonOPen_PB.clicked.connect(self.serverJsonOPen_PB_hit)
        # self.localJsonFile_Bro.clicked.connect(self.localJsonFile_Bro_hit)
        self.localJsonFile_Open.clicked.connect(self.localJsonFile_Open_hit)
        self.addMatteIdAttr_PB.clicked.connect(self.addMatteIdAttr_PB_hit)
        self.convertToShape_PB.clicked.connect(self.convertToShape_PB_hit)
        self.pxrMatteIdSet_PB.clicked.connect(self.pxrMatteIdSet_PB_hit)
        # self.getNonMeshs_PB.clicked.connect(self.getNonMeshs_PB_hit)
        self.createMatteId_PB.clicked.connect(self.createMatteId_PB_hit)
        self.createPnd_PB.clicked.connect(self.createPnd_PB_hit)
        self.createBeauty_PB.clicked.connect(self.createBeauty_PB_hit)
        pass

    def setDefault(self):
        username = getpass.getuser()
        locale_json_path = 'C:/Users/' + username + '/Documents/maya/RSTemplates'
        self.localJsonFile_LE.setText(locale_json_path)
        self.localJsonFile_LE.setReadOnly(True)
        server_json_file = '//mcd-one/database/apps/3d_apps/mayaPlugin/renderMan/renderSetUp_Json'
        self.serverJsonPath_LE.setText(server_json_file)
        self.serverJsonPath_LE.setReadOnly(True)
        lightGrp_list = self.getLightGrp()
        for lightGrp in lightGrp_list:
            self.lightGrp_comboBox.addItem(lightGrp)
        pass

    def getLightGrp(self):
        prman_lightType_list = [
            'PxrRectLight',
            'PxrDiskLight',
            'PxrDistantLight',
            'PxrSphereLight',
            'PxrCylinderLight',
            'PxrDomeLight',
            'PxrMeshLight',
            'PxrEnvDayLight']
        lightGrp_list = []
        for lightType in prman_lightType_list:
            light_list = pm.ls(type=lightType)
            for light in light_list:
                lightGrp = light.getAttr('lightGroup')
                lightGrp_list.append(lightGrp)
        lightGrp_list = list(set(lightGrp_list))
        return lightGrp_list

    def serverJsonPathBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.serverJsonPath_LE.setText(path)

    def serverJsonOPen_PB_hit(self):
        path = self.serverJsonPath_LE.text()
        path = path.replace('/', '\\')
        os.startfile(path)

    def localJsonFile_Bro_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.localJsonFile_LE.setText(path)

    def localJsonFile_Open_hit(self):
        path = self.localJsonFile_LE.text()
        path = path.replace('/', '\\')
        os.startfile(path)

    def addMatteIdAttr_PB_hit(self):
        sel_list = pm.ls(selection=True)
        mesh_list = []
        for obj in sel_list:
            obj_type = obj.getShape().type()
            print obj_type
            if obj_type == 'mesh' or obj_type == 'HairShape' or obj_type == 'gpuCache':
                mesh_list.append(obj)
        for mesh in mesh_list:
            mesh_t = mesh.getTransform()
            for num in range(8):
                attr_name = 'rmanCMatteID' + str(num)
                exists = pm.attributeQuery(attr_name, node=mesh_t, ex=True)
                if exists is False:
                    pm.addAttr(mesh_t, longName=attr_name, usedAsColor=True, attributeType='float3', keyable=True)
                    pm.addAttr(mesh_t, longName=attr_name + 'R', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                    pm.addAttr(mesh_t, longName=attr_name + 'G', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                    pm.addAttr(mesh_t, longName=attr_name + 'B', defaultValue=1.0, attributeType='float', parent=attr_name, keyable=True)
                    mesh_t.setAttr(attr_name, (0, 0, 0))

    def convertToShape_PB_hit(self):
        sel_list = pm.ls(sl=True)
        shape_list = []
        for obj in sel_list:
            shape_list.append(obj.getShape())
        pm.select(shape_list, replace=True)

    def pxrMatteIdSet_PB_hit(self):
        if pm.objExists('global_matteID'):
            print 'global_matteID already exists'
        else:
            pm.shadingNode('PxrMatteID', at=True, n='global_matteID')
        PxrSurface_shaders = pm.ls(type='PxrSurface')
        PxrLayerSurface_shaders = pm.ls(type='PxrLayerSurface')
        PxrDisney_shaders = pm.ls(type='PxrDisney')
        PxrMarschnerHair_shaders = pm.ls(type='PxrMarschnerHair')
        for i in PxrSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)
        for i in PxrLayerSurface_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)
        for i in PxrDisney_shaders:
            pm.connectAttr('global_matteID.resultAOV', i + '.inputAOV', f=True)
        for i in PxrMarschnerHair_shaders:
            try:
                pm.connectAttr('global_matteID.resultAOV', i + '.utilityPattern[0]', f=True)
            except:
                pass
            try:
                pm.connectAttr('global_matteID.resultAOV', i + '.inputAOV', f=True)
            except:
                pass


    def getNonMeshs_PB_hit(self):
        group = pm.ls(selection=True)[0]
        children_list = pm.listRelatives(group, children=True, allDescendents=True, type='transform')
        mesh_list = pm.listRelatives(group, children=True, allDescendents=True, type='mesh')
        for mesh in mesh_list:
            mesh_t = mesh.getTransform()
            children_list.remove(mesh_t)
        pm.select(children_list, replace=True)

    def createMatteId_PB_hit(self):
        max_num = self.createMatteId_spinBox.value()
        num_list = range(int(max_num) + 1)
        for num in num_list:
            display_name = "_MatteID" + str(num)
            display_channel_name = "MatteID" + str(num)
            channel_source = "MatteID" + str(num)
            self.createAovDisplay(display_name, display_channel_name, channel_source, "")
            '''
            display_name = "_MatteID"+str(num)
            if pm.objExists(display_name) is False:
                rman_display_node = pm.createNode('rmanDisplay', n=display_name)
                rman_display_node.setAttr('enable', 0)
                index = self.getNextFreeMultiIndex('rmanGlobals', 'displays')
                pm.connectAttr(rman_display_node.message, 'rmanGlobals.displays[%s]' % (index))
                channel_name = "MatteID"+str(num)
                rman_display_channel_node = pm.createNode('rmanDisplayChannel', n=channel_name)
                rman_display_channel_node.setAttr('channelSource', channel_name)
                index = self.getNextFreeMultiIndex(display_name, 'displayChannels')
                pm.connectAttr(rman_display_channel_node.message, display_name+'.displayChannels[%s]' % (index))
            '''

    def createPnd_PB_hit(self):
        self.createAovDisplay('_Pworld', '__Pworld', '__Pworld', "")
        self.createAovDisplay('_Nworld', '__Nworld', '__Nworld', "")
        self.createAovDisplay('_depth', '__depth', '__depth', "")

    def createAovDisplay(self, display_name, display_channel_name, channel_source, lightGrp):
        if pm.objExists(display_name) is False:
            rman_display_node = pm.createNode('rmanDisplay', n=display_name)
            rman_display_node.setAttr('enable', 0)
            index = self.getNextFreeMultiIndex('rmanGlobals', 'displays')
            pm.connectAttr(rman_display_node.message, 'rmanGlobals.displays[%s]' % (index))
            rman_display_channel_node = pm.createNode('rmanDisplayChannel', n=display_channel_name)
            rman_display_channel_node.setAttr('channelSource', channel_source)
            index = self.getNextFreeMultiIndex(display_name, 'displayChannels')
            pm.connectAttr(rman_display_channel_node.message, display_name + '.displayChannels[%s]' % (index))
            if lightGrp != "":
                rman_display_channel_node.setAttr('lpeLightGroup', lightGrp)

    def getNextFreeMultiIndex(self, node, attr):
        mel = 'getNextFreeMultiIndex %s.%s 0' % (node, attr)
        index = pm.mel.eval(mel)
        return index

    def createBeauty_PB_hit(self):
        lightGrpName = self.lightGrp_comboBox.currentText()
        display_name = "_Beauty_" + lightGrpName
        display_channel_name = "Beauty_" + lightGrpName
        channel_source = 'lpe:C[DS]*[<L.>O]'
        self.createAovDisplay(display_name, display_channel_name, channel_source, lightGrpName)


class prmanR22_tools_objReplacement_ui(QtWidgets.QWidget, prmanR22_tools_objReplacement_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanR22_tools_objReplacement_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()

    def connectInterface(self):
        self.targetGetObj_PB.clicked.connect(self.targetGetObj_PB_hit)
        self.replaceGetObj_PB.clicked.connect(self.replaceGetObj_PB_hit)
        self.duplicate_PB.clicked.connect(self.duplicate_PB_hit)
        self.vdbFileSet_PB.clicked.connect(self.vdbFileSet_PB_hit)
        self.vdbBro_PB.clicked.connect(self.vdbBro_PB_hit)
        self.vdbOpen_PB.clicked.connect(self.vdbOpen_PB_hit)
        self.getSg_PB.clicked.connect(self.getSg_PB_hit)
        self.vdbSgSet_PB.clicked.connect(self.vdbSgSet_PB_hit)
        self.targetVdb_PB.clicked.connect(self.targetVdb_PB_hit)

    def targetGetObj_PB_hit(self):
        node_list = pm.ls(sl=True)
        mesh_list = []
        type_list = ['mesh', 'gpuCache', 'OpenVDBVisualize']
        for node in node_list:
            node_type = node.getShape().type()
            if node_type in type_list:
                mesh_list.append(node)
        name_list = []
        for mesh in mesh_list:
            name_list.append(mesh.name())
        node_text = ', '.join(name_list)
        self.targetGetObj_LE.setText(node_text)

    def replaceGetObj_PB_hit(self):
        node_list = pm.ls(sl=True, tl=True)
        mesh_list = []
        type_list = ['mesh', 'gpuCache', 'OpenVDBVisualize']
        for node in node_list:
            node_type = node.getShape().type()
            if node_type in type_list:
                mesh_list.append(node)
        name_list = []
        for mesh in mesh_list:
            name_list.append(mesh.name())
        node_text = ', '.join(name_list)
        self.replaceGetObj_LE.setText(node_text)

    def duplicate_PB_hit(self):
        replaceObj_text = self.replaceGetObj_LE.text()
        replaceObj_node = pm.PyNode(replaceObj_text)
        list_text = self.targetGetObj_LE.text()
        node_list = list_text.split(',')
        for node in node_list:
            node = pm.PyNode(node)
            pm.select(node)
            piv = cmds.xform(piv=True, q=True, ws=True)[:3]
            scale = node.getAttr('scale')
            rotation = node.getAttr('rotate')
            translate = node.getAttr('translate')
            if self.dupDefaultRB.isChecked():
                newNode = pm.duplicate(replaceObj_node, rr=True)[0]
            elif self.dupInputGraph_RB.isChecked():
                newNode = pm.duplicate(replaceObj_node, rr=True, un=True)[0]
            elif self.dupInputConnections_RB.isChecked():
                newNode = pm.duplicate(replaceObj_node, rr=True, ic=True)[0]
            newNode.setAttr('translate', piv)
            newNode.setAttr('scale', scale)
            newNode.setAttr('rotate', rotation)

    def targetVdb_PB_hit(self):
        ls_list = pm.ls(sl=True)
        vdb_list = []
        for vdb in ls_list:
            vdb_s = vdb.getShape()
            if vdb_s.type() == 'OpenVDBVisualize':
                vdb_list.append(vdb)
        name_list = []
        for vdb in vdb_list:
            name_list.append(vdb.name())
        node_text = ', '.join(name_list)
        self.targetVdb_LE.setText(node_text)

    def vdbBro_PB_hit(self):
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        if file != "":
            self.vdbFile_LE.setText(file)

    def vdbOpen_PB_hit(self):
        file = self.vdbFile_LE.text()
        path = os.path.split(file)[0]
        path = path.replace('/', '\\')
        os.startfile(path)

    def vdbFileSet_PB_hit(self):
        vdbfile = self.vdbFile_LE.text()
        list_text = self.targetVdb_LE.text()
        vdb_list = list_text.split(',')
        for vdb in vdb_list:
            vdb = pm.PyNode(vdb)
            vdb_s = vdb.getShape()
            read_node = pm.listConnections(vdb_s, t='OpenVDBRead', s=True)[0]
            read_node.setAttr('VdbFilePath', vdbfile)

    def getSg_PB_hit(self):
        node = pm.ls(sl=True, tl=True)[0]
        print node.type()
        if node.type() == 'shadingEngine':
            self.vdbSg_LE.setText(node.name())

    def vdbSgSet_PB_hit(self):
        list_text = self.targetVdb_LE.text()
        vdb_list = list_text.split(',')
        sg = self.vdbSg_LE.text()
        sg_node = pm.PyNode(sg)
        for vdb in vdb_list:
            vdb = pm.PyNode(vdb)
            vdb_s = vdb.getShape()
            pm.connectAttr(sg_node.message, vdb_s.rman__torattr___customShadingGroup, f=True)


# ------------------------------------------------------------------------------------


class prmanR22_tools_rlfShaderEdit_ui(QtWidgets.QWidget, prmanR22_tools_rlfShaderEdit_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanR22_tools_rlfShaderEdit_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()

    def connectInterface(self):
        self.anlyse_PB.clicked.connect(self.anlyse_PB_hit)
        self.expanded_all_PB.clicked.connect(self.expanded_all_PB_hit)
        self.expanded_off_PB.clicked.connect(self.expanded_off_PB_hit)
        self.texture_info_treeWidget.itemChanged.connect(self.treeItemChanged)
        self.texture_info_treeWidget.itemClicked.connect(self.treeItemClicked)
        self.texture_info_treeWidget.itemDoubleClicked.connect(self.treeItemDoubleClicked)

    def treeItemChanged(self, item, column):
        index = self.texture_info_treeWidget.indexOfTopLevelItem(item)
        if index == -1:
            parent = item.parent()
            top_index = self.texture_info_treeWidget.indexOfTopLevelItem(parent)
            child_index = parent.indexOfChild(item)
            obj_node = self.shadingInfo[top_index]['mesh'][child_index]
            obj_node.rename(item.text(0))

        elif index != -1 and column == 1:
            sg = self.shadingInfo[index]['SG']
            sg.rename(item.text(1))

        elif index != -1 and column == 2:
            sg = self.shadingInfo[index]['SG']
            exists = pm.attributeQuery('rlfPathExpTag', node=sg, ex=True)
            if exists is False:
                pm.addAttr(sg, longName='rlfPathExpTag', dataType='string')
            sg.setAttr('rlfPathExpTag', item.text(2))

    def treeItemClicked(self, item, column):
        index = self.texture_info_treeWidget.indexOfTopLevelItem(item)
        if index == -1:
            parent = item.parent()
            top_index = self.texture_info_treeWidget.indexOfTopLevelItem(parent)
            child_index = parent.indexOfChild(item)
            obj_node = self.shadingInfo[top_index]['mesh'][child_index]
            pm.select(obj_node, r=True, noExpand=True)

        elif index != -1 and column == 1:
            sg = self.shadingInfo[index]['SG']
            pm.select(sg, r=True, noExpand=True)

        elif index != -1 and column == 0:
            mesh_list = self.shadingInfo[index]['mesh']
            pm.select(mesh_list, r=True, noExpand=True)

    def treeItemDoubleClicked(self, item, column):
        index = self.texture_info_treeWidget.indexOfTopLevelItem(item)
        if index == -1 and column == 0:
            item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        elif index != -1 and column == 1 or column == 2:
            item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        else:
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def deleteTreeItem(self, tree):
        while tree.topLevelItemCount():
            item = tree.takeTopLevelItem(0)

    def anlyse_PB_hit(self):
        self.deleteTreeItem(self.texture_info_treeWidget)
        meshShape_list = self.getMeshShape()
        self.shadingInfo = self.getShader(meshShape_list)
        self.top_tree_item = []
        self.texture_info_treeWidget.setAutoFillBackground(True)
        for shadingDict in self.shadingInfo:
            pathTreeItem = pathTreeItem_class(self.texture_info_treeWidget, shadingDict)
            self.top_tree_item.append(pathTreeItem)
            self.texture_info_treeWidget.addTopLevelItem(pathTreeItem)

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

    def getMeshShape(self):
        meshShape_list = []
        seleted_list = pm.ls(sl=True)
        for node in seleted_list:
            node_s_list = pm.listRelatives(node)
            for node_s in node_s_list:
                if node_s.type() == 'mesh':
                    meshShape_list.append(node_s)
        return meshShape_list

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
            if shadingGrp.name() not in default_mat:
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


class pathTreeItem_class(QtWidgets.QTreeWidgetItem):
    def __init__(self, tree_wid, shading_dict):
        self.tree_wid = tree_wid
        self.shading_dict = shading_dict
        QtWidgets.QTreeWidgetItem.__init__(self)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100, 100))
        # brush2 = QtGui.QBrush(Qt.SolidPattern)
        self.setBackground(0, brush)
        self.setBackground(1, brush)
        self.setBackground(2, brush)
        used_num = len(self.shading_dict['mesh'])
        self.setText(0, str(used_num) + " mesh(s) point to --> ")
        self.setText(1, self.shading_dict['SG'].name())
        exists = pm.attributeQuery('rlfPathExpTag', node=self.shading_dict['SG'], ex=True)
        if exists is True:
            path_exp = self.shading_dict['SG'].getAttr('rlfPathExpTag')
            self.setText(2, path_exp)
        for node in self.shading_dict['mesh']:
            node = node.getTransform().name()
            self.createChild(node)

    def createChild(self, node):
        node_item = QtWidgets.QTreeWidgetItem([node])
        # node_item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        node_item.setText(0, node)
        self.addChild(node_item)





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
