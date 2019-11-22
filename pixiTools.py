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
import sys
import math
import random
import time
import pprint
from shutil import copyfile

maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/' + username + '/Documents/maya/' + maya_version + '/scripts/ui'
py27_lib = 'C:/Python27/Lib/site-packages'
sys.path.append(py27_lib)
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
from PIL import Image
import pixiTools_export_json_ui
reload(pixiTools_export_json_ui)
import pixiTools_export_spine_json_ui
reload(pixiTools_export_spine_json_ui)
import pixiTools_particleEdit_ui
reload(pixiTools_particleEdit_ui)
dialog = None


# ------------------------------------------------------------------------------------
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('pixi tools' + ' v0.5' + u' by 小黑')
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
        self.pixiTools_particleEdit_wid = pixiTools_particleEdit_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.pixiTools_export_json_wid, "Export Pixi Json")
        main_tab_Widget.addTab(self.pixiTools_export_spine_json_wid, "Export Spine Json")
        main_tab_Widget.addTab(self.pixiTools_particleEdit_wid, "Particle Edit")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/pixiTools.csv'
        self.python_temp_json = self.python_temp + '/pixiTools.json'
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
            self.pixiTools_export_spine_json_wid.scale_CB,
            self.pixiTools_export_spine_json_wid.rotation_CB,
            self.pixiTools_export_spine_json_wid.drawOrder_CB,
            self.pixiTools_export_spine_json_wid.nums_LE,
            self.pixiTools_export_spine_json_wid.textureFile_LE,
            self.pixiTools_export_spine_json_wid.rootJoint_LE,
            self.pixiTools_export_spine_json_wid.autoRename_LE,
            self.pixiTools_particleEdit_wid.randomKeyMin_LE,
            self.pixiTools_particleEdit_wid.randomKeyMax_LE,
            self.pixiTools_particleEdit_wid.textureFile_LE,
            self.pixiTools_particleEdit_wid.texWidth_LE,
            self.pixiTools_particleEdit_wid.texHeight_LE,
            self.pixiTools_particleEdit_wid.instanceGrpName_LE,
            self.pixiTools_particleEdit_wid.startFrameLoop_LE,
            self.pixiTools_particleEdit_wid.endFrameLoop_LE,
            self.pixiTools_particleEdit_wid.frequency_LE,
            self.pixiTools_particleEdit_wid.attr_button_group,
            self.pixiTools_particleEdit_wid.attr_set_type_group,
            self.pixiTools_particleEdit_wid.minValue_LE,
            self.pixiTools_particleEdit_wid.maxValue_LE,
            self.pixiTools_particleEdit_wid.keyIndex_LE,
            self.pixiTools_particleEdit_wid.motionPathCurve_LE,
            self.pixiTools_particleEdit_wid.joint_list_LE,
            self.pixiTools_particleEdit_wid.motionPathStartFrame_LE,
            self.pixiTools_particleEdit_wid.motionPathEndFrame_LE,
            self.pixiTools_particleEdit_wid.motionPathKeys_LE,
            self.pixiTools_particleEdit_wid.motionPathPow_LE
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
        for f in xrange(f_min, f_max + 1):
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
        json_file = json_path + "/" + json_name + ".json"
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
        self.animLayer_cb_list = self.animLayerUiCheck()

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
        self.setSameKey_PB.clicked.connect(self.setSameKey_PB_hit)
        self.clearKey_PB.clicked.connect(self.clearKey_PB_hit)
        # self.clearAllKey_PB.clicked.connect(self.clearAllKey_PB_hit)
        self.getChildJoint_PB.clicked.connect(self.getChildJoint_PB_hit)

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
        maya_version = pm.about(version=True)
        mel = 'source "C:/Program Files/Autodesk/Maya%s/scripts/startup/buildSetAnimLayerMenu.mel";' % (maya_version)
        pm.mel.eval(mel)

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
        basename = self.autoRename_LE.text()
        self.reNameChild(node, basename, '')
        pm.rename(node, basename + '_joint')

    def reNameChild(self, root_node, base_name, old_num):
        children_list = pm.listRelatives(root_node, children=True)
        if len(children_list) > 0:
            for num, child in enumerate(children_list):
                node_type = child.type()
                new_num = str(num)
                mix_num = old_num + '_' + new_num
                try:
                    if child.getShape().type() == 'mesh':
                        node_type = 'mesh'
                except:
                    pass
                set_new_name = base_name + mix_num + '_' + node_type
                pm.rename(child, set_new_name)
                self.reNameChild(child, base_name, mix_num)

    def planeEditFixSize_PB_hit(self):
        mesh_list = self.getSelectMeshList()
        for mesh in mesh_list:
            meshShape = mesh.getShape()
            filePath = self.getTextureInfo(meshShape)[4]
            if filePath[0:12] == 'sourceimages':
                current_workspace = cmds.workspace(q=True, rd=True)
                filePath = current_workspace + filePath
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
            pm.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')
            pm.select(clear=True)
            pm.select(mesh)
            pm.hyperShade(assign=shading_group)
            file_node = pm.shadingNode('file', n='baseImage_file', asTexture=True, isColorManaged=True)
            texture_file = self.textureFile_LE.text()
            file_node.setAttr('fileTextureName', texture_file, type='string')
            pm.connectAttr(file_node + '.outColor', lambert_shader + '.color')
            pm.connectAttr(file_node + '.outTransparency', lambert_shader + '.transparency')
            multiplyDivide_node = pm.shadingNode('multiplyDivide', asUtility=True)
            pm.connectAttr(second_joint + '.alphaGain', multiplyDivide_node + '.input1.input1X')
            pm.connectAttr(second_joint + '.fadeGain', multiplyDivide_node + '.input2.input2X')
            pm.connectAttr(multiplyDivide_node + '.output.outputX', file_node + '.alphaGain')
            pm.connectAttr(second_joint + '.colorGainR', file_node + '.colorGainR')
            pm.connectAttr(second_joint + '.colorGainG', file_node + '.colorGainG')
            pm.connectAttr(second_joint + '.colorGainB', file_node + '.colorGainB')

        for mesh in mesh_list:
            meshShape = mesh.getShape()
            filePath = self.getTextureInfo(meshShape)[4]
            if filePath[0:12] == 'sourceimages':
                current_workspace = cmds.workspace(q=True, rd=True)
                filePath = current_workspace + filePath
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
            image_plane[0].setAttr('rotateX', keyable=False, channelBox=True, lock=True)
            image_plane[0].setAttr('rotateY', keyable=False, channelBox=True, lock=True)
            image_plane[0].setAttr('rotateZ', keyable=False, channelBox=True, lock=True)
            image_plane[0].setAttr('visibility', keyable=False, channelBox=True)
            pm.select(clear=True)
            second_joint = pm.joint(name="second_joint", p=[0, 0, 0])
            cmds.addAttr(longName='alphaGain', defaultValue=1.0, minValue=0, maxValue=1, keyable=True)
            cmds.addAttr(longName='fadeGain', defaultValue=1.0, minValue=0, maxValue=1, keyable=True)
            cmds.addAttr(longName='colorGain', usedAsColor=True, attributeType='float3', keyable=True)
            cmds.addAttr(longName='colorGainR', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainG', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainB', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='blendMode', attributeType="enum", enumName="normal:multiply:additive:screen", keyable=True)
            cmds.addAttr(longName='startFrame', defaultValue=1, attributeType="long", keyable=True)
            pm.parent(second_joint, root_joint, relative=True)
            pm.parent(image_plane[0], second_joint, relative=True)

    def getBlendMode(self, bone):
        enumString = pm.attributeQuery('blendMode', node=bone, listEnum=1)[0]
        enumList = enumString.split(":")
        index = bone.getAttr('blendMode')
        return enumList[index]

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
            value_B = int(value * 255)
        value16bit = hex(value_B)
        value16_str = value16bit[2:len(value16bit)]
        while len(value16_str) < 2:
            value16_str = "0" + value16_str
        return value16_str

    def setAttrSameKey(self, obj, attr_list):
        key_list = []
        for attr in attr_list:
            attr_key_list = pm.keyframe(obj, attribute=attr, query=True, cp=False)
            key_list = key_list + attr_key_list
        key_list = list(set(key_list))
        key_list.sort()
        print obj.name()
        print key_list

        if len(key_list) > 0:
            for key in key_list:
                cmds.currentTime(key)
                for attr in attr_list:
                    print attr
                    value = obj.getAttr(attr)
                    pm.setKeyframe(obj, attribute=attr, t=key, v=value)

            '''
            pre_infinity_loop = False
            post_infinity_loop = False
            for attr in attr_list:
                attr_key_list = pm.keyframe(obj, attribute=attr, query=True, cp=False)
                pre_infinity, post_infinity = self.checkAnimCurveLoop(obj, attr)
                if pre_infinity == 3:
                    pre_infinity_loop = True
                if post_infinity == 3:
                    post_infinity_loop = True
            if pre_infinity_loop is True:
                for attr in attr_list:
                    anim_curve_name = pm.keyframe(obj, attribute=attr, query=True, name=True)[0]
                    anim_curve_node = pm.PyNode(anim_curve_name)
                    anim_curve_node.setAttr('preInfinity', 3)
            if post_infinity_loop is True:
                for attr in attr_list:
                    anim_curve_name = pm.keyframe(obj, attribute=attr, query=True, name=True)[0]
                    anim_curve_node = pm.PyNode(anim_curve_name)
                    anim_curve_node.setAttr('postInfinity', 3)
            '''

    def setSameKey_PB_hit(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        joint_list = pm.listRelatives(root_joint, allDescendents=True, type='joint')
        joint_list.append(root_joint)
        second_joint = []
        for mesh in mesh_list:
            parent_bone = pm.listRelatives(mesh.getTransform(), p=True)[0]
            second_joint.append(parent_bone)
        attr_list = ['colorGainR', 'colorGainG', 'colorGainB', 'alphaGain']
        for joint in second_joint:
            self.setAttrSameKey(joint, attr_list)
        for joint in joint_list:
            attr_list = ['translateX', 'translateY']
            self.setAttrSameKey(joint, attr_list)
            attr_list = ['scaleX', 'scaleY']
            self.setAttrSameKey(joint, attr_list)
        self.info_label.setText('Set Same Key Done')

    def clearKey_PB_hit(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        joint_list = pm.listRelatives(root_joint, allDescendents=True, type='joint')
        joint_list.append(root_joint)
        node_list = []
        for mesh in mesh_list:
            node_list.append(mesh.getTransform())
        node_list = node_list + joint_list
        for node in node_list:
            attr_list = pm.listAttr(node, keyable=True)
            for attr in attr_list:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                if len(key_list) == 1:
                    anim_curve_name = pm.keyframe(node, attribute=attr, query=True, name=True)[0]
                    anim_curve_node = pm.PyNode(anim_curve_name)
                    pm.delete(anim_curve_node)
        self.info_label.setText('clear key done')

    def getAllSlots(self):
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        slot_info_list = []
        for mesh in mesh_list:
            parent_bone = pm.listRelatives(mesh.getTransform(), p=True)[0]
            blend_mode = self.getBlendMode(parent_bone)
            r = parent_bone.getAttr('colorGainR')
            r = self.colorConvert16(r)
            g = parent_bone.getAttr('colorGainG')
            g = self.colorConvert16(g)
            b = parent_bone.getAttr('colorGainB')
            b = self.colorConvert16(b)
            alpha = parent_bone.getAttr('alphaGain')
            alpha = self.colorConvert16(alpha)
            color_data = r + g + b + alpha
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
            use_frame_extension = file.getAttr('useFrameExtension')
            if use_frame_extension is False:
                attachment_name = name
                skin_info_dict["default"][transform_name][attachment_name] = {}
                skin_info_dict["default"][transform_name][attachment_name]["width"] = width
                skin_info_dict["default"][transform_name][attachment_name]["height"] = height
                skin_info_dict["default"][transform_name][attachment_name]["x"] = x
                skin_info_dict["default"][transform_name][attachment_name]["y"] = y
            else:
                image_min = self.getSequence(file_image)[0]
                image_max = self.getSequence(file_image)[1]
                for i in xrange(image_min, image_max + 1):
                    run_frame = "%04d" % (i)
                    attachment_name = name[0:-4] + run_frame
                    skin_info_dict["default"][transform_name][attachment_name] = {}
                    skin_info_dict["default"][transform_name][attachment_name]["width"] = width
                    skin_info_dict["default"][transform_name][attachment_name]["height"] = height
                    skin_info_dict["default"][transform_name][attachment_name]["x"] = x
                    skin_info_dict["default"][transform_name][attachment_name]["y"] = y
        return skin_info_dict

    def skeletonData(self):
        skeleton = {
            "width": 1920,
            "height": 1080
        }
        return skeleton

    def exportJsonSpine_PB_hit(self):
        mel = 'ogs -pause;'
        pm.mel.eval(mel)
        time_start = time.time()
        self.setRenderLayer('exportJson_RL')
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        self.fixName(root_joint, 'mesh')
        self.fixName(root_joint, 'joint')
        bone_data = self.getAllBones()
        slot_data = self.getAllSlots()
        skin_data = self.getSkinList()
        skeleton_data = self.skeletonData()
        final_dict = {}
        final_dict['skeleton'] = skeleton_data
        final_dict['bones'] = bone_data
        final_dict['slots'] = slot_data
        final_dict['skins'] = skin_data
        final_dict['animations'] = {}
        animLayer_node_checked_list = []
        baseLayer = pm.animLayer(query=True, root=True)
        for animLayer_cb in self.animLayer_cb_list:
            if animLayer_cb.checkState() == QtCore.Qt.Checked:
                anim_node = animLayer_cb.node
                animLayer_node_checked_list.append(anim_node)
        if len(animLayer_node_checked_list) > 0:
            for animLayer_node_checked in animLayer_node_checked_list:
                for animLayer_cb in self.animLayer_cb_list:
                    animLayer_node = animLayer_cb.node
                    pm.animLayer(animLayer_node, edit=True, mute=True, solo=False, lock=True)
                pm.animLayer(animLayer_node_checked, edit=True, mute=False, solo=True, lock=False)
                anim_layer_name = animLayer_node_checked.name()
                mel = 'selectLayer("%s");' % (anim_layer_name)
                pm.mel.eval(mel)
                animation_data = self.getAnimation()
                final_dict['animations'][anim_layer_name] = animation_data
        else:
            animation_data = self.getAnimation()
            final_dict['animations']['baseAnim'] = animation_data
        self.info_label.setText("Doing")
        json_path = self.outDir_LE.text()
        json_path = json_path.replace('\\', '/')
        json_name = self.json_LE.text()
        if os.path.exists(json_path) is False:
            os.mkdir(json_path)
        json_file = json_path + "/" + json_name + "_fromMaya.json"
        file2 = open(json_file, 'w')
        json.dump(final_dict, file2, ensure_ascii=True, indent=4)
        file2.close()
        '''
        data = json.dumps(OrderedDict(final_dict), ensure_ascii=True, indent=4)
        with open(json_file, "w") as f:
            f.write(data)
        '''
        self.exportTexures()
        time_end = time.time()
        total_time = time_end - time_start
        m, s = divmod(total_time, 60)
        info = 'total %s m %s s to complete' % (int(m), int(s))
        self.info_label.setText(info)

    def fixName(self, root_joint, node_type):
        node_list = pm.listRelatives(root_joint, allDescendents=True, type=node_type)
        name_list = []
        for node in node_list:
            node_name = node.nodeName()
            try:
                node_name = node.getTransform().nodeName()
            except:
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
                    node_rename_list[num]['total'] = node_rename_list[num]['total'] + 1

        for i in node_rename_list:
            if i['total'] > 1:
                for num, node in enumerate(i['nodes']):
                    four_num = "%04d" % (num + 1)
                    new_name = i['name'] + four_num
                    pm.rename(node, new_name)

    def withoutNum(self, name):
        while self.is_number(name[-1:len(name)]):
            numMax = len(name)
            name = name[0:numMax - 1]
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
        fps_cb_num = self.speed_doubleSpinBox.value()
        fps = fps * fps_cb_num
        animation_info = {}
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
            print 'bone_name : %s' % (bone_name)
            bones_data[bone_name] = {}
            start_frame_attr = pm.attributeQuery('startFrame', node=bone, exists=True)
            if start_frame_attr is True:
                offsetValue = bone.getAttr('startFrame') - 1
            else:
                offsetValue = 0
            bones_data[bone_name]['translate'] = []
            bone_trans_set_up_dict = {'x': 0, 'y': 0, 'time': 0}
            bones_data[bone_name]['translate'].append(bone_trans_set_up_dict)
            none_key = self.checkAniNoneKey(bone, ['translateX', 'translateY'])
            if none_key is True:
                cmds.currentTime(1)
                x = bone.getAttr('translateX')
                y = bone.getAttr('translateY')
                key_value = 1 / fps
                translate_dict = {
                    'time': round(key_value, 4),
                    'x': round(x, 2),
                    'y': round(y, 2)
                }
                bones_data[bone_name]['translate'].append(translate_dict)
            key_dict, sort_key_list = self.keyFrameData(bone, 'translateX')
            # print 'translate_key_dict : %s' % (key_dict)
            # print 'translate_sort_key_list : %s' % (sort_key_list)
            if key_dict is not None:
                for key in sort_key_list:
                    cmds.currentTime(key)
                    x = bone.getAttr('translateX')
                    y = bone.getAttr('translateY')
                    key_value = key / fps
                    translate_dict = {
                        'time': round(key_value, 4),
                        'x': round(x, 2),
                        'y': round(y, 2)
                    }
                    bones_data[bone_name]['translate'].append(translate_dict)

            bones_data[bone_name]['rotate'] = []
            bone_rotate_set_up_dict = {'angle': 0, 'time': 0}
            bones_data[bone_name]['rotate'].append(bone_rotate_set_up_dict)
            none_key = self.checkAniNoneKey(bone, ['rotateZ'])
            if none_key is True:
                cmds.currentTime(1)
                angle = bone.getAttr('rotateZ')
                if angle < 0:
                    fix_angle = 360 + (angle % 360)
                else:
                    fix_angle = angle % 360

                key_value = 1 / fps
                rotate_dict = {
                    'time': round(key_value, 4),
                    'angle': round(fix_angle, 2)
                }
                bones_data[bone_name]['rotate'].append(rotate_dict)
            key_dict, sort_key_list = self.keyFrameData(bone, 'rotateZ')
            if key_dict is not None:
                for key in sort_key_list:
                    cmds.currentTime(key)
                    angle = bone.getAttr('rotateZ')
                    if angle < 0:
                        fix_angle = 360 + (angle % 360)
                    else:
                        fix_angle = angle % 360
                    # key_value = (key-offsetValue)/fps
                    key_value = key / fps
                    rotate_dict = {
                        'time': round(key_value, 4),
                        'angle': round(fix_angle, 2)
                    }
                    bones_data[bone_name]['rotate'].append(rotate_dict)

            bones_data[bone_name]['scale'] = []
            bone_scale_set_up_dict = {'x': 1, 'y': 1, 'time': 0}
            bones_data[bone_name]['scale'].append(bone_scale_set_up_dict)
            none_key = self.checkAniNoneKey(bone, ['scaleX', 'scaleY'])
            if none_key is True:
                cmds.currentTime(1)
                x = bone.getAttr('scaleX')
                y = bone.getAttr('scaleY')
                # key_value = (key-offsetValue)/fps
                key_value = 1 / fps
                scale_dict = {
                    'time': round(key_value, 4),
                    'x': round(x, 2),
                    'y': round(y, 2)
                }
                bones_data[bone_name]['scale'].append(scale_dict)
            key_dict, sort_key_list = self.keyFrameData(bone, 'scaleX')
            if key_dict is not None:
                bones_data[bone_name]['scale'] = []
                bone_scale_set_up_dict = {'x': 1, 'y': 1, 'time': 0}
                bones_data[bone_name]['scale'].append(bone_scale_set_up_dict)
                for key in sort_key_list:
                    cmds.currentTime(key)
                    x = bone.getAttr('scaleX')
                    y = bone.getAttr('scaleY')
                    # key_value = (key-offsetValue)/fps
                    key_value = key / fps
                    scale_dict = {
                        'time': round(key_value, 4),
                        'x': round(x, 2),
                        'y': round(y, 2)
                    }
                    bones_data[bone_name]['scale'].append(scale_dict)

        slot_data = {}
        for mesh in mesh_list:
            mesh_tranform = mesh.getTransform().nodeName()
            second_joint = pm.listRelatives(mesh_tranform, p=True)[0]
            alpha_none_zero_list = []
            alpha_value_list = pm.keyframe(second_joint + '.alphaGain', query=True, vc=True)
            for value in alpha_value_list:
                if value != 0:
                    alpha_none_zero_list.append(value)
            slot_data[mesh_tranform] = {}
            SG = pm.listConnections(mesh, type='shadingEngine')[0]
            shader = pm.listConnections(SG.surfaceShader, d=False, s=True, type='lambert')[0]
            file = pm.listConnections(shader.color, d=False, s=True, type='file')[0]
            file_image = file.getAttr('fileTextureName')
            name_ext = os.path.basename(file_image)
            name = os.path.splitext(name_ext)[0]
            sequence = self.getSequence(file_image)
            use_frame_extension = file.getAttr('useFrameExtension')
            if len(alpha_none_zero_list) > 0:
                if use_frame_extension is True:
                    '''
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
                    '''
                    slot_data[mesh_tranform]['attachment'] = []
                    for frame in xrange(min_frame, max_frame):
                        cmds.currentTime(frame)
                        image_name = self.getImageIndex(file)
                        slot_dict = {}
                        key_value = frame / fps
                        slot_dict['time'] = round(key_value, 4)
                        slot_dict['name'] = image_name
                        slot_data[mesh_tranform]['attachment'].append(slot_dict)

            second_joint = pm.listRelatives(mesh.getTransform(), p=True)[0]
            start_frame_attr = pm.attributeQuery('startFrame', node=second_joint, exists=True)
            if start_frame_attr is True:
                offsetValue = second_joint.getAttr('startFrame')- 1
            else:
                offsetValue = 0
            slot_data[mesh_tranform]['color'] = []
            slot_color_set_up_dict = {'color': "ffffffff", 'time': 0}
            slot_data[mesh_tranform]['color'].append(slot_color_set_up_dict)
            none_key = self.checkAniNoneKey(bone, ['colorGainR', 'colorGainG', 'colorGainB'])
            if none_key is True:
                cmds.currentTime(1)
                key_value = 1 / fps
                r = second_joint.getAttr('colorGainR')
                r = self.colorConvert16(r)
                g = second_joint.getAttr('colorGainG')
                g = self.colorConvert16(g)
                b = second_joint.getAttr('colorGainB')
                b = self.colorConvert16(b)
                alphaGain = second_joint.getAttr('alphaGain')
                fadeGain = second_joint.getAttr('fadeGain')
                alpha = self.colorConvert16(alphaGain * fadeGain)
                color_data = r + g + b + alpha
                color_dict = {
                    'time': round(key_value, 4),
                    'color': color_data
                }
                slot_data[mesh_tranform]['color'].append(color_dict)
            key_dict, sort_key_list = self.keyFrameData(second_joint, 'alphaGain')
            print "alphaGain_key_dict : %s" % key_dict
            print "alphaGain_sort_key_list : %s" % sort_key_list
            print "mesh_name : %s" % mesh_tranform
            print "second_joint : %s" % second_joint

            if key_dict is not None:
                for key in sort_key_list:
                    print key
                    cmds.currentTime(key)
                    # key_value = (key-offsetValue)/fps
                    key_value = key / fps
                    r = second_joint.getAttr('colorGainR')
                    r = self.colorConvert16(r)
                    g = second_joint.getAttr('colorGainG')
                    g = self.colorConvert16(g)
                    b = second_joint.getAttr('colorGainB')
                    b = self.colorConvert16(b)
                    alpha = second_joint.getAttr('alphaGain')
                    print "alphaGain: %s" % alpha
                    fadeGain = second_joint.getAttr('fadeGain')
                    final_alpha = alpha * fadeGain
                    alpha = self.colorConvert16(final_alpha)
                    color_data = r + g + b + alpha
                    color_dict = {
                        'time': round(key_value, 4),
                        'color': color_data
                    }
                    slot_data[mesh_tranform]['color'].append(color_dict)
        if self.drawOrder_CB.isChecked():
            mesh_list, zdepth_dict = self.zdepthDictCheck()
            drawOrder_list = self.drawOrderAni(mesh_list, zdepth_dict)
            animation_info['drawOrder'] = drawOrder_list
        animation_info['bones'] = bones_data
        animation_info['slots'] = slot_data
        return animation_info

    def checkAniNoneKey(self, obj, attr_list):
        key_list = []
        for attr in attr_list:
            attr_key_list = pm.keyframe(obj, attribute=attr, query=True, cp=False)
            key_list = key_list + attr_key_list
        if len(key_list) != 0:
            return False
        else:
            return True

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
            key = (key % max_frame) + 1
        elif key == min_frame or key == max_frame:
            key = False
        return key

    def keyFrameData(self, node, attr):
        key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
        if len(key_list) == 0:
            return None, None
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        pre_infinity_loop, post_infinity_loop = self.checkAnimCurveLoop(node, attr)
        if pre_infinity_loop != 3 and post_infinity_loop != 3 or len(key_list) == 1:
            key_list = pm.keyframe(node, attribute=attr, query=True, cp=False, time=[min_frame, max_frame])
            final_key_dict = {min_frame: {'trueKey': min_frame, "curve": 'linear'}, max_frame: {'trueKey': max_frame, "curve": 'linear'}}
            for key in key_list:
                tangent = self.getKeyCurve(node, key, attr)
                final_key_dict[key] = {'trueKey': key, 'curve': tangent}
            if 0 in final_key_dict:
                del final_key_dict[0]
            key_num_list = []
            for key in final_key_dict:
                key_num_list.append(key)
            key_num_list.sort()
            return final_key_dict, key_num_list
        else:
            loop_range = max(key_list) - min(key_list)
            final_key_dict = {min_frame: {'trueKey': min_frame, "curve": 'linear'}, max_frame: {'trueKey': max_frame, "curve": 'linear'}}
            for key in key_list:
                tangent = self.getKeyCurve(node, key, attr)
                loop_list = self.checkKeyFrameLoop(key, loop_range, pre_infinity_loop, post_infinity_loop)
                for loop_key in loop_list:
                    final_key_dict[loop_key] = {'trueKey': key, 'curve': tangent}
            key_num_list = []
            for key in final_key_dict:
                key_num_list.append(key)
            key_num_list.sort()
            return final_key_dict, key_num_list

    def checkKeyFrameLoop(self, key_frame, loop_range, pre_infinity_loop, post_infinity_loop):
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        loop_list = []
        if pre_infinity_loop == 3:
            self.findPreFrame(key_frame, loop_list, loop_range, min_frame, max_frame)
        if post_infinity_loop == 3:
            self.findPostFrame(key_frame, loop_list, loop_range, min_frame, max_frame)
        loop_list = list(set(loop_list))
        return loop_list

    def findPreFrame(self, key, loop_list, loop_range, min_frame, max_frame):
        if key >= min_frame and key <= max_frame:
            loop_list.append(key)
            loop_list.sort()
        if key > min_frame:
            key = key - loop_range
            self.findPreFrame(key, loop_list, loop_range, min_frame, max_frame)

    def findPostFrame(self, key, loop_list, loop_range, min_frame, max_frame):
        if key >= min_frame and key <= max_frame:
            loop_list.append(key)
            loop_list.sort()
        if key < max_frame:
            key = key + loop_range
            self.findPostFrame(key, loop_list, loop_range, min_frame, max_frame)

    def getKeyCurve(self, obj, key, attr):
        tangent = pm.keyTangent(obj, query=True, time=(key, key), attribute=attr, ott=True)[0]
        if tangent == 'step':
            tangent = 'stepped'
        else:
            tangent = 'linear'
        return tangent

    def checkAnimCurveLoop(self, node, attr):
        anim_curve_name = pm.keyframe(node, attribute=attr, query=True, name=True)
        if anim_curve_name != []:
            anim_curve_node = pm.PyNode(anim_curve_name[0])
            pre_infinity_loop = anim_curve_node.getAttr('preInfinity')
            post_infinity_loop = anim_curve_node.getAttr('postInfinity')
            return pre_infinity_loop, post_infinity_loop
        else:
            return None, None

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

    def getImageIndex(self, file_node):
        frame_extension = file_node.getAttr('useFrameExtension')
        image_file = file_node.getAttr('fileTextureName')
        folder = os.path.dirname(image_file)
        nameExt = os.path.basename(image_file)
        name = os.path.splitext(nameExt)[0]
        ext = os.path.splitext(nameExt)[1]
        if frame_extension == 1:
            if name[-4:len(name)] == '0001':
                name = name[0:-4]
                index = file_node.getAttr('frameExtension')
                index = '%04d' % (index)
                final_name = name + index
                return final_name
        else:
            return name

    def zdepthDictCheck(self):
        name = self.rootJoint_LE.text()
        node = pm.PyNode(name)
        children_list = pm.listRelatives(node, allDescendents=True, shapes=True)
        children_list.reverse()
        mesh_list = []
        for i in children_list:
            if i.type() == 'mesh':
                node = i.getTransform()
                mesh_list.append(node.nodeName())
        zdepth_dict = {}
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        for frame in xrange(min_frame, max_frame + 1):
            pm.currentTime(frame)
            zdepth_dict[frame] = {}
            for mesh in mesh_list:
                node = pm.PyNode(mesh)
                pivot = pm.xform(node, query=True, rotatePivot=True, worldSpace=True)
                zdepth_dict[frame][node.nodeName()] = pivot[2]
        return mesh_list, zdepth_dict

    def drawOrderAni(self, mesh_list, zdepth_dict):
        fps = self.getFpsValue()
        fps_cb_num = self.speed_doubleSpinBox.value()
        fps = fps * fps_cb_num
        mesh_list.reverse()
        min_frame = int(cmds.playbackOptions(minTime=True, q=True))
        max_frame = int(cmds.playbackOptions(maxTime=True, q=True))
        drawOrder_list = []
        for frame in xrange(min_frame, max_frame + 1):
            # zValue_list = sorted(zdepth_dict[frame].items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
            zValue_list = sorted(zdepth_dict[frame].items(), lambda x, y: cmp(x[1], y[1]))
            key_value = frame / fps
            data_dict = {}
            data_dict['offsets'] = []
            data_dict['time'] = round(key_value, 4)
            name_list = []
            for zValue in zValue_list:
                name_list.append(zValue[0])
            for index, mesh in enumerate(mesh_list):
                order = name_list.index(mesh)
                offset = order - index
                if offset != 0:
                    ani_dict = {}
                    ani_dict['slot'] = mesh
                    ani_dict['offset'] = offset
                    data_dict['offsets'].append(ani_dict)
            drawOrder_list.append(data_dict)
        return drawOrder_list

    def animLayerUiCheck(self):
        animLayer_list = pm.ls(type='animLayer')
        baseLayer = pm.animLayer(query=True, root=True)
        cb_list = []
        if len(animLayer_list) > 1:
            self.clearLayout(self.baseAnimLayer_layout)
            for animLayer in animLayer_list:
                animLayer_cb = checkBox_class(self, animLayer)
                cb_list.append(animLayer_cb)
                self.baseAnimLayer_layout.addWidget(animLayer_cb)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.baseAnimLayer_layout.addSpacerItem(spacerItem)
        elif len(animLayer_list) == 1:
            self.clearLayout(self.baseAnimLayer_layout)
            animLayer_cb = checkBox_class(self, baseLayer)
            animLayer_cb.setCheckState(QtCore.Qt.Checked)
            animLayer_cb.setEnabled(False)
            cb_list.append(animLayer_cb)
            self.baseAnimLayer_layout.addWidget(animLayer_cb)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.baseAnimLayer_layout.addSpacerItem(spacerItem)
        return cb_list

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

    def exportTexures(self):
        pm.currentTime(1)
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        mesh_list = pm.listRelatives(root_joint, allDescendents=True, type='mesh')
        texture_list = []
        for mesh in mesh_list:
            file = self.getTextureInfo(mesh)[4]
            if file[0:12] == 'sourceimages':
                current_workspace = pm.workspace(q=True, rd=True)
                file = current_workspace + file
            if file not in texture_list:
                texture_list.append(file)
        for file in texture_list:
            if self.getSequence(file) is not False:
                min_frame, max_frame = self.getSequence(file)
                for index in range(min_frame, max_frame):
                    scr_path = os.path.dirname(file)
                    nameExt = os.path.basename(file)
                    name, Ext = os.path.splitext(nameExt)
                    index = '%04d' % (index + 1)
                    final_name = scr_path + "/" + name[0:-4] + index + Ext
                    if final_name not in texture_list:
                        texture_list.append(final_name)
        export_path = self.outDir_LE.text()
        for file in texture_list:
            scr_path = os.path.dirname(file)
            scr_name = os.path.basename(file)
            export_file = export_path + '\\' + scr_name
            if os.path.exists(export_file) is True:
                os.remove(export_file)
            copyfile(file, export_file)

    def anyLayerKeyFrameData(self):
        base_layer = self.baseAniLayer_LE.text()
        mel = 'selectLayer("' + base_layer + '");'
        pm.mel.eval(mel)
        all_dict = {}
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        joint_list = pm.listRelatives(root_joint, allDescendents=True, type='joint')
        joint_list.append(root_joint)
        for obj in joint_list:
            obj_dict = {obj: {}}
            keyable_list = pm.listAttr(obj, keyable=True)
            for attr in keyable_list:
                key_count = pm.keyframe(obj, at=attr, q=True, keyframeCount=True)
                if key_count > 0:
                    ani_node = pm.keyframe(obj.nodeName() + '.' + attr, name=True, query=True)[0]
                    preInfinity = pm.getAttr(ani_node + '.preInfinity')
                    postInfinity = pm.getAttr(ani_node + '.postInfinity')
                    keyTimes = pm.keyframe(obj.nodeName() + '.' + attr, query=True, tc=True)
                    value = pm.keyframe(obj.nodeName() + '.' + attr, query=True, vc=True)
                    obj_dict[obj][attr] = {}
                    obj_dict[obj][attr]['infinity'] = [preInfinity, postInfinity]
                    obj_dict[obj][attr]['keyTimes'] = keyTimes
                    obj_dict[obj][attr]['values'] = value
            if len(obj_dict[obj]) > 0:
                all_dict.update(obj_dict)
        return all_dict

    def setKeyToAniLayer(self, all_dict):
        ani_layer = self.setAniLayer_LE.text()
        mel = 'selectLayer("' + ani_layer + '");'
        pm.mel.eval(mel)
        for obj in all_dict:
            pm.select(obj)
            pm.animLayer(ani_layer, edit=True, addSelectedObjects=True)
            for attr in all_dict[obj]:
                for index, key in enumerate(all_dict[obj][attr]['keyTimes']):
                    # print "key: %s" % key
                    value = all_dict[obj][attr]['values'][index]
                    # print "value: %s" % value
                    pm.setKeyframe(obj, animLayer=ani_layer, at=attr, e=True, time=(key), noResolve=True, value=value)
                    ani_node = pm.keyframe(obj.nodeName() + '.' + attr, name=True, query=True)[0]
                    pm.setAttr(ani_node + '.preInfinity', all_dict[obj][attr]['infinity'][0])
                    pm.setAttr(ani_node + '.postInfinity', all_dict[obj][attr]['infinity'][1])

    def setAniLayer_PB_hit(self):
        all_dict = self.anyLayerKeyFrameData()
        self.setKeyToAniLayer(all_dict)

    def clearAllKey_PB_hit(self):
        '''
        root_joint = self.rootJoint_LE.text()
        root_joint = pm.PyNode(root_joint)
        joint_list = pm.listRelatives(root_joint, allDescendents=True, type='joint')
        joint_list.append(root_joint)
        all_ani_node = []
        for joint in joint_list:
            ani_node_list = pm.keyframe(joint, name=True, query=True)
            all_ani_node = all_ani_node + ani_node_list
        pm.undoInfo(ock=True)
        pm.delete(all_ani_node)
        pm.undoInfo(cck=True)
        '''
        pm.currentTime(1)
        sel_list = pm.ls(selection=True)
        get_joint_list = []
        get_mesh_list = []
        for obj in sel_list:
            joint_list = pm.listRelatives(obj, allDescendents=True, type='joint')
            mesh_list = pm.listRelatives(obj, allDescendents=True, type='mesh')
            get_mesh_list = get_mesh_list + mesh_list
            get_joint_list.append(obj)
            get_joint_list = get_joint_list + joint_list
        '''
        all_ani_node = []
        for joint in get_joint_list:
            ani_node_list = pm.keyframe(joint, name=True, query=True)
            all_ani_node = all_ani_node + ani_node_list
        '''
        pm.undoInfo(ock=True)
        current_aniLayer = pm.treeView("AnimLayerTabanimLayerEditor", q=True, selectItem=True)
        for joint in get_joint_list:
            keyable_list = pm.listAttr(joint, keyable=True)
            for attr in keyable_list:
                pm.animLayer(current_aniLayer, edit=True, removeAttribute=joint.name() + '.' + attr)
        for mesh in get_mesh_list:
            mesh_t = mesh.getTransform()
            second_joint = pm.listRelatives(mesh_t, fullPath=True, parent=True)
            pm.select(second_joint)
            pm.animLayer(current_aniLayer, edit=True, addSelectedObjects=True)
            pm.setKeyframe(second_joint, attribute='alphaGain', t=[1, 1], v=0)
        pm.undoInfo(cck=True)

    def getChildJoint_PB_hit(self):
        sel_list = pm.ls(selection=True)
        get_joint_list = []
        for obj in sel_list:
            joint_list = pm.listRelatives(obj, allDescendents=True, type='joint')
            get_joint_list.append(obj)
            get_joint_list = get_joint_list + joint_list
        pm.select(get_joint_list)


class checkBox_class(QtWidgets.QCheckBox):
    def __init__(self, parent, node):
        QtWidgets.QCheckBox.__init__(self)
        self.parent = parent
        self.node = node
        self.setText(node.name())
        self.stateChanged.connect(self.checkValue)

    def checkValue(self):
        pass
        '''
        if self.checkState() == QtCore.Qt.Checked:
            if self.node not in self.parent.animLayer_cb_list:
                self.parent.animLayer_cb_list.append(self.node)
        elif self.checkState() == QtCore.Qt.Unchecked:
            if self.node in self.parent.animLayer_cb_list:
                self.parent.animLayer_cb_list.remove(self.node)
        self.parent.animLayer_cb_list.sort()
        print self.parent.animLayer_cb_list
        '''


class pixiTools_particleEdit_ui(QtWidgets.QWidget, pixiTools_particleEdit_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(pixiTools_particleEdit_ui, self).__init__(parent)
        self.setupUi(self)
        regx = QtCore.QRegExp("[0-9]+$")
        self.onlyInt = QtGui.QRegExpValidator(regx)
        # self.randomKeyMin_LE.setValidator(self.onlyInt)
        # self.randomKeyMax_LE.setValidator(self.onlyInt)
        self.startFrame_LE.setValidator(self.onlyInt)
        self.startFrameLoop_LE.setValidator(self.onlyInt)
        self.endFrameLoop_LE.setValidator(self.onlyInt)
        self.frequency_LE.setValidator(self.onlyInt)
        self.centerFrame_LE.setValidator(self.onlyInt)
        self.attr_button_group = QtWidgets.QButtonGroup()
        self.attr_button_group.addButton(self.translateX_RB)
        self.attr_button_group.addButton(self.translateY_RB)
        self.attr_button_group.addButton(self.scale_RB)
        self.attr_button_group.addButton(self.scaleX_RB)
        self.attr_button_group.addButton(self.scaleY_RB)
        self.attr_button_group.addButton(self.rotateZ_RB)
        self.attr_button_group.addButton(self.alphaGain_RB)
        self.attr_button_group.addButton(self.colorGain_RB)
        self.attr_set_type_group = QtWidgets.QButtonGroup()
        self.attr_set_type_group.addButton(self.offset_RB)
        self.attr_set_type_group.addButton(self.replace_RB)
        self.connectInterface()
        self.setDefault()

    def connectInterface(self):
        self.deleteKey_PB.clicked.connect(self.deleteKey_PB_hit)
        self.startFrameSet_PB.clicked.connect(self.startFrameSet_PB_hit)
        self.randomKeySet_PB.clicked.connect(self.randomKeySet_PB_hit)
        self.instanceGrpName_PB.clicked.connect(self.instanceGrpName_PB_hit)
        self.textureFileBro_PB.clicked.connect(self.textureFileBro_PB_hit)
        self.textureFileOpen_PB.clicked.connect(self.textureFileOpen_PB_hit)
        self.createPlane_PB.clicked.connect(self.createPlane_PB_hit)
        self.convertJointMode_PB.clicked.connect(self.convertJointMode_PB_hit)
        self.goLoop_PB.clicked.connect(self.goLoop_PB_hit)
        self.randomValueSetKey_PB.clicked.connect(self.randomValueSetKey_PB_hit)
        self.scaleConvertValue_PB.clicked.connect(self.scaleConvertValue_PB_hit)
        self.translateConvertValue_PB.clicked.connect(self.translateConvertValue_PB_hit)
        self.speedConvertTime_PB.clicked.connect(self.speedConvertTime_PB_hit)
        self.motionPathAddCurve_PB.clicked.connect(self.motionPathAddCurve_PB_hit)
        self.add_joint_PB.clicked.connect(self.add_joint_PB_hit)
        self.curveAttach_PB.clicked.connect(self.curveAttach_PB_hit)
        self.resetPosition_PB.clicked.connect(self.resetPosition_PB_hit)
        self.autoSetRotationKey_PB.clicked.connect(self.autoSetRotationKey_PB_hit)

    def setDefault(self):
        pass

    def deleteKey_PB_hit(self):
        grp_name = self.instanceGrpName_LE.text()
        grp_node = pm.PyNode(grp_name)
        pm.undoInfo(ock=True)
        mesh_list = pm.listRelatives(grp_node, allDescendents=True, type='mesh')
        for mesh in mesh_list:
            key_list = pm.keyframe(mesh.getTransform(), attribute='translateX', query=True, cp=False)
            if len(key_list) > 2:
                self.fixInstanceKey(mesh.getTransform(), 'translateX', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'translateY', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'translateZ', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'rotateX', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'rotateY', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'rotateZ', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'scaleX', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'scaleY', key_list)
                self.fixInstanceKey(mesh.getTransform(), 'scaleZ', key_list)
        pm.undoInfo(cck=True)

    def fixInstanceKey(self, mesh, attr, key_list):
        min_frame = int(key_list[1])
        max_frame = int(key_list[-2])
        pm.cutKey(mesh, time=(min_frame, max_frame), attribute=attr, option="keys")
        pm.keyTangent(mesh, time=(key_list[0]), attribute=attr, ott='linear')
        pm.keyTangent(mesh, time=(key_list[0]), attribute=attr, itt='linear')
        pm.keyTangent(mesh, time=(key_list[-1]), attribute=attr, ott='linear')
        pm.keyTangent(mesh, time=(key_list[-1]), attribute=attr, itt='linear')

    def textureFileBro_PB_hit(self):
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        if file != "":
            self.textureFile_LE.setText(file)
            im = Image.open(file)
            width, height = im.size
            self.texWidth_LE.setText(str(width))
            self.texHeight_LE.setText(str(height))

    def textureFileOpen_PB_hit(self):
        file = self.textureFile_LE.text()
        path = os.path.split(file)[0]
        path = path.replace('/', '\\')
        os.startfile(path)

    def createPlane_PB_hit(self):
        width = int(self.texWidth_LE.text())
        height = int(self.texHeight_LE.text())
        image_plane = pm.polyPlane(n='baseImage_mesh')
        image_plane[1].setAttr('subdivisionsHeight', 1)
        image_plane[1].setAttr('subdivisionsWidth', 1)
        image_plane[0].setAttr("rotateX", 90)
        cmds.makeIdentity(image_plane[0].name(), apply=True, rotate=True)
        image_plane[0].setAttr("scaleX", width)
        image_plane[0].setAttr("scaleY", height)

    def startFrameSet_PB_hit(self):
        pm.undoInfo(ock=True)
        start_frame = int(self.startFrame_LE.text())
        mesh_list = pm.ls(selection=True)
        for mesh in mesh_list:
            self.unlockAttr(mesh)
            attr_list = pm.listAttr(mesh, keyable=True)
            for attr in attr_list:
                key_list = pm.keyframe(mesh, attribute=attr, query=True, cp=False)
                if len(key_list) > 0:
                    offset_value = start_frame - key_list[0]
                    pm.keyframe(mesh, edit=True, attribute=attr, includeUpperBound=True, relative=True, timeChange=offset_value, time=(key_list[0], key_list[-1]))
        pm.undoInfo(cck=True)

    def unlockAttr(self, mesh):
        attr_list = pm.listAttr(mesh, channelBox=True)
        for attr in attr_list:
            mesh.setAttr(attr, keyable=True)
        attr_list = pm.listAttr(mesh, locked=True)
        for attr in attr_list:
            mesh.setAttr(attr, lock=False)

    def randomKeySet_PB_hit(self):
        pm.undoInfo(ock=True)
        min_key = int(self.randomKeyMin_LE.text())
        max_key = int(self.randomKeyMax_LE.text())
        mesh_list = pm.ls(selection=True)
        for mesh in mesh_list:
            self.unlockAttr(mesh)
            value = random.randint(min_key, max_key)
            attr_list = pm.listAttr(mesh, keyable=True)
            for attr in attr_list:
                key_list = pm.keyframe(mesh, attribute=attr, query=True, cp=False)
                if len(key_list) > 0:
                    offset_value = value - key_list[0]
                    pm.keyframe(mesh, edit=True, attribute=attr, includeUpperBound=True, relative=True, timeChange=offset_value, time=(key_list[0], key_list[-1]))
        pm.undoInfo(cck=True)

    def instanceGrpName_PB_hit(self):
        grp = pm.ls(selection=True, tail=True)[0]
        self.instanceGrpName_LE.setText(grp.name())

    def goLoop_PB_hit(self):
        pm.undoInfo(ock=True)
        min_frame = int(self.startFrameLoop_LE.text())
        max_frame = int(self.endFrameLoop_LE.text())
        frequency = int(self.frequency_LE.text())
        node_list = pm.ls(sl=True)
        for node in node_list:
            attr_list = pm.listAttr(node, keyable=True)
            for attr in attr_list:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                if len(key_list) > 0:
                    for i in range(frequency):
                        self.loopKey(node, min_frame, max_frame, attr, i + 1)
        pm.undoInfo(cck=True)

    def loopKey(self, node, min_frame, max_frame, attr, frequency):
        pm.copyKey(node, time=(min_frame, max_frame), attribute=attr, option="keys")
        frame_range = max_frame - min_frame + 1
        pasteKey = frame_range * frequency + 1
        pm.pasteKey(node, time=(pasteKey), attribute=attr)

    def convertJointMode_PB_hit(self):
        grp_name = self.instanceGrpName_LE.text()
        grp_node = pm.PyNode(grp_name)
        mesh_list = pm.listRelatives(grp_node, allDescendents=True, type='mesh')
        pm.select(clear=True)
        root_joint = pm.joint(name="root_joint", p=[0, 0, 0])
        pm.select(clear=True)
        width = float(self.texWidth_LE.text())
        height = float(self.texHeight_LE.text())
        for num, mesh in enumerate(mesh_list):
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
            cmds.addAttr(longName='fadeGain', defaultValue=1.0, minValue=0, maxValue=1, keyable=True)
            cmds.addAttr(longName='colorGain', usedAsColor=True, attributeType='float3', keyable=True)
            cmds.addAttr(longName='colorGainR', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainG', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='colorGainB', defaultValue=1.0, attributeType='float', parent='colorGain', keyable=True)
            cmds.addAttr(longName='blendMode', attributeType="enum", enumName="normal:multiply:additive:screen", keyable=True)
            cmds.addAttr(longName='startFrame', defaultValue=1, attributeType="long", keyable=True)
            pm.parent(second_joint, root_joint, relative=True)
            pm.parent(image_plane[0], second_joint, relative=True)
            key_list = pm.keyframe(mesh.getTransform(), attribute='translateX', query=True, cp=False)
            for key in key_list:
                pm.currentTime(key)
                value = mesh.getTransform().getAttr('translateX')
                pm.setKeyframe(second_joint, v=value, at='translateX', time=key)
                value = mesh.getTransform().getAttr('translateY')
                pm.setKeyframe(second_joint, v=value, at='translateY', time=key)
                value = mesh.getTransform().getAttr('translateZ')
                pm.setKeyframe(second_joint, v=value, at='translateZ', time=key)
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateX', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateX', itt='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateY', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateY', itt='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateZ', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='translateZ', itt='linear')
            key_list = pm.keyframe(mesh.getTransform(), attribute='rotateZ', query=True, cp=False)
            for key in key_list:
                pm.currentTime(key)
                value = mesh.getTransform().getAttr('rotateZ')
                pm.setKeyframe(second_joint, v=value, at='rotateZ', time=key)
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='rotateZ', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='rotateZ', itt='linear')
            key_list = pm.keyframe(mesh.getTransform(), attribute='scaleX', query=True, cp=False)
            for key in key_list:
                pm.currentTime(key)
                value = mesh.getTransform().getAttr('scaleX')
                value = value/width
                pm.setKeyframe(second_joint, v=value, at='scaleX', time=key)
                value = mesh.getTransform().getAttr('scaleY')
                value = value/height
                pm.setKeyframe(second_joint, v=value, at='scaleY', time=key)
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='scaleX', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='scaleX', itt='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='scaleY', ott='linear')
            pm.keyTangent(second_joint, time=(key_list[0], key_list[-1]), attribute='scaleY', itt='linear')

    def randomValueSetKey_PB_hit(self):
        pm.undoInfo(ock=True)
        minValue = float(self.minValue_LE.text())
        maxValue = float(self.maxValue_LE.text())
        keyIndex_str = self.keyIndex_LE.text()
        keyIndex_list = keyIndex_str.split(',')
        attr = self.attr_button_group.checkedButton().text()
        set_key_type = self.attr_set_type_group.checkedButton().text()
        node_list = pm.ls(sl=True)
        for node in node_list:
            random_value = random.uniform(minValue, maxValue)
            if attr == 'scale':
                attr_list = ['scaleY', 'scaleX']
                for attr_scale in attr_list:
                    key_list = pm.keyframe(node, attribute=attr_scale, query=True, cp=False)
                    self.randomValueSetKeyControl(node, attr_scale, key_list, keyIndex_list, set_key_type, random_value)
            elif attr == 'colorGain':
                attr_list = ['colorGainR', 'colorGainG', 'colorGainB']
                for attr_color in attr_list:
                    key_list = pm.keyframe(node, attribute=attr_color, query=True, cp=False)
                    self.randomValueSetKeyControl(node, attr_color, key_list, keyIndex_list, set_key_type, random_value)
            else:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                self.randomValueSetKeyControl(node, attr, key_list, keyIndex_list, set_key_type, random_value)
        pm.undoInfo(cck=True)

    def randomValueSetKeyControl(self, node, attr, key_list, keyIndex_list, set_key_type, random_value):
        key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
        if set_key_type == 'offset':
            if keyIndex_list[0] == 'all':
                for key in key_list:
                    pm.keyframe(node, edit=True, attribute=attr, time=key, relative=True, valueChange=random_value)
            else:
                for index in keyIndex_list:
                    pm.keyframe(node, edit=True, attribute=attr, time=key_list[int(index)], relative=True, valueChange=random_value)
        elif set_key_type == 'replace':
            if keyIndex_list[0] == 'all':
                for key in key_list:
                    pm.keyframe(node, edit=True, attribute=attr, time=key, valueChange=random_value)
            else:
                for index in keyIndex_list:
                    pm.keyframe(node, edit=True, attribute=attr, time=key_list[int(index)], valueChange=random_value)

    def translateConvertValue_PB_hit(self):
        pm.undoInfo(ock=True)
        node_list = pm.ls(sl=True)
        adjustment_value = self.translate_SB.value()
        for node in node_list:
            attr_list = ['translateX', 'translateY']
            for attr in attr_list:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                for key in key_list:
                    value = pm.keyframe(node, query=True, attribute=attr, time=key, valueChange=True)[0]
                    value = round(value * adjustment_value, 3)
                    pm.keyframe(node, edit=True, attribute=attr, time=key, valueChange=value)
        pm.undoInfo(cck=True)

    def scaleConvertValue_PB_hit(self):
        pm.undoInfo(ock=True)
        node_list = pm.ls(sl=True)
        adjustment_value = self.scale_SB.value()
        for node in node_list:
            attr_list = ['scaleX', 'scaleY']
            for attr in attr_list:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                for key in key_list:
                    value = pm.keyframe(node, query=True, attribute=attr, time=key, valueChange=True)[0]
                    value = round(value * adjustment_value, 3)
                    pm.keyframe(node, edit=True, attribute=attr, time=key, valueChange=value)
        pm.undoInfo(cck=True)

    def speedConvertTime_PB_hit(self):
        pm.undoInfo(ock=True)
        node_list = pm.ls(sl=True)
        adjustment_value = self.speed_SB.value()
        centerFrame = float(self.centerFrame_LE.text())
        if adjustment_value == 1:
            return
        for node in node_list:
            self.unlockAttr(node)
            attr_list = pm.listAttr(node, keyable=True)
            for attr in attr_list:
                key_list = pm.keyframe(node, attribute=attr, query=True, cp=False)
                if len(key_list) > 0:
                    pre_key_list = []
                    past_key_list = []
                    for key in key_list:
                        if key < centerFrame:
                            pre_key_list.append(key)
                        elif key > centerFrame:
                            past_key_list.append(key)
                    if adjustment_value > 1:
                        past_key_list.reverse()
                    elif adjustment_value < 1:
                        pre_key_list.reverse()
                    all_key_list = pre_key_list+past_key_list
                    for key in all_key_list:
                        ture_key = key - centerFrame
                        ture_key = round(ture_key * adjustment_value, 3)
                        ture_key = ture_key + centerFrame
                        pm.keyframe(node, edit=True, attribute=attr, timeChange=ture_key, time=(key))
        pm.undoInfo(cck=True)

    def curveAttach_PB_hit(self):
        s_frame = int(self.motionPathStartFrame_LE.text())
        e_frame = int(self.motionPathEndFrame_LE.text())
        keys = int(self.motionPathKeys_LE.text())
        pow_num = float(self.motionPathPow_LE.text())
        key_list, value_list = self.curve_key_convert(s_frame, e_frame, keys, pow_num)
        curve_list = self.motionPathCurve_LE.text().split(',')
        curve_max = len(curve_list)
        joint_list = self.joint_list_LE.text().split(',')
        motion_path_list = []
        self.resetPosition_PB_hit()
        for index, joint in enumerate(joint_list):
            num = index % curve_max
            joint_node = pm.PyNode(joint)
            curve_node = pm.PyNode(curve_list[num])
            motion_path = pm.pathAnimation(joint_node, c=curve_node, fractionMode=True, follow=True, followAxis='y', upAxis='z', worldUpType='vector', worldUpVector=[0, 0, 1], inverseUp=False, inverseFront=False, startTimeU=s_frame, endTimeU=e_frame)
            motion_path_list.append(motion_path)
        for motion_path in motion_path_list:
            for index, key in enumerate(key_list):
                if index != 0 and index != len(key_list) - 1:
                    value = value_list[index]
                    pm.setKeyframe(motion_path, t=[key], at='u', v=value)
        key_all_data_dict = {}
        for joint in joint_list:
            joint = pm.PyNode(joint)
            motion_path_node = pm.listConnections(joint.specifiedManipLocation, d=False, s=True, type='motionPath')[0]
            key_list = pm.keyframe(motion_path_node, query=True, at='u')
            key_all_data_dict[joint.name()] = {}
            for key in key_list:
                cmds.currentTime(key)
                key_all_data_dict[joint.name()][str(key)] = {}
                key_all_data_dict[joint.name()][str(key)]['tx'] = round(joint.getAttr('translateX'), 2)
                key_all_data_dict[joint.name()][str(key)]['ty'] = round(joint.getAttr('translateY'), 2)
                key_all_data_dict[joint.name()][str(key)]['rz'] = round(joint.getAttr('rotateZ'), 2)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(key_all_data_dict)
        self.resetPosition_PB_hit()
        for joint in key_all_data_dict:
            joint_node = pm.PyNode(joint)
            for key in key_all_data_dict[joint]:
                tx = key_all_data_dict[joint][key]['tx']
                ty = key_all_data_dict[joint][key]['ty']
                rz = key_all_data_dict[joint][key]['rz']
                pm.setKeyframe(joint_node, t=[float(key)], at='translateX', v=tx)
                pm.setKeyframe(joint_node, t=[float(key)], at='translateY', v=ty)
                pm.setKeyframe(joint_node, t=[float(key)], at='rotateZ', v=rz)
            pm.filterCurve(joint_node.rotateZ)

    def resetPosition_PB_hit(self):
        joint_list = self.joint_list_LE.text().split(',')
        for joint in joint_list:
            self.deleteMotionPath(joint)

    def deleteMotionPath(self, joint_node):
        node = pm.PyNode(joint_node)
        # del_attr_list = [node.tx, node.ty, node.tz, node.rx, node.ry, node.rz, node.alphaGain]
        del_attr_list = [node.tx, node.ty, node.tz, node.rx, node.ry, node.rz]
        for del_attr in del_attr_list:
            attr_list = pm.listConnections(del_attr, d=False, s=True, p=True)
            if len(attr_list) > 0:
                for attr in attr_list:
                    pm.disconnectAttr(attr, del_attr)
        motion_node_list = pm.listConnections(node.specifiedManipLocation, d=False, s=True, type='motionPath')
        pm.delete(motion_node_list)
        node.setAttr('translateX', 0)
        node.setAttr('translateY', 0)
        node.setAttr('translateZ', 0)
        node.setAttr('rotateX', 0)
        node.setAttr('rotateY', 0)
        node.setAttr('rotateZ', 0)
        # node.setAttr('alphaGain', 1)

    def curve_key_convert(self, s_frame, e_frame, keys, pow_num):
        if pow_num != 1 and pow_num != 0:
            log_list = []
            for i in range(keys + 1):
                num = round(math.pow(pow_num, i), 3)
                log_list.append(num)
            rate_list = []
            for i in log_list:
                rate = (i - log_list[0]) / (log_list[-1] - log_list[0])
                rate = round(rate, 3)
                rate_list.append(rate)

            key_list = []
            for rate in rate_list:
                num = (e_frame - s_frame) * rate + s_frame
                num = round(num, 3)
                key_list.append(num)

            value_list = [0]
            for i in range(keys):
                value = 1 / float(keys) * (i + 1)
                value = round(value, 2)
                value_list.append(value)
            return key_list, value_list

        elif pow_num == 1:
            key_list = [s_frame]
            for i in range(keys):
                key = s_frame + (e_frame - s_frame) / float(keys) * (i + 1)
                key = round(key, 2)
                key_list.append(key)

            value_list = [0]
            for i in range(keys):
                value = 1 / float(keys) * (i + 1)
                value = round(value, 2)
                value_list.append(value)
            return key_list, value_list

    def motionPathAddCurve_PB_hit(self):
        node_list = pm.ls(sl=True)
        curve_list = []
        for node in node_list:
            if node.getShape().type() == "nurbsCurve":
                curve_list.append(node)
        name_list = []
        for curve in curve_list:
            name_list.append(curve.name())
        node_text = ', '.join(name_list)
        self.motionPathCurve_LE.setText(node_text)
        to_list = node_text.split()

    def add_joint_PB_hit(self):
        node_list = pm.ls(sl=True)
        joint_list = []
        for node in node_list:
            if node.type() == "joint":
                joint_list.append(node)
        name_list = []
        for joint in joint_list:
            name_list.append(joint.name())
        node_text = ', '.join(name_list)
        self.joint_list_LE.setText(node_text)
        to_list = node_text.split()

    def autoSetRotationKey_PB_hit(self):
        root_node = pm.ls(sl=True, tail=True)[0]
        # root_grp = pm.PyNode(root_node)
        joint_list = pm.listRelatives(root_node, allDescendents=True, type='joint')
        # temp_joint_list = pm.listRelatives(root_grp, allDescendents=True, type='joint')
        # joint_list = filter(lambda x: pm.getAttr('%s.spine_tag' % (x)) == "spine_bone", temp_joint_list)
        set_key_dict = {}
        for joint in joint_list:
            count = pm.keyframe(joint, q=True, keyframeCount=True, attribute='rotateZ')
            if count > 1:
                obj_dict = self.setRotateKey(joint, count)
                set_key_dict[joint] = obj_dict
        pm.undoInfo(ock=True)
        for obj in set_key_dict:
            for frame in set_key_dict[obj]:
                volue = set_key_dict[obj][frame]
                pm.setKeyframe(obj, t=[frame, frame], at='rz', v=volue)
        pm.undoInfo(cck=True)

    def setRotateKey(self, obj, count):
        obj_dict = {}
        frame_list = pm.keyframe(obj, q=True, timeChange=True, attribute='rotateZ', index=(0, count))
        volue_list = pm.keyframe(obj, q=True, valueChange=True, attribute='rotateZ', index=(0, count))
        for i in range(count):
            if i + 1 != count:
                volue_1 = volue_list[i]
                volue_2 = volue_list[i + 1]
                distance = volue_2 - volue_1
                if abs(distance) > 179:
                    if distance >= 0:
                        start_volue = 0
                        while start_volue + 179 < distance:
                            start_volue = start_volue + 179
                            volue_ratio = start_volue / distance
                            set_volue = start_volue + volue_1
                            # print 'set_volue : %s' % (set_volue)
                            frame_range = frame_list[i + 1] - frame_list[i]
                            set_frame = frame_range * volue_ratio + frame_list[i]
                            # print 'set_frame : %s' % (set_frame)
                            obj_dict[str(set_frame)] = set_volue
                    else:
                        start_volue = 0
                        while start_volue - 179 > distance:
                            start_volue = start_volue - 179
                            volue_ratio = start_volue / distance
                            set_volue = start_volue - volue_1
                            # print 'set_volue : %s' % (set_volue)
                            frame_range = frame_list[i + 1] - frame_list[i]
                            set_frame = frame_range * volue_ratio + frame_list[i]
                            # print 'set_frame : %s' % (set_frame)
                            obj_dict[set_frame] = set_volue
        return obj_dict


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
