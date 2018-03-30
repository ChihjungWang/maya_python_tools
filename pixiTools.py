# -*- coding: utf-8 -*-
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import maya.cmds as cmds
import pymel.core as pm
import maya.OpenMaya as om
import json
import os
import getpass
import csv
import sys
import math
import random

maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
py27_lib = 'C:/Python27/Lib/site-packages'
sys.path.append(py27_lib)
sys.path.append(ui_path)
# sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
from PIL import Image
import pixiTools_export_json_ui
reload(pixiTools_export_json_ui)
import pixiTools_export_spine_json_ui
reload(pixiTools_export_spine_json_ui)
dialog = None


# ------------------------------------------------------------------------------------
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('pixi tools'+' v0.5'+u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800, 600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0, 0, 0, 0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.pixiTools_export_json_wid = pixiTools_export_json_ui()
        self.pixiTools_export_spine_json_wid = pixiTools_export_spine_json_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.pixiTools_export_json_wid, "Export Pixi Json")
        main_tab_Widget.addTab(self.pixiTools_export_spine_json_wid, "Export Spine Json")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/pixiTools.csv'
        self.python_temp_json = self.python_temp+'/pixiTools.json'
        self.layout().addWidget(main_tab_Widget)
        self.save_UI_list = [
            self.pixiTools_export_json_wid.objGrp_LE,
            self.pixiTools_export_json_wid.instanceGrp_LE,
            self.pixiTools_export_json_wid.sourceCam_LE,
            self.pixiTools_export_json_wid.canvasCam_LE,
            self.pixiTools_export_json_wid.outDir_LE,
            self.pixiTools_export_json_wid.json_LE,
            self.pixiTools_export_json_wid.textureMode_01_RB,
            self.pixiTools_export_json_wid.textureMode_02_RB,
            self.pixiTools_export_json_wid.textureMode_03_RB,
            self.pixiTools_export_json_wid.scale_CB,
            self.pixiTools_export_json_wid.rotation_CB,
            self.pixiTools_export_json_wid.zdepth_CB,
            self.pixiTools_export_json_wid.cropBroders_CB,
            self.pixiTools_export_spine_json_wid.canvasCam_LE,
            self.pixiTools_export_spine_json_wid.outDir_LE,
            self.pixiTools_export_spine_json_wid.json_LE,
            self.pixiTools_export_spine_json_wid.textureMode_01_RB,
            self.pixiTools_export_spine_json_wid.textureMode_02_RB,
            self.pixiTools_export_spine_json_wid.textureMode_03_RB,
            self.pixiTools_export_spine_json_wid.scale_CB,
            self.pixiTools_export_spine_json_wid.rotation_CB,
            self.pixiTools_export_spine_json_wid.zdepth_CB,
            self.pixiTools_export_spine_json_wid.nums_LE,
            self.pixiTools_export_spine_json_wid.textureFile_LE,
            self.pixiTools_export_spine_json_wid.rootJoint_LE,
            self.pixiTools_export_spine_json_wid.aniModeNormal_RB,
            self.pixiTools_export_spine_json_wid.aniModeOffsetLoop_RB
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
                    self.setValue(widget, value)

    def setValue(self, widget, value):
        wid_type = type(widget)
        if wid_type == QtWidgets.QLineEdit:
            widget.setText(value)
        elif wid_type == QtWidgets.QRadioButton:
            widget.setChecked(value)
        elif wid_type == QtWidgets.QCheckBox:
            widget.setChecked(value)

    def getValue(self, widget):
        widget_type = type(widget)
        if widget_type == QtWidgets.QLineEdit:
            return widget.text()
        elif widget_type == QtWidgets.QRadioButton:
            return widget.isChecked()
        elif widget_type == QtWidgets.QCheckBox:
            return widget.isChecked()

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


class pixiTools_export_json_ui(QtWidgets.QWidget, pixiTools_export_json_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(pixiTools_export_json_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        self.setDefault()
        self.info_label.setText("waiting ~~")
        regx = QtCore.QRegExp("[0-9]+$")
        self.onlyInt = QtGui.QRegExpValidator(regx)
        self.createPlaneW_LE.setValidator(self.onlyInt)
        self.createPlaneH_LE.setValidator(self.onlyInt)
        self.frameRangeStart_LE.setValidator(self.onlyInt)
        self.frameRangeEnd_LE.setValidator(self.onlyInt)
        self.frameRangeStep_LE.setValidator(self.onlyInt)
        self.sourceSizeW_LE.setValidator(self.onlyInt)
        self.sourceSizeH_LE.setValidator(self.onlyInt)

    def connectInterface(self):
        self.exportJson_PB.clicked.connect(self.exportJson_PB_hit)
        self.outDirBro_PB.clicked.connect(self.outDirBro_PB_hit)
        self.outDirOpen_PB.clicked.connect(self.outDirOpen_PB_hit)
        self.createPlane_PB.clicked.connect(self.createPlane_PB_hit)
        self.sourceCamSetUp_PB.clicked.connect(self.sourceCamSetUp_PB_hit)
        self.canvasCamSetUp_PB.clicked.connect(self.canvasCamSetUp_PB_hit)
        self.shaderSetToDefault_PB.clicked.connect(self.shaderSetToDefault_PB_hit)
        self.frameRangeTime_CB.currentIndexChanged.connect(self.frameRangeTime_CB_hit)
        self.objGrpPick_PB.clicked.connect(self.objGrpPick_PB_hit)
        self.instanceGrpPick_PB.clicked.connect(self.instanceGrpPick_PB_hit)
        self.convertSimpleJson_PB.clicked.connect(self.convertSimpleJson_PB_hit)

    def setDefault(self):
        # width = cmds.getAttr("defaultResolution.width")
        # height = cmds.getAttr("defaultResolution.height")
        # self.sourceSizeW_LE.setText(str(width))
        # self.sourceSizeH_LE.setText(str(height))
        time = cmds.currentUnit(q=True, time=True)
        if time == "film":
            self.frameRangeTime_CB.setCurrentIndex(0)
        elif time == "ntsc":
            self.frameRangeTime_CB.setCurrentIndex(1)
        elif time == "ntscf":
            self.frameRangeTime_CB.setCurrentIndex(2)
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        self.frameRangeStart_LE.setText(str(min_frame))
        self.frameRangeEnd_LE.setText(str(max_frame))

    def objGrpPick_PB_hit(self):
        grp = cmds.ls(selection=True, tail=True, allPaths=True)[0]
        self.objGrp_LE.setText(grp)
        self.reSetRenderLayer('source_RL', grp)
        self.sourceCamSetUp_PB_hit()

    def instanceGrpPick_PB_hit(self):
        grp = cmds.ls(selection=True, tail=True, allPaths=True)[0]
        self.instanceGrp_LE.setText(grp)
        self.reSetRenderLayer('canvas_RL', grp)
        self.canvasCamSetUp_PB_hit()

    def reSetRenderLayer(self, rlName, objGrp):
        if pm.objExists(rlName) is False:
            cmds.createRenderLayer(name=rlName, e=True, mc=True)
        member_list = cmds.editRenderLayerMembers(rlName, fullNames=True, query=True)
        print member_list
        if member_list is not None:
            if len(member_list) > 0:
                for member in member_list:
                    cmds.editRenderLayerMembers(rlName, member, remove=True)
        cmds.editRenderLayerMembers(rlName, objGrp)

    def bakeToObject_PB_hit(self):
        particleName = self.particleName_LE.text()
        f_min = int(self.frameRangeStart_LE.text())
        f_max = int(self.frameRangeEnd_LE.text())
        node_t = pm.PyNode(particleName)
        node_s = node.getShape()
        instancer = pm.particleInstancer(node_t, q=True, name=True)[0]
        mesh_list = pm.listConnections(instancer.inputHierarchy, s=True)
        totalParticle = pm.nParticle(node, query=True, count=True)
        pId_list = []
        object_list = []
        for f in xrange(f_min, f_max+1):
            totalParticle = pm.nParticle(node, query=True, count=True)
            if totalParticle != 0:
                for pId in totalParticle:
                    '''
                    if 'customIndexPP:doubleArray' in pm.nParticle(node_t, q=True, dal=True):
                        index=cmds.nParticle(node_t, q=True, id=pId,attribute='customIndexPP')
                        index=int(index)
                    else:
                        index=0
                    '''
                    index = 0
                    if pid not in pId_list:
                        pId_list.append(pId)
                        object_list.append(pm.duplicate(mesh_list[index]))
                    tranform = cmds.particle(node_t, q=True, id=pid, attribute='position')
                    scale_range = cmds.nParticle(node_t, q=True, id=pId, attribute='customScalePP')

    def setResolution(self):
        width = int(self.sourceSizeW_LE.text())
        height = int(self.sourceSizeH_LE.text())
        # cmds.setAttr("defaultResolution.width", width)
        # cmds.setAttr("defaultResolution.height", height)

    def createPlane_PB_hit(self):
        width = int(self.createPlaneW_LE.text())
        height = int(self.createPlaneH_LE.text())
        image_plane = pm.polyPlane(n='baseImage_mesh')
        image_plane[1].setAttr('subdivisionsHeight', 1)
        image_plane[1].setAttr('subdivisionsWidth', 1)
        image_plane[0].setAttr("rotateX", 90)
        cmds.makeIdentity(image_plane[0].name(), apply=True, rotate=True)
        image_plane[0].setAttr("scaleX", width)
        image_plane[0].setAttr("scaleY", height)

    def sourceCamSetUp_PB_hit(self):
        width = float(self.sourceSizeW_LE.text())
        height = float(self.sourceSizeH_LE.text())
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        self.setCamera('sourceCam', width)
        self.setRenderLayer('source_RL')

    def canvasCamSetUp_PB_hit(self):
        width = float(self.canvasSizeW_LE.text())
        height = float(self.canvasSizeH_LE.text())
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        self.setCamera('canvasCam', width)
        self.setRenderLayer('canvas_RL')

    def setCamera(self, cameraName, width):
        if cameraName not in cmds.listCameras():
            camera = pm.camera()
            pm.rename(camera[0], cameraName)
        camera = pm.PyNode(cameraName)
        camera.setAttr("translateZ", 500)
        cameraShape = camera.getShape()
        cameraShape.setAttr("orthographic", 1)
        cameraShape.setAttr("orthographicWidth", width)
        cameraShape.setAttr("displayFilmGate", 0)
        cameraShape.setAttr("displayResolution", 1)
        cameraShape.setAttr("displayGateMask", 1)
        cameraShape.setAttr("overscan", 1.6)

    def setRenderLayer(self, rlName):
        if pm.objExists(rlName) is False:
            cmds.createRenderLayer(name=rlName, e=True, mc=True)
        pm.editRenderLayerGlobals(currentRenderLayer=rlName)

    def frameRangeTime_CB_hit(self, index):
        if index == 0:
            cmds.currentUnit(time='film')
        elif index == 1:
            cmds.currentUnit(time='ntsc')
        elif index == 2:
            cmds.currentUnit(time='ntscf')

    def outDirBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.outDir_LE.setText(path)

    def outDirOpen_PB_hit(self):
        json_path = self.outDir_LE.text()
        json_path = json_path.replace('/', '\\')
        os.startfile(json_path)

    def textureFileBro_PB_hit(self):
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        print file
        if file != "":
            self.textureFile_LE.setText(file)

    def textureFileOpen_PB_hit(self):
        file = self.textureFile_LE.text()
        path = os.path.split(file)[0]
        path = path.replace('/', '\\')
        os.startfile(path)

    def pointWorldToCam(self, cameraName, point, res):
        sel = om.MSelectionList()
        dag = om.MDagPath()
        sel.add(cameraName)
        sel.getDagPath(0, dag)
        cam = om.MFnCamera(dag)
        floatMat = cam.projectionMatrix()
        projMat = om.MMatrix(floatMat.matrix)
        floatMat = cam.postProjectionMatrix()
        postProjMat = om.MMatrix(floatMat.matrix)
        transMat = dag.inclusiveMatrix()
        point = om.MPoint(point[0], point[1], point[2])

        fullMat = transMat.inverse() * projMat * postProjMat
        nuPoint = point * fullMat
        return [(nuPoint[0]/nuPoint[3]/2+0.5)*res[0], (1-(nuPoint[1]/nuPoint[3]/2+0.5))*res[1]]

    def getParticlePositions(self, pObject, pId, start, end):
        cTime = cmds.currentTime(q=True)
        positions = {}
        fromStart = True
        for f in xrange(start, end+1):
            cmds.runup(maxFrame=f, fsf=fromStart)
            fromStart = False
            try:
                pos = cmds.particle(pObject, q=True, id=pId, attribute='position')
            except RuntimeError:
                pos = None
            frame = "%04d" % f
            positions[frame] = pos
        cmds.currentTime(cTime)
        return positions

    def showCounts(self, particle, start, end):
        fromStart = True
        count_list = []
        for f in xrange(start, end+1):
            cmds.runup(maxFrame=f, fsf=fromStart)
            fromStart = False
            count = cmds.nParticle(particle, count=True, q=True)
            count_list.append(count)
        return max(count_list)

    def createDict(self):
        source_width = int(self.sourceSizeW_LE.text())
        source_height = int(self.sourceSizeH_LE.text())
        canvas_width = int(self.canvasSizeW_LE.text())
        canvas_height = int(self.canvasSizeH_LE.text())
        source_camera = self.sourceCam_LE.text()
        canvas_camera = self.canvasCam_LE.text()
        f_min = int(self.frameRangeStart_LE.text())
        f_max = int(self.frameRangeEnd_LE.text())
        step = int(self.frameRangeStep_LE.text())
        final_dict = {}
        particle_dict = self.getParticleInfo(f_min, f_max, step, source_camera, source_width, source_height)
        isinstance_dict = self.getInstanceInfo(f_min, f_max, step, canvas_camera, canvas_width, canvas_height)
        meta_dict = self.getMetaData()
        final_dict.update(particle_dict)
        final_dict.update(isinstance_dict)
        final_dict.update(meta_dict)
        return final_dict

    def getParticleInfo(self, f_min, f_max, step, camera, width, height):
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        obj_grp = self.objGrp_LE.text()
        mesh_list = pm.listRelatives(obj_grp, ad=True, type='mesh')
        obj_list = []
        for mesh in mesh_list:
            obj_list.append(mesh.getTransform())
        particle_dict = {}
        for index, obj in enumerate(obj_list):
            particle_ID = str(index)
            particle_dict['pId_'+particle_ID] = {}
            particle_dict['pId_'+particle_ID]['translate'] = []
            particle_dict['pId_'+particle_ID]['rotate'] = []
            particle_dict['pId_'+particle_ID]['scale'] = []
            for f in xrange(f_min, f_max+1, step):
                cmds.currentTime(f)
                positionPP = cmds.getAttr(obj+'.translate')[0]
                visibility = cmds.getAttr(obj+'.visibility')
                camera_positon = self.pointWorldToCam(camera, positionPP, (width, height))
                file_index = self.getTextureInfo(obj.getShape())[1]
                file_alpha = self.getTextureInfo(obj.getShape())[2]
                file_image = self.getTextureInfo(obj.getShape())[3]
                if self.cropBroders_CB.isChecked():
                    file_alpha = self.boaderFalloff(camera_positon[0], camera_positon[1], file_alpha)
                if visibility is False:
                    file_alpha = 0
                particle_dict['pId_'+particle_ID]['translate'].append({
                    "time": f, "x": int(camera_positon[0]),
                    "y": int(camera_positon[1]),
                    "vis": visibility,
                    "trans": file_alpha,
                    "index": file_index,
                    "image": file_image
                })
                rotationPP = cmds.getAttr(obj+'.rotate')[0]
                rotation_z = int(rotationPP[2])
                if rotation_z < 0:
                    fix_angle = 360+(rotation_z % 360)
                else:
                    fix_angle = rotation_z % 360
                particle_dict['pId_'+particle_ID]['rotate'].append({"time": f, "angle": int(fix_angle)})
                scalePP = cmds.getAttr(obj+'.scale')[0]
                scale_w = int(scalePP[0])
                scale_h = int(scalePP[1])
                particle_dict['pId_'+particle_ID]['scale'].append({"time": f, "w": scale_w, "h": scale_h})
            cmds.currentTime(f_min)
            # angle = cmds.getAttr(obj+'.rotate')[0]
            # pivot = self.getPivot(obj, angle[2])
            pivot = self.getPivot2(obj)
            particle_dict['pId_'+particle_ID]['pivot_w'] = pivot[0]
            particle_dict['pId_'+particle_ID]['pivot_h'] = pivot[1]
        return particle_dict

    def getMetaData(self):
        data_dict = {}
        obj_grp = self.objGrp_LE.text()
        mesh_list = pm.listRelatives(obj_grp, ad=True, type='mesh')
        sequence = self.getTextureMode()
        instance_big_grp = self.instanceGrp_LE.text()
        transform_list = pm.listRelatives(instance_big_grp, ad=True, type='transform')
        instancer_grp_list = []
        for i in transform_list:
            if i.getShape() is None:
                instancer_grp_list.append(i)
        min_frame = cmds.playbackOptions(minTime=True, q=True)
        max_frame = cmds.playbackOptions(maxTime=True, q=True)
        data_dict['metaData'] = {}
        data_dict['metaData']['frame_start'] = int(min_frame)
        data_dict['metaData']['frame_end'] = int(max_frame)
        data_dict['metaData']['source_width'] = int(self.sourceSizeW_LE.text())
        data_dict['metaData']['source_height'] = int(self.sourceSizeH_LE.text())
        data_dict['metaData']['sequence'] = sequence
        data_dict['metaData']['particle_num'] = len(mesh_list)
        data_dict['metaData']['instancer_num'] = len(instancer_grp_list)
        data_dict['metaData']['canvas_width'] = int(self.canvasSizeW_LE.text())
        data_dict['metaData']['canvas_height'] = int(self.canvasSizeH_LE.text())
        return data_dict

    def getTextureInfo(self, meshShape):
        SG = pm.listConnections(meshShape, type='shadingEngine')[0]
        shader = pm.listConnections(SG.surfaceShader, d=False, s=True, type='lambert')[0]
        file = pm.listConnections(shader.color, d=False, s=True, type='file')[0]
        sequence = file.getAttr('useFrameExtension')
        alpha = file.getAttr('alphaGain')
        fileImage = file.getAttr('fileTextureName')
        basename = os.path.basename(fileImage)
        alpha = round(alpha, 2)
        if sequence is True:
            index = file.getAttr('frameExtension')
        else:
            index = None
        return sequence, index, alpha, basename, fileImage

    def getTextureMode(self):
        if self.textureMode_01_RB.isChecked():
            mode = "sequence"
        elif self.textureMode_02_RB.isChecked():
            mode = "multiImages"
        elif self.textureMode_03_RB.isChecked():
            mode = "singleImage"
        if mode == "sequence":
            return True
        else:
            return False

    def exportJson_PB_hit(self):
        self.info_label.setText("Doing")
        big_data = self.createDict()
        json_path = self.outDir_LE.text()
        json_path = json_path.replace('\\', '/')
        json_name = self.json_LE.text()
        if os.path.exists(json_path) is False:
            os.mkdir(json_path)
        json_file = json_path+"/"+json_name+".json"
        file2 = open(json_file, 'w')
        json.dump(big_data, file2, ensure_ascii=True, indent=4)
        file2.close()
        self.convertSimpleJson_PB_hit()
        self.info_label.setText("Done")

    def getInstanceInfo(self, f_min, f_max, step, camera, width, height):
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        instance_big_grp = self.instanceGrp_LE.text()
        transform_list = pm.listRelatives(instance_big_grp, type='transform')
        instancer_grp_list = []
        for i in transform_list:
            if i.getShape() is None:
                instancer_grp_list.append(i)
        final_dict = {}
        instance_dict = {}
        for index, instancer_grp in enumerate(instancer_grp_list):
            ID = str(index)
            instance_dict['instancer_'+ID] = {}
            instance_dict['instancer_'+ID]['translate'] = []
            instance_dict['instancer_'+ID]['rotate'] = []
            instance_dict['instancer_'+ID]['scale'] = []
            mesh_list = pm.listRelatives(instancer_grp, ad=True, type='mesh')
            print mesh_list
            abc_node = pm.listConnections(mesh_list[0].getTransform(), type='AlembicNode')
            if len(abc_node) > 0:
                offset = abc_node[0].getAttr('offset')
                instance_dict['instancer_'+ID]['offset'] = offset
            else:
                instance_dict['instancer_'+ID]['offset'] = 0
            for f in xrange(f_min, f_max+1, step):
                cmds.currentTime(f)
                positionPP = cmds.getAttr(instancer_grp+'.translate')[0]
                camera_positon = self.pointWorldToCam(camera, positionPP, (width, height))
                instance_dict['instancer_'+ID]['translate'].append({
                    "time": f,
                    "x": int(camera_positon[0]),
                    "y": int(camera_positon[1]),
                    "trans": 1
                })
                rotationPP = cmds.getAttr(instancer_grp+'.rotate')[0]
                rotation_z = int(rotationPP[2])
                if rotation_z < 0:
                    fix_angle = 360+(rotation_z % 360)
                else:
                    fix_angle = rotation_z % 360
                instance_dict['instancer_' + ID]['rotate'].append({"time": f, "angle": int(fix_angle)})
                scalePP = cmds.getAttr(instancer_grp+'.scale')[0]
                scale_w = round(scalePP[0], 2)
                scale_h = round(scalePP[1], 2)
                instance_dict['instancer_' + ID]['scale'].append({"time": f, "w": scale_w, "h": scale_h})
            bbox = self.getBoundBox(instancer_grp, f_min, f_max)
            print instancer_grp
            print bbox
            bbox_w = bbox[1]-bbox[0]
            bbox_h = bbox[3]-bbox[2]
            instance_dict['instancer_'+ID]['bbox_w'] = int(bbox_w)
            instance_dict['instancer_'+ID]['bbox_h'] = int(bbox_h)
            # cmds.currentTime(f_min)
            # angle = cmds.getAttr(instancer_grp+'.rotate')[0]
            # pivot = self.getGrpPivot(instancer_grp, angle[2])
            pivot = pm.xform(instancer_grp, query=True, pivots=True)
            instance_dict['instancer_'+ID]['pivot_w'] = int(pivot[0])
            instance_dict['instancer_'+ID]['pivot_h'] = 0-int(pivot[1])
        final_dict["instancer"] = instance_dict
        return final_dict

    def boaderFalloff(self, x, y, alpha):
        falloff_range = 0.15
        output_size_w = int(self.sourceSizeW_LE.text())
        output_size_h = int(self.sourceSizeH_LE.text())
        h_min = output_size_h*falloff_range
        w_min = output_size_w*falloff_range
        h_max = output_size_h-h_min
        w_max = output_size_w-w_min
        if x < w_min and x > 0:
            x_alpha = x/w_min
        elif x > w_max and x < output_size_w:
            x_alpha = 1-(x-w_max)/w_min
        elif x <= 0 or x >= output_size_w:
            x_alpha = 0
        else:
            x_alpha = 1
        if y < h_min and y > 0:
            y_alpha = y/h_min
        elif y > h_max and y < output_size_h:
            y_alpha = 1-(y-h_max)/h_min
        elif y <= 0 or y >= output_size_h:
            y_alpha = 0
        else:
            y_alpha = 1
        final_alpha = min([x_alpha, y_alpha])*alpha
        final_alpha = round(final_alpha, 2)
        return final_alpha

    def shaderSetToDefault_PB_hit(self):
        currentRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        trans_list = pm.ls(selection=True, type='transform', long=True)
        mesh_list = []
        for i in trans_list:
            if i.getShape().type() == "mesh":
                mesh_list.append(i)
        if currentRL != 'defaultRenderLayer':
            for mesh in mesh_list:
                SG = pm.listConnections(mesh.getShape(), type='shadingEngine')[0]
                pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
                pm.sets(SG, edit=True, forceElement=mesh)
                pm.editRenderLayerGlobals(currentRenderLayer=currentRL)

    def getPivot2(self, mesh):
        pivot = pm.xform(mesh, query=True, pivots=True)
        pivot_x = round(pivot[0]+0.5, 2)
        pivot_y = round(pivot[1]+0.5, 2)
        pivot = [pivot_x, pivot_y]
        return pivot

    def getPivot(self, mesh, angle):
        pivot, left_top_point, right_top_point, right_down_point, left_down_point = self.meshInfo(mesh)
        width = self.getDistance(left_top_point[0], left_top_point[1], right_top_point[0], right_top_point[1])
        height = self.getDistance(left_top_point[0], left_top_point[1], left_down_point[0], left_down_point[1])
        left_top_point = [left_top_point[0]-pivot[0], left_top_point[1]-pivot[1]]
        angle = 0-angle
        left_top_point = self.coordinateConversion(left_top_point[0], left_top_point[1], angle)
        # scale = cmds.getAttr(mesh+'.scale')[0]

        pivot_offset = [0-left_top_point[0], 0-left_top_point[1]]
        pivot_local_x = round(pivot_offset[0]/width, 2)
        pivot_local_y = round(pivot_offset[1]/height, 2)
        pivot_local = [pivot_local_x, 0-pivot_local_y]
        return pivot_local

    def getGrpPivot(self, grp, angle):
        grp = pm.PyNode(grp)
        position = [grp.getAttr('translateX'), grp.getAttr('translateY'), grp.getAttr('translateZ'), ]
        angle = 0-angle
        pivot = pm.xform(grp, query=True, pivots=True, worldSpace=True)
        pivot = [round(pivot[0], 2), round(pivot[1], 2)]
        position = [position[0]-pivot[0], position[1]-pivot[1]]
        position = self.coordinateConversion(position[0], position[1], angle)
        pivot_local_x = round(position[0], 2)
        pivot_local_y = round(position[1], 2)
        pivot_local = [pivot_local_x, 0-pivot_local_y]
        return pivot_local

    def meshInfo(self, mesh):
        uvs = pm.polyEvaluate(mesh, uv=True)
        for i in range(uvs):
            pos = cmds.polyEditUV(mesh + '.map['+str(i)+']', query=True)
            if pos == [0.0, 0.0]:
                left_down = mesh + '.map['+str(i)+']'
            elif pos == [1.0, 0.0]:
                right_down = mesh + '.map['+str(i)+']'
            elif pos == [0.0, 1.0]:
                left_top = mesh + '.map['+str(i)+']'
            elif pos == [1.0, 1.0]:
                right_top = mesh + '.map['+str(i)+']'

        left_top_vertex = cmds.polyListComponentConversion(left_top, tv=True)[0]
        left_top_point = cmds.pointPosition(left_top_vertex)
        left_top_point = [round(left_top_point[0]), round(left_top_point[1])]

        right_top_vertex = cmds.polyListComponentConversion(right_top, tv=True)[0]
        right_top_point = cmds.pointPosition(right_top_vertex)
        right_top_point = [round(right_top_point[0]), round(right_top_point[1])]

        right_down_vertex = cmds.polyListComponentConversion(right_down, tv=True)[0]
        right_down_point = cmds.pointPosition(right_down_vertex)
        right_down_point = [round(right_down_point[0]), round(right_down_point[1])]

        left_down_vertex = cmds.polyListComponentConversion(left_down, tv=True)[0]
        left_down_point = cmds.pointPosition(left_down_vertex)
        left_down_point = [round(left_down_point[0]), round(left_down_point[1])]
        pivot = pm.xform(mesh, query=True, pivots=True, worldSpace=True)
        pivot = [round(pivot[0], 2), round(pivot[1], 2)]

        return pivot, left_top_point, right_top_point, right_down_point, left_down_point

    def getDistance(self, p1x, p2x, p1y, p2y,):
        distance = ((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** 0.5
        return distance

    def coordinateConversion(self, x, y, angle):
        p1 = [x, y]
        angle = angle/(180/math.pi)
        p2_x = math.cos(angle)*p1[0]-math.sin(angle)*p1[1]
        p2_y = math.sin(angle)*p1[0]+math.cos(angle)*p1[1]
        p2 = [p2_x, p2_y]
        print p2_x, p2_y
        return p2

    def getBoundBox(self, grp, f_min, f_max):
        bbox_x = []
        bbox_y = []
        for f in xrange(f_min, f_max+1):
            cmds.currentTime(f)
            bbox = pm.exactWorldBoundingBox(grp)
            bbox_x.append(bbox[0])
            bbox_x.append(bbox[3])
            bbox_y.append(bbox[1])
            bbox_y.append(bbox[4])
        bbox_x_min = round(min(bbox_x), 2)
        bbox_x_max = round(max(bbox_x), 2)
        bbox_y_min = round(min(bbox_y), 2)
        bbox_y_max = round(max(bbox_y), 2)
        bbox = [bbox_x_min, bbox_x_max, bbox_y_min, bbox_y_max]
        return bbox

    def createBboxPlane(self, bbox):
        image_plane = pm.polyPlane(n='bbox_plane')
        image_plane[1].setAttr('subdivisionsHeight', 1)
        image_plane[1].setAttr('subdivisionsWidth', 1)
        image_plane[0].setAttr("rotateX", 90)
        pm.makeIdentity(image_plane[0].name(), apply=True, rotate=True)
        pm.xform(image_plane[0].vtx[0], t=[bbox[0], bbox[2], 0], worldSpace=True)
        pm.xform(image_plane[0].vtx[1], t=[bbox[1], bbox[2], 0], worldSpace=True)
        pm.xform(image_plane[0].vtx[2], t=[bbox[0], bbox[3], 0], worldSpace=True)
        pm.xform(image_plane[0].vtx[3], t=[bbox[1], bbox[3], 0], worldSpace=True)

    def convertSimpleJson_PB_hit(self):
        json_path = self.outDir_LE.text()
        json_name = self.json_LE.text()
        json_file = json_path+'/'+json_name+".json"
        file = open(json_file, "r")
        json_dict = json.load(file)
        file.close()
        particle_num = json_dict['metaData']['particle_num']
        instancer_num = json_dict['metaData']['instancer_num']
        frame_start = json_dict['metaData']['frame_start']
        frame_end = json_dict['metaData']['frame_end']

        particle_dict = {}
        for i in range(particle_num):
            pIdNum = "pId_"+str(i)
            base_data_list = []
            base_data_list.append(json_dict[pIdNum]['pivot_w'])
            base_data_list.append(json_dict[pIdNum]['pivot_h'])
            base_data_list.append(json_dict[pIdNum]['translate'][0]['index'])
            base_data_list.append(json_dict[pIdNum]['translate'][0]['vis'])
            particle_dict[pIdNum] = {}
            particle_dict[pIdNum]['base'] = base_data_list
            particle_dict[pIdNum]['dt'] = {}
            for i in xrange(frame_start, frame_end+1):
                num = i-frame_start
                x = json_dict[pIdNum]['translate'][num]['x']
                y = json_dict[pIdNum]['translate'][num]['y']
                trans = json_dict[pIdNum]['translate'][num]['trans']
                angle = json_dict[pIdNum]['rotate'][num]['angle']
                w = json_dict[pIdNum]['scale'][num]['w']
                h = json_dict[pIdNum]['scale'][num]['h']
                dt_data = []
                dt_data.append(x)
                dt_data.append(y)
                dt_data.append(trans)
                dt_data.append(angle)
                dt_data.append(w)
                dt_data.append(h)
                particle_dict[pIdNum]['dt'][str(i)] = dt_data

        instance_dict = {}
        for i in range(instancer_num):
            instanceNum = "instancer_"+str(i)
            instance_dict[instanceNum] = {}
            base_data_list = []
            base_data_list.append(json_dict['instancer'][instanceNum]['bbox_w'])
            base_data_list.append(json_dict['instancer'][instanceNum]['bbox_h'])
            base_data_list.append(json_dict['instancer'][instanceNum]['pivot_w'])
            base_data_list.append(json_dict['instancer'][instanceNum]['pivot_h'])
            base_data_list.append(json_dict['instancer'][instanceNum]['offset'])
            instance_dict[instanceNum] = {}
            instance_dict[instanceNum]['base'] = base_data_list
            instance_dict[instanceNum]['dt'] = {}
            for i in xrange(frame_start, frame_end+1):
                num = i-frame_start
                x = json_dict['instancer'][instanceNum]['translate'][num]['x']
                y = json_dict['instancer'][instanceNum]['translate'][num]['y']
                trans = json_dict['instancer'][instanceNum]['translate'][num]['trans']
                angle = json_dict['instancer'][instanceNum]['rotate'][num]['angle']
                w = json_dict['instancer'][instanceNum]['scale'][num]['w']
                h = json_dict['instancer'][instanceNum]['scale'][num]['h']
                dt_data = []
                dt_data.append(x)
                dt_data.append(y)
                dt_data.append(trans)
                dt_data.append(angle)
                dt_data.append(w)
                dt_data.append(h)
                instance_dict[instanceNum]['dt'][str(i)] = dt_data
        final_data = {}
        final_data.update(particle_dict)
        final_data.update(instance_dict)
        final_data['metaData'] = json_dict['metaData']
        json_simple_file = json_path+"/"+json_name+"_simple.json"
        file2 = open(json_simple_file, 'w')
        # json.dump(final_data, file2, ensure_ascii=True, sort_keys=True, indent=4)
        json.dump(final_data, file2, ensure_ascii=True, sort_keys=True)
        file2.close()

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


class pixiTools_export_spine_json_ui(QtWidgets.QWidget, pixiTools_export_spine_json_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(pixiTools_export_spine_json_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        self.setDefault()
        self.info_label.setText("waiting ~~")
        regx = QtCore.QRegExp("[0-9]+$")
        self.onlyInt = QtGui.QRegExpValidator(regx)
        self.createPlaneW_LE.setValidator(self.onlyInt)
        self.createPlaneH_LE.setValidator(self.onlyInt)
        self.frameRangeStart_LE.setValidator(self.onlyInt)
        self.frameRangeEnd_LE.setValidator(self.onlyInt)
        self.frameRangeStep_LE.setValidator(self.onlyInt)
        self.nums_LE.setValidator(self.onlyInt)

    def connectInterface(self):
        self.outDirBro_PB.clicked.connect(self.outDirBro_PB_hit)
        self.outDirOpen_PB.clicked.connect(self.outDirOpen_PB_hit)
        self.textureFileBro_PB.clicked.connect(self.textureFileBro_PB_hit)
        self.textureFileOpen_PB.clicked.connect(self.textureFileOpen_PB_hit)
        self.createPlane_PB.clicked.connect(self.createPlane_PB_hit)
        self.canvasCamSetUp_PB.clicked.connect(self.canvasCamSetUp_PB_hit)
        self.shaderSetToDefault_PB.clicked.connect(self.shaderSetToDefault_PB_hit)
        self.frameRangeTime_CB.currentIndexChanged.connect(self.frameRangeTime_CB_hit)
        self.autoRename_PB.clicked.connect(self.autoRename_PB_hit)
        self.planeEditFixSize_PB.clicked.connect(self.planeEditFixSize_PB_hit)
        self.createLambert_PB.clicked.connect(self.createLambert_PB_hit)
        self.rootJointPick_PB.clicked.connect(self.rootJointPick_PB_hit)
        self.exportJsonSpine_PB.clicked.connect(self.exportJsonSpine_PB_hit)

    def setDefault(self):
        time = cmds.currentUnit(q=True, time=True)
        if time == "film":
            self.frameRangeTime_CB.setCurrentIndex(0)
        elif time == "ntsc":
            self.frameRangeTime_CB.setCurrentIndex(1)
        elif time == "ntscf":
            self.frameRangeTime_CB.setCurrentIndex(2)
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        self.frameRangeStart_LE.setText(str(min_frame))
        self.frameRangeEnd_LE.setText(str(max_frame))

    def getSelectMeshList(self):
        mesh_list = []
        selected_list = pm.ls(selection=True, allPaths=True)
        for obj in selected_list:
            shape = obj.getShape()
            shape_type = pm.objectType(shape)
            if shape_type == "mesh":
                mesh_list.append(obj)
        return mesh_list

    def autoRename_PB_hit(self):
        node = pm.ls(sl=True, tail=True)[0]
        new_name = self.autoRename_LE.text()
        self.reNameChild(node, new_name, '')

    def reNameChild(self, root_node, new_name, new_num):
        children_list = pm.listRelatives(root_node, children=True)
        if len(children_list) > 0:
            for num, child in enumerate(children_list):
                node_type = child.type()
                new_num = new_num+'_'+str(num)
                set_new_name = new_name+'_'+new_num+'_'+node_type
                pm.rename(child, set_new_name)
                self.reNameChild(child, new_name, new_num)

    def planeEditFixSize_PB_hit(self):
        mesh_list = self.getSelectMeshList()
        for mesh in mesh_list:
            meshShape = mesh.getShape()
            filePath = self.getTextureInfo(meshShape)[4]
            if filePath[0:12] == 'sourceimages':
                current_workspace = cmds.workspace(q=True, rd=True)
                filePath = current_workspace+filePath
            im = Image.open(filePath)
            width, height = im.size
            mesh.setAttr('scaleX', lock=False)
            mesh.setAttr('scaleY', lock=False)
            mesh.setAttr('scaleX', width)
            mesh.setAttr('scaleY', height)
            mesh.setAttr('scaleX', lock=True)
            mesh.setAttr('scaleY', lock=True)

    def rootJointPick_PB_hit(self):
        root = cmds.ls(selection=True, tail=True, allPaths=True)[0]
        self.rootJoint_LE.setText(root)

    def reSetRenderLayer(self, rlName, objGrp):
        if pm.objExists(rlName) is False:
            cmds.createRenderLayer(name=rlName, e=True, mc=True)
        member_list = cmds.editRenderLayerMembers(rlName, fullNames=True, query=True)
        print member_list
        if member_list is not None:
            if len(member_list) > 0:
                for member in member_list:
                    cmds.editRenderLayerMembers(rlName, member, remove=True)
        cmds.editRenderLayerMembers(rlName, objGrp)

    def createLambert_PB_hit(self):
        mesh_list = self.getSelectMeshList()
        for mesh in mesh_list:
            second_joint = pm.listRelatives(mesh, fullPath=True, parent=True)[0]
            lambert_shader = pm.shadingNode('lambert', n="baseImage_lambert", asShader=True)
            shading_group = cmds.sets(name='baseImage_SG', renderable=True, noSurfaceShader=True, empty=True)
            pm.connectAttr(lambert_shader+'.outColor', shading_group+'.surfaceShader')
            pm.select(clear=True)
            pm.select(mesh)
            pm.hyperShade(assign=shading_group)
            file_node = pm.shadingNode('file', n='baseImage_file', asTexture=True, isColorManaged=True)
            texture_file = self.textureFile_LE.text()
            file_node.setAttr('fileTextureName', texture_file, type='string')
            pm.connectAttr(file_node+'.outColor', lambert_shader+'.color')
            pm.connectAttr(file_node+'.outTransparency', lambert_shader+'.transparency')
            pm.connectAttr(second_joint+'.alphaGain', file_node+'.alphaGain')
            pm.connectAttr(second_joint+'.colorGainR', file_node+'.colorGainR')
            pm.connectAttr(second_joint+'.colorGainG', file_node+'.colorGainG')
            pm.connectAttr(second_joint+'.colorGainB', file_node+'.colorGainB')

        for mesh in mesh_list:
            meshShape = mesh.getShape()
            filePath = self.getTextureInfo(meshShape)[4]
            if filePath[0:12] == 'sourceimages':
                current_workspace = cmds.workspace(q=True, rd=True)
                filePath = current_workspace+filePath
            im = Image.open(filePath)
            width, height = im.size
            mesh.setAttr('scaleX', lock=False)
            mesh.setAttr('scaleY', lock=False)
            mesh.setAttr('scaleX', width)
            mesh.setAttr('scaleY', height)
            mesh.setAttr('scaleX', lock=True)
            mesh.setAttr('scaleY', lock=True)

    def setResolution(self):
        width = int(self.sourceSizeW_LE.text())
        height = int(self.sourceSizeH_LE.text())
        # cmds.setAttr("defaultResolution.width", width)
        # cmds.setAttr("defaultResolution.height", height)

    def createPlane_PB_hit(self):
        pm.select(clear=True)
        root_joint = pm.joint(name="root_joint", p=[0, 0, 0])
        pm.select(clear=True)
        width = int(self.createPlaneW_LE.text())
        height = int(self.createPlaneH_LE.text())
        joint_nums = int(self.nums_LE.text())
        for num in range(joint_nums):
            image_plane = pm.polyPlane(n='baseImage_mesh')
            image_plane[1].setAttr('subdivisionsHeight', 1)
            image_plane[1].setAttr('subdivisionsWidth', 1)
            image_plane[0].setAttr("rotateX", 90)
            cmds.makeIdentity(image_plane[0].name(), apply=True, rotate=True)
            image_plane[0].setAttr("scaleX", width)
            image_plane[0].setAttr("scaleY", height)
            image_plane[0].setAttr('scaleX', lock=True)
            image_plane[0].setAttr('scaleY', lock=True)
            image_plane[0].setAttr('scaleZ', lock=True)
            image_plane[0].setAttr('translateX', keyable=False, channelBox=True)
            image_plane[0].setAttr('translateY', keyable=False, channelBox=True)
            image_plane[0].setAttr('translateZ', keyable=False, channelBox=True)
            image_plane[0].setAttr('rotateX', keyable=False, channelBox=True)
            image_plane[0].setAttr('rotateY', keyable=False, channelBox=True)
            image_plane[0].setAttr('rotateZ', keyable=False, channelBox=True)
            image_plane[0].setAttr('visibility', keyable=False, channelBox=True)
            pm.select(clear=True)
            second_joint = pm.joint(name="second_joint", p=[0, 0, 0])
            cmds.addAttr(longName='alphaGain', defaultValue=1.0, minValue=0, maxValue=1, keyable=True)
            cmds.addAttr(longName='colorGain', usedAsColor=True, attributeType='float3', keyable=True)
            cmds.addAttr(longName='colorGainR', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainG', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainB', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='blendMode', attributeType="enum", enumName="normal:multiply:additive:screen", keyable=True)
            cmds.addAttr(longName='startFrame', defaultValue=1, attributeType="long", keyable=True)
            pm.parent(second_joint, root_joint, relative=True)
            pm.parent(image_plane[0], second_joint, relative=True)

    def getBlendMode(self, bone):
        index = bone.getAttr('blendMode')
        if index is 0:
            return 'normal'
        elif index is 1:
            return 'multiply'
        elif index is 2:
            return 'additive'
        elif index is 3:
            return 'screen'

    def canvasCamSetUp_PB_hit(self):
        width = float(self.canvasSizeW_LE.text())
        height = float(self.canvasSizeH_LE.text())
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        self.setCamera('canvasCam', width)
        self.setRenderLayer('canvas_RL')

    def setCamera(self, cameraName, width):
        if cameraName not in cmds.listCameras():
            camera = pm.camera()
            pm.rename(camera[0], cameraName)
        camera = pm.PyNode(cameraName)
        camera.setAttr("translateZ", 500)
        cameraShape = camera.getShape()
        cameraShape.setAttr("orthographic", 1)
        cameraShape.setAttr("orthographicWidth", width)
        cameraShape.setAttr("displayFilmGate", 0)
        cameraShape.setAttr("displayResolution", 1)
        cameraShape.setAttr("displayGateMask", 1)
        cameraShape.setAttr("overscan", 1.6)

    def setRenderLayer(self, rlName):
        if pm.objExists(rlName) is False:
            cmds.createRenderLayer(name=rlName, e=True, mc=True)
        pm.editRenderLayerGlobals(currentRenderLayer=rlName)

    def frameRangeTime_CB_hit(self, index):
        if index == 0:
            cmds.currentUnit(time='film')
        elif index == 1:
            cmds.currentUnit(time='ntsc')
        elif index == 2:
            cmds.currentUnit(time='ntscf')

    def outDirBro_PB_hit(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = path.replace('\\', '/')
        if path != "":
            self.outDir_LE.setText(path)

    def outDirOpen_PB_hit(self):
        json_path = self.outDir_LE.text()
        json_path = json_path.replace('/', '\\')
        os.startfile(json_path)

    def textureFileBro_PB_hit(self):
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        if file != "":
            self.textureFile_LE.setText(file)

    def textureFileOpen_PB_hit(self):
        file = self.textureFile_LE.text()
        path = os.path.split(file)[0]
        path = path.replace('/', '\\')
        os.startfile(path)

    def getTextureInfo(self, meshShape):
        SG = pm.listConnections(meshShape, type='shadingEngine')[0]
        shader = pm.listConnections(SG.surfaceShader, d=False, s=True, type='lambert')[0]
        file = pm.listConnections(shader.color, d=False, s=True, type='file')[0]
        sequence = file.getAttr('useFrameExtension')
        alpha = file.getAttr('alphaGain')
        fileImage = file.getAttr('fileTextureName')
        basename = os.path.basename(fileImage)
        alpha = round(alpha, 2)
        if sequence is True:
            index = file.getAttr('frameExtension')
        else:
            index = None
        return sequence, index, alpha, basename, fileImage

    def getTextureMode(self):
        if self.textureMode_01_RB.isChecked():
            mode = "sequence"
        elif self.textureMode_02_RB.isChecked():
            mode = "multiImages"
        elif self.textureMode_03_RB.isChecked():
            mode = "singleImage"
        if mode == "sequence":
            return True
        else:
            return False

    def shaderSetToDefault_PB_hit(self):
        currentRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        trans_list = pm.ls(selection=True, type='transform', long=True)
        mesh_list = []
        for i in trans_list:
            if i.getShape().type() == "mesh":
                mesh_list.append(i)
        if currentRL != 'defaultRenderLayer':
            for mesh in mesh_list:
                SG = pm.listConnections(mesh.getShape(), type='shadingEngine')[0]
                pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
                pm.sets(SG, edit=True, forceElement=mesh)
                pm.editRenderLayerGlobals(currentRenderLayer=currentRL)

    def getAllBones(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        bone_info_list = []
        bone_list = []
        bone_list = self.checkNodeChild(root_joint, bone_list, 'joint')
        for bone in bone_list:
            x = round(bone.getAttr('translateX'), 2)
            y = round(bone.getAttr('translateY'), 2)
            r = round(bone.getAttr('rotateZ'), 2)
            scaleX = round(bone.getAttr('scaleX'), 2)
            scaleY = round(bone.getAttr('scaleY'), 2)
            attr_list = ['translateX', 'translateY']
            self.setAttrSameKey(bone, attr_list)
            attr_list = ['scaleX', 'scaleY']
            self.setAttrSameKey(bone, attr_list)
            bone_dict = {
                "name": bone.nodeName(),
                "rotation": 0,
                "x": 0,
                "y": 0,
                "scaleX": 1,
                "scaleY": 1
            }
            bone_parent = pm.listRelatives(bone, p=True)
            if len(bone_parent) > 0:
                bone_dict["parent"] = bone_parent[0].nodeName()
            bone_info_list.append(bone_dict)
        return bone_info_list

    def checkNodeChild(self, root_node, export_list, node_type):
        export_list.append(root_node)
        children_list = pm.listRelatives(root_node, children=True, type=node_type)
        if len(children_list) > 0:
            for child in children_list:
                self.checkNodeChild(child, export_list, node_type)
        return export_list

    def colorConvert16(self, value):
        if value >= 1:
            value_B = 255
        elif value <= 0:
            value_B = 0
        else:
            value_B = int(value*255)
        value16bit = hex(value_B)
        value16_str = value16bit[2:len(value16bit)]
        while len(value16_str) < 2:
            value16_str = "0" + value16_str
        return value16_str

    def setRgbaSameKey(self, second_joint):
        r_key_list = pm.keyframe(second_joint, attribute='colorGainR', query=True, cp=False)
        g_key_list = pm.keyframe(second_joint, attribute='colorGainG', query=True, cp=False)
        b_key_list = pm.keyframe(second_joint, attribute='colorGainB', query=True, cp=False)
        a_key_list = pm.keyframe(second_joint, attribute='alphaGain', query=True, cp=False)
        all_key_list = r_key_list+g_key_list+b_key_list+a_key_list
        all_key_list = list(set(all_key_list))
        for key in all_key_list:
            cmds.currentTime(key)
            r_value = second_joint.getAttr('colorGainR')
            pm.setKeyframe(second_joint, attribute='colorGainR', t=key, v=r_value)
            g_value = second_joint.getAttr('colorGainG')
            pm.setKeyframe(second_joint, attribute='colorGainG', t=key, v=g_value)
            b_value = second_joint.getAttr('colorGainB')
            pm.setKeyframe(second_joint, attribute='colorGainG', t=key, v=b_value)
            a_value = second_joint.getAttr('alphaGain')
            pm.setKeyframe(second_joint, attribute='alphaGain', t=key, v=a_value)

    def setAttrSameKey(self, obj, attr_list):
        key_list = []
        for attr in attr_list:
            attr_key_list = pm.keyframe(obj, attribute=attr, query=True, cp=False)
            key_list = key_list+attr_key_list
        fix_key_list = list(set(key_list))
        fix_key_list.sort()
        print obj
        print attr_list
        print fix_key_list
        for key in fix_key_list:
            cmds.currentTime(key)
            for attr in attr_list:
                value = obj.getAttr(attr)
                print attr
                print value
                pm.setKeyframe(obj, attribute=attr, t=key, v=value)

    def getAllSlots(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        slot_info_list = []
        for mesh in mesh_list:
            parent_bone = pm.listRelatives(mesh.getTransform(), p=True)[0]
            attr_list = ['colorGainR', 'colorGainG', 'colorGainB', 'alphaGain']
            self.setAttrSameKey(parent_bone, attr_list)
            blend_mode = self.getBlendMode(parent_bone)
            r = parent_bone.getAttr('colorGainR')
            r = self.colorConvert16(r)
            g = parent_bone.getAttr('colorGainG')
            g = self.colorConvert16(g)
            b = parent_bone.getAttr('colorGainB')
            b = self.colorConvert16(b)
            alpha = parent_bone.getAttr('alphaGain')
            alpha = self.colorConvert16(alpha)
            color_data = r+g+b+alpha
            name = mesh.getTransform().nodeName()
            file_image = self.getTextureInfo(mesh)[3]
            attachment_name = os.path.splitext(file_image)[0]
            slot_dict = {}
            slot_dict["name"] = name
            slot_dict["bone"] = parent_bone.nodeName()
            slot_dict["color"] = 'ffffffff'
            slot_dict["attachment"] = attachment_name
            slot_dict["blend"] = blend_mode
            slot_info_list.append(slot_dict)
        return slot_info_list

    def getSkinList(self):
        cmds.currentTime(1)
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        skin_info_dict = {"default": {}}
        for mesh in mesh_list:
            transform = mesh.getTransform()
            transform_name = transform.nodeName()
            skin_info_dict["default"][transform_name] = {}
            SG = pm.listConnections(mesh, type='shadingEngine')[0]
            shader = pm.listConnections(SG.surfaceShader, d=False, s=True, type='lambert')[0]
            file = pm.listConnections(shader.color, d=False, s=True, type='file')[0]
            file_image = file.getAttr('fileTextureName')
            name_ext = os.path.basename(file_image)
            name = os.path.splitext(name_ext)[0]
            width = int(transform.getAttr('scaleX'))
            height = int(transform.getAttr('scaleY'))
            x = round(transform.getAttr('translateX'), 2)
            y = round(transform.getAttr('translateY'), 2)
            if self.getSequence(file_image) is False:
                attachment_name = name
                skin_info_dict["default"][transform_name][attachment_name] = {}
                skin_info_dict["default"][transform_name][attachment_name]["width"] = width
                skin_info_dict["default"][transform_name][attachment_name]["height"] = height
                skin_info_dict["default"][transform_name][attachment_name]["x"] = x
                skin_info_dict["default"][transform_name][attachment_name]["y"] = y
            else:
                image_min = self.getSequence(file_image)[0]
                image_max = self.getSequence(file_image)[1]
                for i in xrange(image_min, image_max+1):
                    run_frame = "%04d" % (i)
                    print run_frame
                    attachment_name = name[0:-4]+run_frame
                    skin_info_dict["default"][transform_name][attachment_name] = {}
                    skin_info_dict["default"][transform_name][attachment_name]["width"] = width
                    skin_info_dict["default"][transform_name][attachment_name]["height"] = height
                    # skin_info_dict["default"][transform_name][attachment_name]["x"] = x
                    # skin_info_dict["default"][transform_name][attachment_name]["y"] = y
        return skin_info_dict

    def exportJsonSpine_PB_hit(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        self.fixName(root_joint, 'mesh')
        self.fixName(root_joint, 'joint')
        bone_data = self.getAllBones()
        slot_data = self.getAllSlots()
        skin_data = self.getSkinList()
        animation_data = self.getAnimation()
        final_dict = {}
        final_dict['bones'] = bone_data
        final_dict['slots'] = slot_data
        final_dict['skins'] = skin_data
        final_dict['animations'] = animation_data
        self.info_label.setText("Doing")
        json_path = self.outDir_LE.text()
        json_path = json_path.replace('\\', '/')
        json_name = self.json_LE.text()
        if os.path.exists(json_path) is False:
            os.mkdir(json_path)
        json_file = json_path+"/"+json_name+".json"
        file2 = open(json_file, 'w')
        json.dump(final_dict, file2, ensure_ascii=True, indent=4)
        file2.close()
        self.info_label.setText("Done")

    def fixName(self, root_joint, node_type):
        node_list = pm.listRelatives(root_joint, allDescendents=True, type=node_type)
        name_list = []
        for node in node_list:
            node_name = node.nodeName()
            try:
                node_name = node.getTransform().nodeName()
            except:
                print node.nodeName()
                print 'no transform node'
                pass
            transform_name = self.withoutNum(node_name)
            if transform_name not in name_list:
                name_list.append(transform_name)
        node_rename_list = []
        for name in name_list:
            node_dic = {}
            node_dic['name'] = name
            node_dic['nodes'] = []
            node_dic['total'] = 0
            node_rename_list.append(node_dic)

        for node in node_list:
            transform = node
            transform_name = node.nodeName()
            transform_name = self.withoutNum(transform_name)
            try:
                transform = node.getTransform()
                transform_name = node.getTransform().nodeName()
                transform_name = self.withoutNum(transform_name)
            except:
                pass
            for num, i in enumerate(node_rename_list):
                if transform_name == i['name']:
                    node_rename_list[num]['nodes'].append(transform)
                    node_rename_list[num]['total'] = node_rename_list[num]['total']+1

        for i in node_rename_list:
            if i['total'] > 1:
                for num, node in enumerate(i['nodes']):
                    four_num = "%04d" % (num+1)
                    new_name = i['name']+four_num
                    pm.rename(node, new_name)

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

    def getAnimation(self):
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        fps = self.getFpsValue()
        animation_info = {}
        animation_info['testAnimation'] = {}
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        bone_list = []
        bone_list = self.checkNodeChild(root_joint, bone_list, 'joint')
        second_joint_list = []
        for mesh in mesh_list:
            second_joint = pm.listRelatives(mesh.getTransform(), p=True)[0]
            second_joint_list.append(second_joint)
        bones_data = {}
        for bone in bone_list:
            bone_name = bone.nodeName()
            bones_data[bone_name] = {}
            start_frame_attr = pm.attributeQuery('startFrame', node=bone, exists=True)
            if start_frame_attr is True:
                offsetValue = bone.getAttr('startFrame')-1
            else:
                offsetValue = 0
            key_list = pm.keyframe(bone, attribute='translateX', query=True, cp=False)
            key_dict, sort_key_list = self.reFixKeyFrame(key_list)
            if key_dict is not None:
                bones_data[bone_name]['translate'] = []
                bone_trans_set_up_dict = {'x': 0, 'y': 0, 'time': 0}
                bones_data[bone_name]['translate'].append(bone_trans_set_up_dict)
                for key in sort_key_list:
                    cmds.currentTime(key)
                    x = bone.getAttr('translateX')
                    y = bone.getAttr('translateY')
                    # key_value = (key-offsetValue)/fps
                    key_value = key/fps
                    tanslate_dict = {}
                    tanslate_dict['x'] = round(x, 2)
                    tanslate_dict['y'] = round(y, 2)
                    tanslate_dict['time'] = round(key_value, 2)
                    trueKey = key_dict[key]['trueKey']
                    if key_dict[key]['curve'] is True:
                        tangent = self.getKeyCurve(bone, trueKey, 'translateX')
                        tanslate_dict['curve'] = tangent
                    bones_data[bone_name]['translate'].append(tanslate_dict)

            key_list = pm.keyframe(bone, attribute='rotateZ', query=True, cp=False)
            key_dict, sort_key_list = self.reFixKeyFrame(key_list)
            if key_dict is not None:
                bones_data[bone_name]['rotate'] = []
                bone_rotate_set_up_dict = {'angle': 0, 'time': 0}
                bones_data[bone_name]['rotate'].append(bone_rotate_set_up_dict)
                for key in sort_key_list:
                    cmds.currentTime(key)
                    angle = bone.getAttr('rotateZ')
                    # key_value = (key-offsetValue)/fps
                    key_value = key/fps
                    rotate_dict = {}
                    rotate_dict['angle'] = round(angle, 2)
                    rotate_dict['time'] = round(key_value, 2)
                    trueKey = key_dict[key]['trueKey']
                    if key_dict[key]['curve'] is True:
                        tangent = self.getKeyCurve(bone, trueKey, 'rotateZ')
                        rotate_dict['curve'] = tangent
                    bones_data[bone_name]['rotate'].append(rotate_dict)

            key_list = pm.keyframe(bone, attribute='scaleX', query=True, cp=False)
            key_dict, sort_key_list = self.reFixKeyFrame(key_list)
            if key_dict is not None:
                bones_data[bone_name]['scale'] = []
                bone_scale_set_up_dict = {'x': 1, 'y': 1, 'time': 0}
                bones_data[bone_name]['scale'].append(bone_scale_set_up_dict)
                for key in sort_key_list:
                    cmds.currentTime(key)
                    x = bone.getAttr('scaleX')
                    y = bone.getAttr('scaleY')
                    # key_value = (key-offsetValue)/fps
                    key_value = key/fps
                    trueKey = key_dict[key]['trueKey']
                    scale_dict = {}
                    scale_dict['x'] = round(x, 2)
                    scale_dict['y'] = round(y, 2)
                    scale_dict['time'] = round(key_value, 2)
                    if key_dict[key]['curve'] is True:
                        tangent = self.getKeyCurve(bone, trueKey, 'scaleX')
                        scale_dict['curve'] = tangent
                    bones_data[bone_name]['scale'].append(scale_dict)
        slot_data = {}
        for mesh in mesh_list:
            mesh_tranform = mesh.getTransform().nodeName()
            slot_data[mesh_tranform] = {}
            SG = pm.listConnections(mesh, type='shadingEngine')[0]
            shader = pm.listConnections(SG.surfaceShader, d=False, s=True, type='lambert')[0]
            file = pm.listConnections(shader.color, d=False, s=True, type='file')[0]
            file_image = file.getAttr('fileTextureName')
            name_ext = os.path.basename(file_image)
            name = os.path.splitext(name_ext)[0]
            sequence = self.getSequence(file_image)
            if sequence is not False:
                base_name = name[0:-4]
                slot_data[mesh_tranform]['attachment'] = []
                random_num = random.randint(0, 99)
                cycle_num = sequence[1]
                last_image = 'default'
                for frame in xrange(min_frame, max_frame):
                    slow_speed = 1
                    slow_frame = frame / slow_speed
                    run_frame = (slow_frame+random_num) % cycle_num+1
                    run_frame = "%04d" % (run_frame)
                    if last_image == 'default':
                        slot_dict = {}
                        slot_dict['time'] = 0
                        slot_dict['name'] = base_name+run_frame
                        slot_data[mesh_tranform]['attachment'].append(slot_dict)
                        last_image = run_frame
                    elif run_frame != last_image:
                        key_value = frame/fps
                        slot_dict = {}
                        slot_dict['time'] = round(key_value, 2)
                        slot_dict['name'] = base_name+run_frame
                        slot_data[mesh_tranform]['attachment'].append(slot_dict)
                        last_image = run_frame
                    elif run_frame == last_image:
                        pass
            second_joint = pm.listRelatives(mesh.getTransform(), p=True)[0]
            start_frame_attr = pm.attributeQuery('startFrame', node=second_joint, exists=True)
            if start_frame_attr is True:
                offsetValue = second_joint.getAttr('startFrame')-1
            else:
                offsetValue = 0
            color_key_list = pm.keyframe(second_joint, attribute='colorGainR', query=True, cp=False)
            alpha_key_list = pm.keyframe(second_joint, attribute='alphaGain', query=True, cp=False)
            key_list = color_key_list + alpha_key_list
            key_list = list(set(key_list))
            key_dict, sort_key_list = self.reFixKeyFrame(key_list)
            if key_dict is not None:
                slot_data[mesh_tranform]['color'] = []
                slot_color_set_up_dict = {'color': "ffffffff", 'time': 0}
                slot_data[mesh_tranform]['color'].append(slot_color_set_up_dict)
                for key in sort_key_list:
                    cmds.currentTime(key)
                    # key_value = (key-offsetValue)/fps
                    key_value = key/fps
                    trueKey = key_dict[key]['trueKey']
                    r = second_joint.getAttr('colorGainR')
                    r = self.colorConvert16(r)
                    g = second_joint.getAttr('colorGainG')
                    g = self.colorConvert16(g)
                    b = second_joint.getAttr('colorGainB')
                    b = self.colorConvert16(b)
                    alpha = second_joint.getAttr('alphaGain')
                    alpha = self.colorConvert16(alpha)
                    color_data = r+g+b+alpha
                    color_dict = {}
                    color_dict['color'] = color_data
                    color_dict['time'] = round(key_value, 2)
                    if key_dict[key]['curve'] is True:
                        tangent = self.getKeyCurve(second_joint, trueKey, 'alphaGain')
                        color_dict['curve'] = tangent
                    slot_data[mesh_tranform]['color'].append(color_dict)

        animation_info['testAnimation']['bones'] = bones_data
        animation_info['testAnimation']['slots'] = slot_data
        return animation_info

    def getFpsValue(self):
        time_mode = pm.currentUnit(query=True, time=True)
        if time_mode == 'ntsc':
            fps = 30
        elif time_mode == 'ntscf':
            fps = 60
        elif time_mode == 'film':
            fps = 24
        return float(fps)

    def checkOverMaxFrame(self, key):
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        if key > max_frame:
            key = (key % max_frame)+1
        elif key == min_frame or key == max_frame:
            key = False
        return key

    def reFixKeyFrame(self, key_list):
        if key_list is None:
            return None, None
        key_list.sort()
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        final_key_dict = {min_frame: {'trueKey': min_frame, 'curve': False}, max_frame: {'trueKey': max_frame, 'curve': False}}
        for i in key_list:
            if i > max_frame:
                reSetKey = (i-1) % (max_frame-min_frame) + 1
                final_key_dict[reSetKey] = {'trueKey': i, 'curve': True}
            else:
                final_key_dict[i] = {'trueKey': i, 'curve': True}
        if 0 in final_key_dict:
            del final_key_dict[0]
        key_num_list = []
        for key in final_key_dict:
            key_num_list.append(key)
        key_num_list.sort()
        return final_key_dict, key_num_list

    def getKeyCurve(self, obj, key, attr):
        tangent = pm.keyTangent(obj, query=True, time=(key, key), attribute=attr, ott=True)[0]
        if tangent == 'step':
            tangent = 'stepped'
        else:
            tangent = 'linear'
        return tangent

    def getSequence(self, file):
        path = os.path.dirname(file)
        all_file_list = os.listdir(path)
        nameExt = os.path.basename(file)
        name = os.path.splitext(nameExt)[0]
        num_list = []
        if name[-4:len(name)] == '0001':
            for file in all_file_list:
                file_name = os.path.splitext(file)[0]
                if self.is_number(file_name[-4:len(file_name)]):
                    if file_name[0:-4] == name[0:-4]:
                        num_list.append(int(file_name[-4:len(file_name)]))
            min_frame = min(num_list)
            max_frame = max(num_list)
            return [min_frame, max_frame]
        else:
            return False


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


def pixiToolsMain():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()
