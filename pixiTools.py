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
maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
sys.path.append(ui_path)
# sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
import pixiTools_export_json_ui
reload(pixiTools_export_json_ui)

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
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.pixiTools_export_json_wid, "export Json")
        username = getpass.getuser()
        self.python_temp = 'C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp+'/pixiTools.csv'
        self.layout().addWidget(main_tab_Widget)
        self.save_UI_list = [
            self.pixiTools_export_json_wid.objGrp_LE,
            self.pixiTools_export_json_wid.instanceGrp_LE,
            self.pixiTools_export_json_wid.sourceCam_LE,
            self.pixiTools_export_json_wid.canvasCam_LE,
            self.pixiTools_export_json_wid.outDir_LE,
            self.pixiTools_export_json_wid.json_LE
        ]
        self.setFromCsv()

    def closeEvent(self, event):
        self.writeCsv()

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

    def getValue(self, widget):
        if type(widget) == QtWidgets.QLineEdit:
            return widget.text()


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
        self.sourceCam_setUp_PB.clicked.connect(self.sourceCam_setUp_PB_hit)
        self.canvasCam_setUp_PB.clicked.connect(self.canvasCam_setUp_PB_hit)
        self.shaderSetToDefault_PB.clicked.connect(self.shaderSetToDefault_PB_hit)
        self.frameRangeTime_CB.currentIndexChanged.connect(self.frameRangeTime_CB_hit)

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
                    tranform = cmds.particle(
                        node_t, q=True, id=pid, attribute='position')
                    scale_range = cmds.nParticle(
                        node_t, q=True, id=pId, attribute='customScalePP')

    def setResolution(self):
        width = int(self.sourceSizeW_LE.text())
        height = int(self.sourceSizeH_LE.text())
        # cmds.setAttr("defaultResolution.width", width)
        # cmds.setAttr("defaultResolution.height", height)

    def createPlane_PB_hit(self):
        width = int(self.createPlaneW_LE.text())
        height = int(self.createPlaneH_LE.text())
        image_plane = pm.polyPlane(n='pixiImagePlane')
        image_plane[1].setAttr('subdivisionsHeight', 1)
        image_plane[1].setAttr('subdivisionsWidth', 1)
        image_plane[0].setAttr("rotateX", 90)
        cmds.makeIdentity(image_plane[0].name(), apply=True, rotate=True)
        image_plane[0].setAttr("scaleX", width)
        image_plane[0].setAttr("scaleY", height)
        # cmds.delete(image_plane[0].name(),ch=True)

    def sourceCam_setUp_PB_hit(self):
        width = float(self.sourceSizeW_LE.text())
        height = float(self.sourceSizeH_LE.text())
        ratio = width / height
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultResolution.deviceAspectRatio", ratio)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        self.setCamera('sourceCam', width)
        self.setRenderLayer('source_RL')

    def canvasCam_setUp_PB_hit(self):
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
        return [(nuPoint[0]/nuPoint[3]/2+0.5)*res[0],
                (1-(nuPoint[1]/nuPoint[3]/2+0.5))*res[1]]

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
        sequence = self.getTextureInfo(mesh_list[0])[0]
        instance_big_grp = self.instanceGrp_LE.text()
        transform_list = pm.listRelatives(
            instance_big_grp, ad=True, type='transform')
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
        shader = pm.listConnections(
            SG.surfaceShader, d=False, s=True, type='lambert')[0]
        file = pm.listConnections(
            shader.color, d=False, s=True, type='file')[0]
        sequence = file.getAttr('useFrameExtension')
        alpha = file.getAttr('alphaGain')
        fileImage = file.getAttr('fileTextureName')
        basename = os.path.basename(fileImage)
        alpha = round(alpha, 2)

        if sequence is True:
            index = file.getAttr('frameExtension')
        else:
            index = None
        return sequence, index, alpha, basename

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
        self.info_label.setText("Done")

    def getInstanceInfo(self, f_min, f_max, step, camera, width, height):
        instance_big_grp = self.instanceGrp_LE.text()
        transform_list = pm.listRelatives(instance_big_grp, ad=True, type='transform')
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
            abc_node = pm.listConnections(
                mesh_list[0].getTransform(), type='AlembicNode')
            if len(abc_node) > 0:
                offset = abc_node[0].getAttr('offset')
                instance_dict['instancer_'+ID]['offset'] = offset
            else:
                instance_dict['instancer_'+ID]['offset'] = 0
            for f in xrange(f_min, f_max+1, step):
                cmds.currentTime(f)
                positionPP = cmds.getAttr(instancer_grp+'.translate')[0]
                camera_positon = self.pointWorldToCam(camera, positionPP, (width, height))
                instance_dict['instancer_'+ID]['translate'].append(
                    {"time": f, "x": int(camera_positon[0]), "y": int(camera_positon[1]), "trans": 1})
                rotationPP = cmds.getAttr(instancer_grp+'.rotate')[0]
                rotation_z = int(rotationPP[2])
                if rotation_z < 0:
                    fix_angle = 360+(rotation_z % 360)
                else:
                    fix_angle = rotation_z % 360
                instance_dict['instancer_' + ID]['rotate'].append({"time": f, "angle": int(fix_angle)})
                scalePP = cmds.getAttr(instancer_grp+'.scale')[0]
                scale_w = round(scalePP[0],2)
                scale_h = round(scalePP[1],2)
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
        currentRL = pm.editRenderLayerGlobals(
            query=True, currentRenderLayer=True)
        trans_list = pm.ls(selection=True, type='transform', long=True)
        mesh_list = []
        for i in trans_list:
            if i.getShape().type() == "mesh":
                mesh_list.append(i)
        if currentRL != 'defaultRenderLayer':
            for mesh in mesh_list:
                print mesh.name()
                SG = pm.listConnections(
                    mesh.getShape(), type='shadingEngine')[0]
                pm.editRenderLayerGlobals(
                    currentRenderLayer='defaultRenderLayer')
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
