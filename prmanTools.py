# -*- coding: utf-8 -*-
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import maya.cmds as cmds
import pymel.core as pm
import os
import getpass
import inspect
import csv
import time
import sys
maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
import prmanToolsLighting_ui
reload(prmanToolsLighting_ui)
import prmanToolsShaderRename_ui
reload(prmanToolsShaderRename_ui)
import prmanToolsRibEdit_ui
reload(prmanToolsRibEdit_ui)
import prmanToolsTexureEdit_ui
reload(prmanToolsTexureEdit_ui)
import prmanToolsDelUnuse_ui
reload(prmanToolsDelUnuse_ui)
import prmanToolsDelUnknow_ui
reload(prmanToolsDelUnknow_ui)

dialog = None

# ---------------------------------------------------------------------------------------------------#


class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('renderman tools'+' v0.5'+u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800, 600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0, 0, 0, 0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        self.prmanToolsLighting_wid = prmanToolsLighting_ui()
        self.prmanToolsShaderRename_wid = prmanToolsShaderRename_ui()
        self.prmanToolsRibEdit_wid = prmanToolsRibEdit_ui()
        self.prmanToolsTextureEdit_wid = prmanToolsTexureEdit_ui()
        self.prmanToolsDelUnuse_wid = prmanToolsDelUnuse_ui()
        self.prmanToolsDelUnknow_wid = prmanToolsDelUnknow_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.prmanToolsLighting_wid, "lighting")
        main_tab_Widget.addTab(self.prmanToolsShaderRename_wid, "shaderRename")
        main_tab_Widget.addTab(self.prmanToolsRibEdit_wid, "ribEdit")
        main_tab_Widget.addTab(self.prmanToolsTextureEdit_wid, "textureEdit")
        main_tab_Widget.addTab(self.prmanToolsDelUnuse_wid, "deleteUnuse")
        main_tab_Widget.addTab(self.prmanToolsDelUnknow_wid, "deleteUnknow")
        self.layout().addWidget(main_tab_Widget)
        username = getpass.getuser()
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/prmanTools.csv'
        ribEdit_save_UI_list = [self.prmanToolsRibEdit_wid.oldRoot_LE, self.prmanToolsRibEdit_wid.newRoot_LE]
        self.save_UI_list = ribEdit_save_UI_list
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


class prmanToolsLighting_ui(QtWidgets.QWidget, prmanToolsLighting_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsLighting_ui, self).__init__(parent)
        self.setupUi(self)
        self.currentRL = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        self.infoBar_label.setText('Current renderLayer : '+self.currentRL)
        self.timer_status = QtCore.QTimer()
        self.timer_status.start(400)
        self.connectInterface()

    def connectInterface(self):
        self.addSubD_PB.clicked.connect(self.addSubD_PB_hit)
        self.deleteSubD_PB.clicked.connect(self.delSubD_PB_hit)
        self.motionVectorSetting_PB.clicked.connect(self.motionVectorSetting_PB_hit)
        self.aoSettings_PB.clicked.connect(self.aoSettings_PB_hit)
        self.creatMatteID_PB.clicked.connect(self.creatMatteID_PB_hit)
        self.pxrMatteID_toShaders_PB.clicked.connect(self.pxrMatteID_toShaders_PB_hit)
        self.checkLights_PB.clicked.connect(self.checkLights_PB_hit)
        self.beautySettings_PB.clicked.connect(self.beautySettings_PB_hit)
        self.denoiseSettings_PB.clicked.connect(self.denoiseSettings_PB_hit)
        self.timer_status.timeout.connect(self.updateRenderLayer)

    def pxrMatteID_toShaders_PB_hit(self):
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

    def delSubD_PB_hit(self):
        u'''刪除選中的mesh的subD'''
        selList = pm.selected()
        for i in selList:
            if pm.attributeQuery('rman__torattr___subdivScheme', node=i.getShape(), ex=True):
                pm.deleteAttr(i.getShape(), at='rman__torattr___subdivScheme')
            else:
                pass
            if pm.attributeQuery('rman__torattr___subdivFacevaryingInterp', node=i.getShape(), ex=True):
                pm.deleteAttr(i.getShape(), at='rman__torattr___subdivFacevaryingInterp')
            else:
                pass

    def addSubD_PB_hit(self):
        selList = pm.selected()
        for i in selList:
            shape_name = i.getShape()
            if pm.attributeQuery('rman__torattr___subdivScheme', node=shape_name, ex=True) == False:
                addSubDAttrCmd = "rmanExecAEMenuCmd %s " % shape_name+'"Subdiv Scheme"'
                pm.mel.eval(addSubDAttrCmd)
            else:
                pass

    def motionVectorSetting_PB_hit(self):
        self.createOutput('dPdtime')

        if pm.attributeQuery('rman__riopt__Hider_samplemotion', node='rmanFinalGlobals', ex=True) == False:
            cmds = 'rmanAddAttr rmanFinalGlobals rman__riopt__Hider_samplemotion ""'
            pm.mel.eval(cmds)
            pm.setAttr("rmanFinalGlobals.rman__riopt__Hider_samplemotion", 1)

        currentRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        if currentRL != 'defaultRenderLayer':
            pm.editRenderLayerAdjustment('renderManRISGlobals.rman__torattr___motionBlur')
            pm.setAttr("renderManRISGlobals.rman__torattr___motionBlur", 1)
            pm.editRenderLayerAdjustment('renderManRISGlobals.rman__torattr___cameraBlur')
            pm.setAttr("renderManRISGlobals.rman__torattr___cameraBlur", 1)
            pm.editRenderLayerAdjustment('dPdtime_output.rman__torattr___computeBehavior')
            pm.setAttr("dPdtime_output.rman__torattr___computeBehavior", 1)
            pm.editRenderLayerAdjustment('rmanFinalGlobals.rman__riopt__Hider_samplemotion')
            pm.setAttr("rmanFinalGlobals.rman__riopt__Hider_samplemotion", 0)

    def aoSettings_PB_hit(self):
        pm.editRenderLayerAdjustment('renderManRISGlobals.rman__riopt__Integrator_name')
        pm.setAttr("renderManRISGlobals.rman__riopt__Integrator_name", "PxrOcclusion")
        pm.setAttr("PxrOcclusion.numSamples", 16)
        pm.setAttr("PxrOcclusion.cosineSpread", 0.8)
        pm.setAttr("PxrOcclusion.maxDistance", 20)

        self.createOutput('z')
        self.createOutput('__Nworld')
        self.createOutput('__Pworld')
        self.createOutput('__depth')
        currentRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        if currentRL != 'defaultRenderLayer':
            pm.editRenderLayerAdjustment('z_output.rman__torattr___computeBehavior')
            pm.setAttr("z_output.rman__torattr___computeBehavior", 1)
            pm.editRenderLayerAdjustment('__Nworld_output.rman__torattr___computeBehavior')
            pm.setAttr("__Nworld_output.rman__torattr___computeBehavior", 1)
            pm.editRenderLayerAdjustment('__Pworld_output.rman__torattr___computeBehavior')
            pm.setAttr("__Pworld_output.rman__torattr___computeBehavior", 1)
            pm.editRenderLayerAdjustment('__depth_output.rman__torattr___computeBehavior')
            pm.setAttr("__depth_output.rman__torattr___computeBehavior", 1)

    def beautySettings_PB_hit(self):
        self.checkLights_PB_hit()
        if self.currentRL != 'defaultRenderLayer':
            for light in self.light_in_RL_list:
                node_lightGrp = pm.getAttr(light+'.lightGroup')
                if node_lightGrp != '':
                    self.createOutputBeauty(node_lightGrp)
                    pm.editRenderLayerAdjustment("beauty_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("beauty_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)

    def denoiseSettings_PB_hit(self):
        pm.setAttr("defaultRenderGlobals.outFormatControl", 0)
        pm.setAttr("defaultRenderGlobals.animation", 1)
        pm.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)
        pm.setAttr("defaultRenderGlobals.periodInExt", 1)
        pm.setAttr("defaultRenderGlobals.extensionPadding", 4)

        self.checkLights_PB_hit()
        if self.currentRL != 'defaultRenderLayer':
            pm.editRenderLayerAdjustment('renderManRISGlobals.rman__torattr___denoise')
            pm.setAttr("renderManRISGlobals.rman__torattr___denoise", 1)
            for light in self.light_in_RL_list:
                node_lightGrp = pm.getAttr(light+'.lightGroup')
                if node_lightGrp != '':
                    self.createOutputDirectDiffuse(node_lightGrp)
                    self.createOutputIndirectDiffuse(node_lightGrp)
                    self.createOutputDirectSpecular(node_lightGrp)
                    self.createOutputIndirectSpecular(node_lightGrp)
                    self.createOutputSubsurface(node_lightGrp)
                    self.createOutputTransmissive(node_lightGrp)
                    self.createOutputDirectDiffuse(node_lightGrp)
                    pm.editRenderLayerAdjustment("directDiffuse_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("directDiffuse_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
                    pm.editRenderLayerAdjustment("indirectDiffuse_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("indirectDiffuse_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
                    pm.editRenderLayerAdjustment("directSpecular_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("directSpecular_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
                    pm.editRenderLayerAdjustment("indirectSpecular_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("indirectSpecular_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
                    pm.editRenderLayerAdjustment("subsurface_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("subsurface_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
                    pm.editRenderLayerAdjustment("transmissive_"+node_lightGrp+'_output.rman__torattr___computeBehavior')
                    pm.setAttr("transmissive_"+node_lightGrp+"_output.rman__torattr___computeBehavior", 1)
        try:
            cmds = 'rmanSetComputeBehavior '+'"rmanDenoiseGlobals" 0'
            pm.mel.eval(cmds)
        except:
            pass

    def createOutputDirectDiffuse(self, name):
        name_output = 'directDiffuse_'+name+'_output'
        create_name = 'color directDiffuse_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<RD>[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutputIndirectDiffuse(self, name):
        name_output = 'indirectDiffuse_'+name+'_output'
        create_name = 'color indirectDiffuse_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<RD>[DS]+[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutputDirectSpecular(self, name):
        name_output = 'directSpecular_'+name+'_output'
        create_name = 'color directSpecular_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<RS>[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutputIndirectSpecular(self, name):
        name_output = 'indirectSpecular_'+name+'_output'
        create_name = 'color indirectSpecular_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<RS>[DS]+[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutputSubsurface(self, name):
        name_output = 'subsurface_'+name+'_output'
        create_name = 'color subsurface_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<TD>[DS]*[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutputTransmissive(self, name):
        name_output = 'transmissive_'+name+'_output'
        create_name = 'color transmissive_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C<TS>[DS]*[<L.'"+name+"'>O]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def createOutput(self, name):
        name_output = name+'_output'
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)

    def createOutputBeauty(self, name):
        name_output = 'beauty_'+name+'_output'
        create_name = 'color beauty_'+name
        if pm.objExists(name_output) == False:
            cmds = 'rmanAddOutput rmanFinalGlobals '+'"'+create_name+'"'
            output = pm.mel.eval(cmds)
            cmds = 'rename %s ' % output+'"'+name_output+'"'
            pm.mel.eval(cmds)
            pm.setAttr(name_output+".rman__torattr___computeBehavior", 0)
            node_list = pm.listHistory("rmanFinalGlobals", pdo=True, lf=False, il=2)
            channel_node = node_list[-1].name()
            print channel_node
            source_value = '"'+"color lpe:C\[DS\]*\[<L.'"+name+"'>O\]"+'"'
            cmds = 'rmanAddAttr '+'"'+channel_node+'" '+'"rman__riopt__DisplayChannel_source" '+source_value
            pm.mel.eval(cmds)

    def creatMatteID_PB_hit(self):
        max_num = self.matteNum_SB.value()
        num_list = range(int(max_num)+1)
        for num in num_list:
            self.optionalMatteIDAttr(num)

    def optionalMatteIDAttr(self, num):
        settingsR = 'matte'+str(num)+'_R'
        settingsG = 'matte'+str(num)+'_G'
        settingsB = 'matte'+str(num)+'_B'
        attr = 'MatteID'+str(num)

        if pm.objExists(settingsR) == False:
            geo_settingsR = pm.mel.eval('rmanCreateAttrNode("kGeometric")')
            geo_settingsR = cmds.rename(geo_settingsR, settingsR)
            gui_hint_cmds = 'rmanGetGUIHint %s rman__riattr__user_%s ' % (settingsR, attr)+'"description"'
            pm.mel.eval(gui_hint_cmds)
            create_attr_cmds = 'rmanAddAttr %s rman__riattr__user_%s ' % (settingsR, attr)+'""'
            pm.mel.eval(create_attr_cmds)
            pm.setAttr(settingsR+'.rman__riattr__user_'+attr, 1, 0, 0, type="double3")

        if pm.objExists(settingsG) == False:
            geo_settingsG = pm.mel.eval('rmanCreateAttrNode("kGeometric")')
            geo_settingsG = cmds.rename(geo_settingsG, settingsG)
            gui_hint_cmds = 'rmanGetGUIHint %s rman__riattr__user_%s ' % (settingsG, attr)+'"description"'
            pm.mel.eval(gui_hint_cmds)
            create_attr_cmds = 'rmanAddAttr %s rman__riattr__user_%s ' % (settingsG, attr)+'""'
            pm.mel.eval(create_attr_cmds)
            pm.setAttr(settingsG+'.rman__riattr__user_'+attr, 0, 1, 0, type="double3")

        if pm.objExists(settingsB) == False:
            geo_settingsB = pm.mel.eval('rmanCreateAttrNode("kGeometric")')
            geo_settingsB = cmds.rename(geo_settingsB, settingsB)
            gui_hint_cmds = 'rmanGetGUIHint %s rman__riattr__user_%s ' % (settingsB, attr)+'"description"'
            pm.mel.eval(gui_hint_cmds)
            create_attr_cmds = 'rmanAddAttr %s rman__riattr__user_%s ' % (settingsB, attr)+'""'
            pm.mel.eval(create_attr_cmds)
            pm.setAttr(settingsB+'.rman__riattr__user_'+attr, 0, 0, 1, type="double3")

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        return False

    def withoutNum(self, name):
        while self.is_number(name[-1:len(name)]):
            numMax = len(name)
            name = name[0:numMax-1]
        return name

    def getTransforms(self, node):
        if cmds.nodeType(node) != 'transform':
            transforms = cmds.listRelatives(node, f=True, parent=True)[0]
            return transforms
        return False

    def updateRenderLayer(self):
        new_RL = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        if new_RL != self.currentRL:
            self.currentRL = new_RL
            self.infoBar_label.setText('Current renderLayer : '+self.currentRL)
            self.checkLights_PB_hit()

    def rmanLightList(self):
        rman_light_name_list = ['PxrDistantLight', 'PxrDomeLight', 'PxrRectLight', 'PxrMeshLight', 'PxrDiskLight']
        light_inScene_list = []
        for name in rman_light_name_list:
            light_list = cmds.ls(type=name)
            light_inScene_list.extend(light_list)
        light_inScene_list.sort()
        return light_inScene_list

    def checkInRL(self, pxrLightShape):
        u'''確認是否在當前render_layer裡面'''
        if self.currentRL == 'defaultRenderLayer':
            return False
        membersList = cmds.editRenderLayerMembers(self.currentRL, fn=True, query=True)
        if membersList != None:
            trans_node = self.getTransforms(pxrLightShape)
            if trans_node in membersList:
                return True
        return False

    def checkLights_PB_hit(self):

        self.currentRL = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        self.infoBar_label.setText('Current renderLayer : '+self.currentRL)
        self.clearLayout(self.lightCheck_layout)

        if self.currentRL != 'defaultRenderLayer':
            rman_light_list = self.rmanLightList()
            self.light_in_RL_list = []
            for light in rman_light_list:
                if self.checkInRL(light) == True:
                    self.light_in_RL_list.append(light)

            node_list_widget = QtWidgets.QWidget()
            node_list_layout = QtWidgets.QGridLayout()
            node_list_layout.setAlignment(QtCore.Qt.AlignLeft)
            node_list_layout.setContentsMargins(0, 0, 0, 0)
            node_list_widget.setLayout(node_list_layout)
            self.lightCheck_layout.addWidget(node_list_widget)

            top_name_label = QtWidgets.QLabel('Light Name')
            top_name_label.setStyleSheet("font: bold;")
            node_list_layout.addWidget(top_name_label, 0, 0)

            top_intensity_label = QtWidgets.QLabel('Intensity')
            top_intensity_label.setStyleSheet("font: bold;")
            node_list_layout.addWidget(top_intensity_label, 0, 1)

            top_exposure_label = QtWidgets.QLabel('Exposure')
            top_exposure_label.setStyleSheet("font: bold;")
            node_list_layout.addWidget(top_exposure_label, 0, 2)

            top_light_sample_label = QtWidgets.QLabel('Light Sample')
            top_light_sample_label.setStyleSheet("font: bold;")
            node_list_layout.addWidget(top_light_sample_label, 0, 3)

            top_light_grp_label = QtWidgets.QLabel('Light Group')
            top_light_grp_label.setStyleSheet("font: bold;")
            node_list_layout.addWidget(top_light_grp_label, 0, 4)

            for num, light in enumerate(self.light_in_RL_list):
                node_name = name_label_class(light)
                node_list_layout.addWidget(node_name, num+1, 0)
                node_intensity = attr_edit_class(light, 'intensity')
                node_list_layout.addWidget(node_intensity, num+1, 1)
                node_exposure = attr_edit_class(light, 'exposure')
                node_list_layout.addWidget(node_exposure, num+1, 2)
                node_lightSample = attr_edit_class(light, 'fixedSampleCount')
                node_list_layout.addWidget(node_lightSample, num+1, 3)
                node_lightGroup = attr_edit_unicode_class(light, 'lightGroup')
                node_list_layout.addWidget(node_lightGroup, num+1, 4)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.lightCheck_layout.addSpacerItem(self.spacerItem)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())


class name_label_class(QtWidgets.QLabel):
    def __init__(self, nodeShape):
        '''建立有滑鼠觸發功能的label'''
        self.nodeShape = nodeShape
        QtWidgets.QLabel.__init__(self)
        node = pm.PyNode(self.nodeShape)
        self.setText(node.nodeName())

    def mousePressEvent(self, e):
        node_trans = self.getTransforms(self.nodeShape)
        cmds.select(node_trans)

    def leaveEvent(self, e):
        self.setStyleSheet("font:;color: rgb(255, 255, 255);")

    def enterEvent(self, e):
        self.setStyleSheet("font: bold;color: rgb(0, 255, 0);")

    def getTransforms(self, node):
        if cmds.nodeType(node) != 'transform':
            transforms = cmds.listRelatives(node, f=True, parent=True)[0]
            return transforms
        return False


class attr_edit_unicode_class(QtWidgets.QLineEdit):
    def __init__(self, nodeShape, attr):
        self.nodeShape = nodeShape
        self.attr = attr
        QtWidgets.QLineEdit.__init__(self)
        attr_value = pm.getAttr(self.nodeShape+'.'+self.attr)
        self.setText(str(attr_value))
        self.textEdited.connect(self.text_hit)

    def text_hit(self):
        new_value = self.text()
        cmds.setAttr(self.nodeShape+'.'+self.attr, new_value, type='string')


class attr_edit_class(QtWidgets.QLineEdit):
    def __init__(self, nodeShape, attr):
        self.attr = attr
        self.nodeShape = nodeShape
        QtWidgets.QLineEdit.__init__(self)
        attr_value = pm.getAttr(self.nodeShape+'.'+self.attr)
        self.setText(str(attr_value))
        self.reg_ex = QtCore.QRegExp("[0-9]+")
        self.text_validator = QtGui.QRegExpValidator(self.reg_ex, self)
        self.setValidator(self.text_validator)
        self.textEdited.connect(self.text_hit)
        self.value_type = type(attr_value)

    def text_hit(self):
        new_value = self.text()
        if self.value_type == type(1.0):
            cmds.setAttr(self.nodeShape+'.'+self.attr, float(new_value))
        elif self.value_type == type(1):
            cmds.setAttr(self.nodeShape+'.'+self.attr, int(new_value))

##################################################################################################################


class prmanToolsShaderRename_ui(QtWidgets.QWidget, prmanToolsShaderRename_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsShaderRename_ui, self).__init__(parent)
        self.setupUi(self)

        self.connectInterface()

    def connectInterface(self):
        self.shadeNode_PB.clicked.connect(self.shadeNode_PB_hit)
        self.shadeNodePreview_PB.clicked.connect(self.shadeNodePreview_PB_hit)
        self.run_rename_PB.clicked.connect(self.run_rename_PB_hit)

    def shadeNode_PB_hit(self):
        # 刪除列表
        self.clearLayout(self.shaderNodesList_layout)

        self.node_list = cmds.ls(selection=True, ap=True)
        self.node_list.sort()
        obj_node_num = len(self.node_list)
        text_label = QtWidgets.QLabel('Total ' + str(obj_node_num) + ' node(s) are selected')
        self.shaderNodesList_layout.addWidget(text_label)

        for i in self.node_list:
            nodeList_wid_class_add = nodeList_wid_class(i)
            self.shaderNodesList_layout.addWidget(nodeList_wid_class_add)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.shaderNodesList_layout.addSpacerItem(self.spacerItem)

    def shadeNodePreview_PB_hit(self):
        self.clearLayout(self.shaderNodesList_layout)

        get_name = self.renema_LE.text()
        obj_node_num = len(self.node_list)
        text_label = QtWidgets.QLabel('Total ' + str(obj_node_num) + ' node(s) are selected')
        self.shaderNodesList_layout.addWidget(text_label)

        for i in self.node_list:
            nodeList_wid_class_add = preview_nodeList_wid_class(i, get_name)
            self.shaderNodesList_layout.addWidget(nodeList_wid_class_add)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.shaderNodesList_layout.addSpacerItem(self.spacerItem)

    def run_rename_PB_hit(self):
        get_name = self.renema_LE.text()
        for i in self.node_list:
            node_type = cmds.nodeType(i)
            cmds.rename(i, get_name+'_'+node_type)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())


class nodeList_wid_class(QtWidgets.QWidget):
    def __init__(self, objNode):
        self.objNode = objNode
        # 定義UI
        QtWidgets.QWidget.__init__(self)
        self.OutsideLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        # 定義路徑欄UI
        node_type = cmds.nodeType(self.objNode)
        self.obj_founded_label = QtWidgets.QLabel(str(self.objNode)+'  ('+node_type+')')
        self.layout().addWidget(self.obj_founded_label)


class preview_nodeList_wid_class(QtWidgets.QWidget):
    def __init__(self, objNode, name):
        self.objNode = objNode
        self.name = name
        # 定義UI
        QtWidgets.QWidget.__init__(self)
        self.OutsideLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        # 定義路徑欄UI
        node_type = cmds.nodeType(self.objNode)
        self.obj_founded_label = QtWidgets.QLabel(str(self.objNode)+'  ('+node_type+')')
        self.obj_rename_label = QtWidgets.QLabel('----> '+str(self.name)+'_'+node_type)
        self.layout().addWidget(self.obj_founded_label)
        self.layout().addWidget(self.obj_rename_label)

##################################################################################################################


class prmanToolsRibEdit_ui(QtWidgets.QWidget, prmanToolsRibEdit_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsRibEdit_ui, self).__init__(parent)
        self.setupUi(self)
        username = getpass.getuser()
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/prmanToolsRibEdit.csv'
        self.connectInterface()
        self.save_UI_list = [self.oldRoot_LE, self.newRoot_LE]
        self.setFromCsv()

    def connectInterface(self):
        self.oldRootBro_PB.clicked.connect(self.oldRootBro_PB_hit)
        self.oldRootOpen_PB.clicked.connect(self.oldRootOpen_PB_hit)
        self.newRootBro_PB.clicked.connect(self.newRootBro_PB_hit)
        self.newRootOpen_PB.clicked.connect(self.newRootOpen_PB_hit)
        self.substituteRib_PB.clicked.connect(self.substituteRib_PB_hit)
        self.substituteGpuCache_PB.clicked.connect(self.substituteGpuCache_PB_hit)
        self.ribShapeRename_PB.clicked.connect(self.ribShapeRename_PB_hit)
        self.ribFrameFix_PB.clicked.connect(self.ribFrameFix_PB_hit)

    def writeCsv(self):
        if os.path.exists(self.python_temp) is False:
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

    def retrieve_name(self, var):
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]

    def getValue(self, widget):
        if type(widget) == QtWidgets.QLineEdit:
            return widget.text()

    def oldRootOpen_PB_hit(self):
        path = self.oldRoot_LE.text()
        path = path.replace('/', '\\')
        os.startfile(path)

    def oldRootBro_PB_hit(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory != '':
            directory = directory.replace('\\', '/')
            self.oldRoot_LE.setText(directory)

    def newRootOpen_PB_hit(self):
        path = self.newRoot_LE.text()
        path = path.replace('/', '\\')
        os.startfile(path)

    def newRootBro_PB_hit(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory != '':
            directory = directory.replace('\\', '/')
            self.newRoot_LE.setText(directory)

    def substituteRib_PB_hit(self):
        rib_list = pm.ls(type='RenderManArchive', dag=True)
        for i in rib_list:
            path = pm.getAttr(i+'.filename')
            new_path = self.go_replace(path)
            pm.setAttr(i+'.filename', new_path, type="string")

    def substituteGpuCache_PB_hit(self):
        rib_list = pm.ls(type='gpuCache', dag=True)
        for i in rib_list:
            path = pm.getAttr(i+'.cacheFileName')
            new_path = self.go_replace(path)
            pm.setAttr(i+'.cacheFileName', new_path, type="string")

    def go_replace(self, path):
        path = path.replace('\\', '/')
        print 'path '+path
        old_path = self.oldRoot_LE.text()
        old_path = old_path.replace('\\', '/')
        print 'old_path '+old_path
        new_path = self.newRoot_LE.text()
        new_path = new_path.replace('\\', '/')
        print 'new_path '+new_path
        pathChanged = path.replace(old_path, new_path)
        print 'replaced '+pathChanged
        return pathChanged

    def ribFrameFix_PB_hit(self):
        if pm.objExists('global_timeUC'):
            print 'global_UC already exists'
        else:
            pm.shadingNode('timeToUnitConversion', au=True, n='global_timeUC')
            pm.setAttr("global_timeUC.conversionFactor", 0.004)
            pm.connectAttr('time1.outTime', 'global_timeUC.input', f=True)
        rib_list = []
        node_list = pm.ls(sl=True)
        for node in node_list:
            shape = node.getShape()
            if shape.type() == 'RenderManArchive':
                rib_list.append(shape)
        for rib in rib_list:
            pm.connectAttr('global_timeUC.output', rib+'.frame', f=True)

    def ribShapeRename_PB_hit(self):
        rib_list = cmds.ls(type='RenderManArchive', long=True)
        transform_list = []
        for i in rib_list:
            trans = self.getTransforms(i)
            transform_list.append(trans)

        name_list = []
        for i in transform_list:
            node = pm.PyNode(i)
            new_name = self.withoutNum(node.nodeName())
            if new_name not in name_list:
                name_list.append(new_name)

        node_rename_list = []
        for i in name_list:
            node_dic = {}
            node_dic['name'] = i
            node_dic['nodes'] = []
            node_dic['total'] = 0
            node_rename_list.append(node_dic)

        for i in transform_list:
            node = pm.PyNode(i)
            new_name = self.withoutNum(node.nodeName())
            for num, i in enumerate(node_rename_list):
                if new_name == i['name']:
                    node_rename_list[num]['nodes'].append(node.name())
                    node_rename_list[num]['total'] = node_rename_list[num]['total']+1

        for i in node_rename_list:
            if i['total'] > 1:
                for num, node in enumerate(i['nodes']):
                    four_num = "%04d" % (num+1)
                    new_name = i['name']+four_num
                    cmds.rename(node, new_name)

    def getTransforms(self, node):
        if cmds.nodeType(node) != 'transform':
            transforms = cmds.listRelatives(node, f=True, parent=True)[0]
            return transforms
        return False

    def withoutNum(self, name):
        while self.is_number(name[-1:len(name)]):
            numMax = len(name)
            name = name[0:numMax-1]
        return name

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        return False
##################################################################################################################


class prmanToolsTexureEdit_ui(QtWidgets.QWidget, prmanToolsTexureEdit_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsTexureEdit_ui, self).__init__(parent)
        self.setupUi(self)
        self.texture_info_treeWidget.header().resizeSection(0, 500)
        self.texture_info_treeWidget.header().resizeSection(1, 100)
        self.texture_info_treeWidget.header().resizeSection(2, 50)
        current_workspace = cmds.workspace(q=True, rd=True)
        self.project_LE.setText(current_workspace+'sourceimages')
        self.connectInterface()

    def connectInterface(self):
        print
        self.anlyse_PB.clicked.connect(self.anlyse_PB_hit)
        self.substitute_PB.clicked.connect(self.substitute_PB_hit)
        self.expanded_all_PB.clicked.connect(self.expanded_all_PB_hit)
        self.expanded_off_PB.clicked.connect(self.expanded_off_PB_hit)
        self.select_all_PB.clicked.connect(self.select_all_PB_hit)
        self.select_clean_PB.clicked.connect(self.select_clean_PB_hit)
        self.texture_info_treeWidget.itemChanged.connect(self.treeWidgetItem_changed)
        self.texture_info_treeWidget.itemClicked.connect(self.treeWidgetItem_hit)

    def listDirs(self):
        pxrNodes = cmds.ls(type='PxrTexture')
        fileNodes = cmds.ls(type='file')
        textureNode_list = pxrNodes+fileNodes
        fileName_list = []
        for node in textureNode_list:
            file_name = self.getFileName(node)
            fileName_list.append(file_name)
        return fileName_list, textureNode_list

    def getFileName(self, node):
        if cmds.nodeType(node) == 'file':
            return cmds.getAttr(node+'.fileTextureName')
        if cmds.nodeType(node) == 'PxrTexture':
            return cmds.getAttr(node+'.filename')

    def setFileName(self, node, value):
        if cmds.nodeType(node) == 'file':
            cmds.setAttr(node+'.fileTextureName', value, type='string')
        if cmds.nodeType(node) == 'PxrTexture':
            cmds.setAttr(node+'.filename', value, type='string')

    def fixDirs(self, path):
        pathDirs = []
        for i in path:
            if os.path.dirname(i) not in pathDirs:
                pathDirs.append(os.path.dirname(i))
        return pathDirs

    def checkExists(self, node, path):
        if cmds.nodeType(node) == 'PxrTexture':
            if '_MAPID_' in path:
                num = cmds.getAttr(node+'.atlasStyle')
                if num == 1:
                    path = path.replace('_MAPID_', '1001')
                if num == 2:
                    path = path.replace('_MAPID_', 'u1_v1')
                if num == 3:
                    path = path.replace('_MAPID_', 'u0_v0')

        currentProj = cmds.workspace(q=True, rd=True)
        if path[0:12] == 'sourceimages':
            path = currentProj+path
        path = path.replace('/', '\\')
        return os.path.exists(path)

    def grpDirs(self):
        u'''整理成一個List'''
        pathGrp = []
        fileName_list, textureNodes = self.listDirs()
        fixDirsR = self.fixDirs(fileName_list)
        for index, path in enumerate(fixDirsR):
            path_dict = {}
            path_dict['path'] = path
            path_dict['used'] = []
            path_dict['exists'] = []
            path_dict['notExists'] = []
            for index2, path2 in enumerate(fileName_list):
                if os.path.dirname(path2) == path:
                    path_dict['used'].append(textureNodes[index2])
                    if self.checkExists(textureNodes[index2], path2):
                        path_dict['exists'].append(textureNodes[index2])
                    else:
                        path_dict['notExists'].append(textureNodes[index2])
            pathGrp.append(path_dict)
        return pathGrp

    def anlyse_PB_hit(self):
        u'''創建內嵌式列表'''
        # self.texture_info_treeWidget.clear()
        self.deleteTreeItem(self.texture_info_treeWidget)
        self.checked_node = []
        self.path_info_big_data = self.grpDirs()
        self.top_tree_item = []
        for index, path_dict in enumerate(self.path_info_big_data):
            pathTreeItem = pathTreeItem_class(self, path_dict)
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

    def select_all_PB_hit(self):
        for item in self.top_tree_item:
            item.setCheckState(0, QtCore.Qt.Checked)

    def select_clean_PB_hit(self):
        for item in self.top_tree_item:
            item.setCheckState(0, QtCore.Qt.Unchecked)
            number = item.childCount()
            for i in range(number):
                item.child(i).setCheckState(0, QtCore.Qt.Unchecked)

    def treeWidgetItem_changed(self, item, column):
        item_index = self.texture_info_treeWidget.indexOfTopLevelItem(item)
        childred_list = []
        if item_index == -1:
            if item.text(0) == 'exists':
                number = item.childCount()
                for i in range(number):
                    node = item.child(i).text(0)
                    childred_list.append(node)
            elif item.text(0) == 'notExists':
                number = item.childCount()
                for i in range(number):
                    node = item.child(i).text(0)
                    childred_list.append(node)
            else:
                node = item.text(0)
                childred_list.append(node)
        elif item_index >= 0:
            node_list = self.path_info_big_data[item_index]['used']
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

    def treeWidgetItem_hit(self, item, column):
        item_index = self.texture_info_treeWidget.indexOfTopLevelItem(item)
        if item_index == -1:
            if item.text(0) == 'exists':
                childred_list = []
                number = item.childCount()
                for i in range(number):
                    node = item.child(i).text(0)
                    childred_list.append(node)
                pm.select(childred_list, r=True)
            elif item.text(0) == 'notExists':
                childred_list = []
                number = item.childCount()
                for i in range(number):
                    node = item.child(i).text(0)
                    childred_list.append(node)
                pm.select(childred_list, r=True)
            else:
                pm.select(item.text(0), r=True)

        if item_index >= 0:
            node_list = self.path_info_big_data[item_index]['used']
            pm.select(node_list, r=True)

    def substitute_PB_hit(self):
        # pm.undoInfo(ock=True)

        for node in self.checked_node:
            path = self.getFileName(node)
            pathChanged = self.replace(path)
            print pathChanged
            self.setFileName(node, pathChanged)
        # pm.undoInfo(cck=True)
        time.sleep(1)
        self.anlyse_PB_hit()

    def replace(self, path):
        u'''路徑替換'''
        oldPath = self.old_root_LE.text()
        newPath = self.new_root_LE.text()
        path = path.replace('\\', '/')
        oldPath = oldPath.replace('\\', '/')
        newPath = newPath.replace('\\', '/')
        pathChanged = path.replace(oldPath, newPath)
        return pathChanged

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

    def deleteTreeItem(self, tree):
        while tree.topLevelItemCount():
            item = tree.takeTopLevelItem(0)


class pathTreeItem_class(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, path_dict):
        self.parent = parent
        self.path_dict = path_dict
        QtWidgets.QTreeWidgetItem.__init__(self)
        used_num = len(self.path_dict['used'])
        self.setText(0, str(used_num)+" texture(s) point to "+self.path_dict['path'])
        self.setCheckState(0, QtCore.Qt.Unchecked)
        self.item_exists = QtWidgets.QTreeWidgetItem(['exists'])
        self.item_exists.setCheckState(0, QtCore.Qt.Unchecked)
        self.item_notExists = QtWidgets.QTreeWidgetItem(['notExists'])
        self.item_notExists.setCheckState(0, QtCore.Qt.Unchecked)
        self.addChild(self.item_exists)
        self.addChild(self.item_notExists)
        if len(self.path_dict['notExists']) > 0:
            self.setForeground(0, QtGui.QColor('red'))
            self.item_notExists.setForeground(0, QtGui.QColor('red'))
        for node in self.path_dict['exists']:
            self.createChild(node, self.item_exists)
        for node in self.path_dict['notExists']:
            self.createChild(node, self.item_notExists)

    def createChild(self, node, parent):
        filename = self.parent.getFileName(node)
        basename = os.path.basename(filename)
        ext = os.path.splitext(basename)[1]
        node_item = QtWidgets.QTreeWidgetItem([node])
        node_item.setText(1, basename)
        node_item.setText(2, self.checkMultipleUV(node))
        node_item.setText(3, cmds.nodeType(node))
        # node_item.setCheckState(0,QtCore.Qt.Unchecked)
        parent.addChild(node_item)

    def checkMultipleUV(self, node):
        if cmds.nodeType(node) == 'file':
            num = cmds.getAttr(node+'.uvTilingMode')
            if num == 1:
                return 'ZBrush'
            elif num == 2:
                return 'Mudbox'
            elif num == 3:
                return 'Mari'
            else:
                return ''

        elif cmds.nodeType(node) == 'PxrTexture':
            num = cmds.getAttr(node+'.atlasStyle')
            if num == 1:
                return 'Mari'
            elif num == 2:
                return 'Mudbox'
            elif num == 3:
                return 'ZBrush'
            return ''


##################################################################################################################
class prmanToolsDelUnuse_ui(QtWidgets.QWidget, prmanToolsDelUnuse_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsDelUnuse_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()

    def connectInterface(self):
        self.analyse_PB.clicked.connect(self.analyse_PB_hit)
        self.setAllOn_PB.clicked.connect(self.setAllOn_PB_hit)
        self.setAllOff_PB.clicked.connect(self.setAllOff_PB_hit)
        self.selectNode_PB.clicked.connect(self.selectNode_PB_hit)
        self.deleteNode_PB.clicked.connect(self.deleteNode_PB_hit)

    def pxrNodeList(self):
        u'''搜尋所有pxrNode'''
        mat_ist = pm.ls(mat=True)
        tex_ist = pm.ls(tex=True)
        nodeList = mat_ist+tex_ist
        pxrNodeList = []
        for i in nodeList:
            if i.nodeType()[0:3] == 'Pxr':
                pxrNodeList.append(i)
        return pxrNodeList

    def loopDelNode(self, node_list):
        unused_node_list = []
        while len(self.checkTopAll(node_list, unused_node_list)) > 0:
            for node in node_list:
                if self.topNodeCheck(node, unused_node_list) is True:
                    unused_node_list.append(node)
                    node_list.remove(node)
        return unused_node_list

    def checkTopAll(self, node_list, unused_node_list):
        unused_node_new_list = []
        for node in node_list:
            if self.topNodeCheck(node, unused_node_list) is True:
                unused_node_new_list.append(node)
        return unused_node_new_list

    def topNodeCheck(self, node, unuseNode_list):
        connectNodeList_original = pm.listConnections(node, s=0)
        connectNodeList = []
        for node in connectNodeList_original:
            if node not in connectNodeList:
                connectNodeList.append(node)
        for node in connectNodeList:
            if pm.nodeType(node) == 'nodeGraphEditorInfo':
                connectNodeList.remove(node)
            elif pm.nodeType(node) == 'defaultTextureList':
                connectNodeList.remove(node)

        for node in unuseNode_list:
            if node in connectNodeList:
                connectNodeList.remove(node)

        if len(connectNodeList) == 0:
            return True
        else:
            return False

    def analyse_PB_hit(self):
        self.clearLayout(self.nodeCheck_layout)
        pxrNodeList = self.pxrNodeList()
        unused_node_list = self.loopDelNode(pxrNodeList)

        pxrNodesNum = len(unused_node_list)
        allNode_Label = QtWidgets.QLabel('Total ' + str(pxrNodesNum) + ' pxrNode(s) are unused')
        self.nodeCheck_layout.addWidget(allNode_Label)

        self.pxrNode_CB_list = []
        for node in unused_node_list:
            pxrNode_CB = QtWidgets.QCheckBox(node.name())
            self.pxrNode_CB_list.append(pxrNode_CB)
            self.nodeCheck_layout.addWidget(pxrNode_CB)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.nodeCheck_layout.addSpacerItem(self.spacerItem)

    def selectNode_PB_hit(self):
        u'''點擊選擇按鈕觸發'''
        self.deleteNodeList = []
        for CB in self.pxrNode_CB_list:
            if CB.checkState():
                self.deleteNodeList.append(CB.text())
        pm.select(self.deleteNodeList)

    def setAllOn_PB_hit(self):
        for CB in self.pxrNode_CB_list:
            CB.setChecked(True)

    def setAllOff_PB_hit(self):
        for CB in self.pxrNode_CB_list:
            CB.setChecked(False)

    def deleteNode_PB_hit(self):
        u'''點擊刪除按鈕觸發'''
        self.deleteNodeList = []
        for CB in self.pxrNode_CB_list:
            if CB.checkState():
                self.deleteNodeList.append(CB.text())
        pm.undoInfo(ock=True)
        pm.delete(self.deleteNodeList)
        pm.undoInfo(cck=True)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())


##################################################################################################################
class prmanToolsDelUnknow_ui(QtWidgets.QWidget, prmanToolsDelUnknow_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(prmanToolsDelUnknow_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()

    def connectInterface(self):
        self.analyseUnknowNodes_PB.clicked.connect(self.analyseUnknowNodes_PB_hit)
        self.analyseUnknowPlugins_PB.clicked.connect(self.analyseUnknowPlugins_PB_hit)
        self.setAllOn_PB.clicked.connect(self.setAllOn_PB_hit)
        self.setAllOff_PB.clicked.connect(self.setAllOff_PB_hit)
        self.selectNode_PB.clicked.connect(self.selectNode_PB_hit)
        self.deleteNode_PB.clicked.connect(self.deleteNode_PB_hit)

    def analyseUnknowNodes_PB_hit(self):
        self.delete_node = "unknowNodes"
        self.clearLayout(self.nodeCheck_layout)
        unknown_node_list = pm.ls(type='unknown')
        node_num = len(unknown_node_list)
        all_node_Label = QtWidgets.QLabel('Total ' + str(node_num) + ' unknowNode(s) are unused')
        self.nodeCheck_layout.addWidget(all_node_Label)

        self.node_CB_list = []
        for node in unknown_node_list:
            node_CB = QtWidgets.QCheckBox(node.name())
            self.node_CB_list.append(node_CB)
            self.nodeCheck_layout.addWidget(node_CB)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.nodeCheck_layout.addSpacerItem(self.spacerItem)

    def analyseUnknowPlugins_PB_hit(self):
        self.delete_node = "unknowPlugins"
        self.clearLayout(self.nodeCheck_layout)
        unknownPlugin_list = pm.unknownPlugin(q=True, list=True)
        if unknownPlugin_list is None:
            node_num = 0
            all_node_Label = QtWidgets.QLabel('Total ' + str(node_num) + ' unknowPlugin(s) are unused')
            self.nodeCheck_layout.addWidget(all_node_Label)
            self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.nodeCheck_layout.addSpacerItem(self.spacerItem)
        else:
            node_num = len(unknownPlugin_list)
            all_node_Label = QtWidgets.QLabel('Total ' + str(node_num) + ' unknowPlugin(s) are unused')
            self.nodeCheck_layout.addWidget(all_node_Label)
            self.node_CB_list = []
            for node in unknownPlugin_list:
                node_CB = QtWidgets.QCheckBox(node)
                self.node_CB_list.append(node_CB)
                self.nodeCheck_layout.addWidget(node_CB)
            self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.nodeCheck_layout.addSpacerItem(self.spacerItem)

    def selectNode_PB_hit(self):
        u'''點擊選擇按鈕觸發'''
        self.deleteNodeList = []
        for CB in self.node_CB_list:
            if CB.checkState():
                self.deleteNodeList.append(CB.text())
        pm.select(self.deleteNodeList)

    def setAllOn_PB_hit(self):
        for CB in self.node_CB_list:
            CB.setChecked(True)

    def setAllOff_PB_hit(self):
        for CB in self.node_CB_list:
            CB.setChecked(False)

    def deleteNode_PB_hit(self):
        u'''點擊刪除按鈕觸發'''
        self.deleteNodeList = []
        for CB in self.node_CB_list:
            if CB.checkState():
                self.deleteNodeList.append(CB.text())
        pm.undoInfo(ock=True)
        if self.delete_node == "unknowNodes":
            if len(self.deleteNodeList) > 0:
                for node in self.deleteNodeList:
                    pm.lockNode(node, lock=False)
                    pm.delete(node)
                    print 'deleting: ' + node
        elif self.delete_node == "unknowPlugins":
            if len(self.deleteNodeList) > 0:
                for plugin in self.deleteNodeList:
                    pm.unknownPlugin(plugin, remove=True)
                    print 'deleting: ' + plugin
        pm.undoInfo(cck=True)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

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


def prmanToolsMain():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()
