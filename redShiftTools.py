# -*- coding: utf-8 -*-
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import maya.cmds as cmds
import pymel.core as pm
import os
import getpass
import csv
import sys
import colorsys
maya_version=cmds.about(version=True)
username=getpass.getuser()
ui_path='C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
import redShiftTools_objSet_ui;reload(redShiftTools_objSet_ui)
import redShiftTools_objSet_mesh_ui;reload(redShiftTools_objSet_mesh_ui)
import redShiftTools_objSet_matte_ui;reload(redShiftTools_objSet_matte_ui)
import redShiftTools_objSet_objectId_ui;reload(redShiftTools_objSet_objectId_ui)
import redShiftTools_objSet_visbility_ui;reload(redShiftTools_objSet_visbility_ui)
import srgbtransform;reload(srgbtransform)

dialog=None



def checkPlugin(name_list):
    for i in name_list:
        if cmds.pluginInfo( i, q=True, l=True ) == False:
            cmds.loadPlugin(i)

plugin_list=['redshift4maya.mll']
checkPlugin(plugin_list)

#---------------------------------------------------------------------------------------------------#
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('redShift tools'+' v0.5'+u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800,600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0,0,0,0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.redShiftTools_objSet_wid=redShiftTools_objSet_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.redShiftTools_objSet_wid, "obj sets")
        username=getpass.getuser()
        self.python_temp='C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv=self.python_temp+'/redShfitTools.csv'
        self.layout().addWidget(main_tab_Widget)
        self.save_UI_list=[]
        self.setFromCsv()

    def closeEvent(self, event):
        self.writeCsv()

    def writeCsv(self):
        if os.path.exists(self.python_temp) == False:
            os.mkdir(self.python_temp)
        data=[['var_name','value']]
        for obj in self.save_UI_list:
            obj_info=[obj.objectName(),self.getValue(obj)]
            data.append(obj_info)
        file = open(self.python_temp_csv,'w')
        w = csv.writer(file)
        w.writerows(data)
        file.close()

    def setFromCsv(self):
        if os.path.exists(self.python_temp_csv):
            cache_value_list=[]
            file = open(self.python_temp_csv, 'r')
            for i in csv.DictReader(file):
                cache_value_list.append(i['value'])
            file.close()
            for index,value in enumerate(cache_value_list):
                self.save_UI_list[index].setText(value)

    def getValue(self,widget):
        if type(widget)==QtWidgets.QLineEdit:
            return widget.text()

#---------------------------------------------------------------------------------------------------#
class redShiftTools_objSet_ui(QtWidgets.QWidget,redShiftTools_objSet_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(redShiftTools_objSet_ui, self).__init__(parent)
        self.setupUi(self) 
        self.connectInterface()
        self.getObjSets()

    def connectInterface(self):
        self.objectID_PB.clicked.connect(self.objectID_PB_hit)
        self.visibility_PB.clicked.connect(self.visibility_PB_hit)
        self.meshParameters_PB.clicked.connect(self.meshParameters_PB_hit)
        self.matte_PB.clicked.connect(self.matte_PB_hit)
        self.del_PB.clicked.connect(self.del_PB_hit)
        self.attach_PB.clicked.connect(self.attach_PB_hit)
        self.detach_PB.clicked.connect(self.detach_PB_hit)
        self.select_PB.clicked.connect(self.select_PB_hit)
        self.objSets_listWidget.itemClicked.connect(self.checkAttrUi)
        self.objSets_listWidget.itemChanged.connect(self.editItemName)
 
    def getObjSets(self):
        self.clearLayout(self.attr_scrollAreaWidgetContents.layout())
        self.objSets_listWidget.clear()
        type_list=["RedshiftObjectId","RedshiftVisibility","RedshiftMeshParameters","RedshiftMatteParameters"]
        objSets_list=pm.ls(type=type_list)
        for i in objSets_list:
            ltem_class=obj_properties_listItem(i)
            self.objSets_listWidget.addItem(ltem_class)

    def editItemName(self,item):
        item.node.rename(item.text())

    def objectID_PB_hit(self):
        pm.createNode( 'RedshiftObjectId')
        self.getObjSets()

    def visibility_PB_hit(self):
        pm.createNode( 'RedshiftVisibility')
        self.getObjSets()

    def meshParameters_PB_hit(self):
        pm.createNode( 'RedshiftMeshParameters')
        self.getObjSets()

    def matte_PB_hit(self):
        pm.createNode( 'RedshiftMatteParameters')
        self.getObjSets()

    def attach_PB_hit(self):
        parameter_node=self.objSets_listWidget.currentItem().node
        type_list=['mesh','nurbsSurface']
        selected_list=pm.ls(sl=True)
        obj_list=[]
        for i in selected_list:
            if i.getShape().type() in type_list:
                obj_list.append(i)
        pm.sets(parameter_node,forceElement=obj_list)

    def detach_PB_hit(self):
        parameter_node=self.objSets_listWidget.currentItem().node
        type_list=['mesh','nurbsSurface']
        selected_list=pm.ls(sl=True)
        obj_list=[]
        for i in selected_list:
            if i.getShape().type() in type_list:
                obj_list.append(i)
        pm.sets(parameter_node,remove =obj_list)

    def select_PB_hit(self):
        parameter_node=self.objSets_listWidget.currentItem().node
        node_list=pm.sets(parameter_node,nodesOnly=True,q=True)
        pm.select(node_list)

    def del_PB_hit(self):
        item_list=self.objSets_listWidget.selectedItems()
        for i in item_list:
            pm.delete(i.node)
        self.getObjSets()
        print

    def checkAttrUi(self,item):
        self.clearLayout(self.attr_scrollAreaWidgetContents.layout())
        node=item.node
        if len(self.objSets_listWidget.selectedItems())==1:
            if node.type()=='RedshiftMeshParameters':
                self.attr_label.setText("Redshift Mesh Parameters Attribute")
                attri_ui=redShiftTools_objSet_mesh_ui(node)
                self.attr_scrollAreaWidgetContents.layout().addWidget(attri_ui)

            elif node.type()=='RedshiftMatteParameters':
                self.attr_label.setText("Redshift Matte Parameters Attribute")
                attri_ui=redShiftTools_objSet_matte_ui(node)
                self.attr_scrollAreaWidgetContents.layout().addWidget(attri_ui)

            elif node.type()=='RedshiftObjectId':
                self.attr_label.setText("Redshift ObjectId Attribute")
                attri_ui=redShiftTools_objSet_objectId_ui(node)
                self.attr_scrollAreaWidgetContents.layout().addWidget(attri_ui)

            elif node.type()=='RedshiftVisibility':
                self.attr_label.setText("Redshift Visibility Attribute")
                attri_ui=redShiftTools_objSet_visbility_ui(node)
                self.attr_scrollAreaWidgetContents.layout().addWidget(attri_ui)

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())

#---------------------------------------------------------------------------------------------------#
class obj_properties_listItem(QtWidgets.QListWidgetItem):
    def __init__(self,node):
        super(obj_properties_listItem, self).__init__()
        self.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.setText(node.name())
        self.setSizeHint(QtCore.QSize(20,20))
        self.node=node

#---------------------------------------------------------------------------------------------------#
class redShiftTools_objSet_mesh_ui(QtWidgets.QWidget,redShiftTools_objSet_mesh_ui.Ui_main_widget):
    def __init__(self,node, parent=None):
        super(redShiftTools_objSet_mesh_ui, self).__init__(parent)
        self.setupUi(self)
        self.node=node
        self.onlyFloat32 = QtGui.QDoubleValidator(0.0,32.0,2)
        self.onlyFloat1000 = QtGui.QDoubleValidator(0.0,1000,2)
        self.onlyInt = QtGui.QIntValidator(0,16)
        self.miniEdge_LE.setValidator(self.onlyFloat32)
        self.maxSd_LE.setValidator(self.onlyInt)
        self.factor_LE.setValidator(self.onlyFloat32)
        self.max_dm_LE.setValidator(self.onlyFloat32)
        self.dm_scale_LE.setValidator(self.onlyFloat32)
        self.setAttr()
        self.connectInterface()

    def connectInterface(self):
        self.tessellation_enable_CB_hit()
        self.dm_enable_CB_hit()
        self.tessellation_enable_CB.stateChanged.connect(self.tessellation_enable_CB_hit)
        self.dm_enable_CB.stateChanged.connect(self.dm_enable_CB_hit)

    def setAttr(self):
        self.attr_dict={
            self.tessellation_enable_CB:self.node.enableSubdivision,
            self.screeSpaceAdaptiveCB:self.node.screenSpaceAdaptive,
            self.smoothSd_CB:self.node.doSmoothSubdivision,
            self.dm_enable_CB:self.node.enableDisplacement,
            self.enable_auto_bump_mapping_CB:self.node.autoBumpMap,
            self.miniEdgeLength_label:self.node.minTessellationLength,
            self.maxSd_label:self.node.maxTessellationSubdivs,
            self.outOfFrustumTessFactor_label:self.node.outOfFrustumTessellationFactor,
            self.maximum_dm_label:self.node.maxDisplacement,
            self.dm_scale_label:self.node.displacementScale,
            self.sdRule_label:self.node.subdivisionRule
            }
        self.enableSubdivision_class=setCheckBox(self, self.node.enableSubdivision, self.tessellation_enable_CB)
        self.screenSpaceAdaptive_class=setCheckBox(self, self.node.screenSpaceAdaptive, self.screeSpaceAdaptiveCB)
        self.doSmoothSubdivision_class=setCheckBox(self, self.node.doSmoothSubdivision, self.smoothSd_CB)
        self.enableDisplacement_class=setCheckBox(self, self.node.enableDisplacement, self.dm_enable_CB)
        self.autoBumpMap_class=setCheckBox(self, self.node.autoBumpMap, self.enable_auto_bump_mapping_CB)
        self.minTessellationLength_class=setLineEditAndSlider(self,self.node.minTessellationLength, "float", 0, 32, self.miniEdge_LE, self.miniEdge_slider,self.miniEdgeLength_label)
        self.maxTessellationSubdivs_class=setLineEditAndSlider(self,self.node.maxTessellationSubdivs, "int", 0, 16, self.maxSd_LE, self.maxSd_slider,self.maxSd_label)
        self.outOfFrustumTessellationFactor_class=setLineEditAndSlider(self,self.node.outOfFrustumTessellationFactor, "float", 0, 32, self.factor_LE, self.factor_slider,self.outOfFrustumTessFactor_label)
        self.maxDisplacement_class=setLineEditAndSlider(self,self.node.maxDisplacement, "float", 0, 1000, self.max_dm_LE, self.max_dm_slider,self.maximum_dm_label)
        self.displacementScale_class=setLineEditAndSlider(self,self.node.displacementScale, "float", 0, 1000, self.dm_scale_LE, self.dm_scale_slider,self.dm_scale_label)
        self.subdivisionRule_class=setComboBox(self, self.node.subdivisionRule, self.sdRule_comboBox,self.sdRule_label)

    def tessellation_enable_CB_hit(self):
        CB_list=[
            self.sdRule_comboBox,
            self.screeSpaceAdaptiveCB,
            self.smoothSd_CB,
            self.miniEdge_LE,
            self.miniEdge_slider,
            self.maxSd_LE,
            self.maxSd_slider,
            self.factor_LE,
            self.factor_slider
            ]
        if self.tessellation_enable_CB.checkState():
            for i in CB_list:
                i.setEnabled(True)        
        else:
            for i in CB_list:
                i.setEnabled(False)

    def dm_enable_CB_hit(self):
        CB_list=[
            self.max_dm_LE,
            self.max_dm_slider,
            self.dm_scale_LE,
            self.dm_scale_slider,
            self.enable_auto_bump_mapping_CB
            ]
        if self.dm_enable_CB.checkState():
            for i in CB_list:
                i.setEnabled(True)        
        else:
            for i in CB_list:
                i.setEnabled(False)

    def mousePressEvent(self,event):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer != 'defaultRenderLayer':
            if event.button() == QtCore.Qt.RightButton:
                point=event.pos()
                item=self.childAt(point)
                if item in self.attr_dict:
                    self.mouseMenu(item,self.attr_dict[item])

    def mouseMenu(self,item,attr):
        override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
        print override_list
        self.override_attr=attr
        self.override_item=item
        if override_list != None:
            if attr in override_list:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Remove Layer Overide',self)
                action.triggered.connect(self.removeOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
            else:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Create Layer Override',self)
                action.triggered.connect(self.createOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
        else:
            popMenu = QtWidgets.QMenu()
            action = QtWidgets.QAction('Create Layer Override',self)
            action.triggered.connect(self.createOverride)
            popMenu.addAction(action)
            popMenu.exec_(QtGui.QCursor.pos())

    def createOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr)
        self.override_item.setStyleSheet("color: rgb(255, 127, 0);")

    def removeOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr,remove=True)
        self.override_item.setStyleSheet("color:"";")

#---------------------------------------------------------------------------------------------------#
class redShiftTools_objSet_matte_ui(QtWidgets.QWidget,redShiftTools_objSet_matte_ui.Ui_main_widget):
    def __init__(self,node, parent=None):
        super(redShiftTools_objSet_matte_ui, self).__init__(parent)
        self.setupUi(self)
        self.node=node
        self.onlyFloat32 = QtGui.QDoubleValidator(0.0,32.0,2)
        self.onlyFloat1 = QtGui.QDoubleValidator(0.0,1,2)
        self.onlyInt = QtGui.QIntValidator(0,16)
        self.matteAlpha_LE.setValidator(self.onlyFloat32)
        self.matteReflectionScale_LE.setValidator(self.onlyInt)
        self.matteRefractionScale_LE.setValidator(self.onlyFloat32)
        self.matteDiffuseScale_LE.setValidator(self.onlyFloat32)
        self.shadowTransparency_LE.setValidator(self.onlyFloat32)
        self.connectInterface()
        self.setAttr()

    def setAttr(self):
        self.attr_dict={
            self.matteEnable_CB:self.node.matteEnable,
            self.matteShowBackground_CB:self.node.matteShowBackground,
            self.matteApplyToSecondaryRays_CB:self.node.matteApplyToSecondaryRays,
            self.matteAffectedByMatteLights_CB:self.node.matteAffectedByMatteLights,
            self.matteNoSelfShadow_CB:self.node.noSelfShadow,
            self.shadowEnable_CB:self.node.matteShadowEnable,
            self.shadowAffectAlpha_CB:self.node.matteShadowAffectsAlpha,
            self.matteAlpha_label:self.node.matteAlpha,
            self.matteReflection_label:self.node.matteReflectionScale,
            self.matteRefractionScale_label:self.node.matteRefractionScale,
            self.matteRefractionScale_label:self.node.matteRefractionScale,
            self.matteDiffuseScale_label:self.node.matteDiffuseScale,
            self.shadowColor_label:self.node.matteShadowColor,
            self.shadowTransparency_label:self.node.matteShadowTransparency
            }
        self.matteEnable_CB_hit()
        self.shadowEnable_CB_hit()
        self.matteEnable_class=setCheckBox(self, self.node.matteEnable, self.matteEnable_CB)
        self.matteShowBackground_class=setCheckBox(self, self.node.matteShowBackground, self.matteShowBackground_CB)
        self.matteApplyToSecondaryRays_class=setCheckBox(self, self.node.matteApplyToSecondaryRays, self.matteApplyToSecondaryRays_CB)
        self.matteAffectedByMatteLights_class=setCheckBox(self, self.node.matteAffectedByMatteLights, self.matteAffectedByMatteLights_CB)
        self.noSelfShadow_class=setCheckBox(self, self.node.noSelfShadow, self.matteNoSelfShadow_CB)
        self.matteAlpha_class=setLineEditAndSliderB(self,self.node.matteAlpha, "float", 0.0, 1.0, self.matteAlpha_LE, self.matteAlpha_slider,self.matteAlpha_label)
        self.matteReflectionScale_class=setLineEditAndSliderB(self,self.node.matteReflectionScale, "float", 0.0, 1.0, self.matteReflectionScale_LE, self.matteReflectionScale_slider,self.matteReflection_label)
        self.matteRefractionScale_class=setLineEditAndSliderB(self,self.node.matteRefractionScale, "float", 0.0, 1.0, self.matteRefractionScale_LE, self.matteRefractionScale_slider,self.matteRefractionScale_label)
        self.matteDiffuseScale_class=setLineEditAndSliderB(self,self.node.matteDiffuseScale, "float", 0.0, 1.0, self.matteDiffuseScale_LE, self.matteDiffuseScale_slider,self.matteDiffuseScale_label)
        self.matteShadowEnable_class=setCheckBox(self, self.node.matteShadowEnable, self.shadowEnable_CB)
        self.matteShadowAffectsAlpha_class=setCheckBox(self, self.node.matteShadowAffectsAlpha, self.shadowAffectAlpha_CB)
        self.matteShadowColor_class=setColorEdit(self,self.node.matteShadowColor,0.0,1.0,self.shadowColorSet_PB, self.shadowColor_slider,self.shadowColor_label)
        self.matteShadowTransparency_class=setLineEditAndSliderB(self,self.node.matteShadowTransparency, "float", 0.0, 1.0, self.shadowTransparency_LE, self.shadowTransparency_slider,self.shadowTransparency_label)

    def connectInterface(self):
        self.matteEnable_CB.stateChanged.connect(self.matteEnable_CB_hit)
        self.shadowEnable_CB.stateChanged.connect(self.shadowEnable_CB_hit)

    def mousePressEvent(self,event):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer != 'defaultRenderLayer':
            if event.button() == QtCore.Qt.RightButton:
                point=event.pos()
                item=self.childAt(point)
                if item in self.attr_dict:
                    self.mouseMenu(item,self.attr_dict[item])

    def mouseMenu(self,item,attr):
        override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
        print override_list
        self.override_attr=attr
        self.override_item=item
        if override_list != None:
            if attr in override_list:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Remove Layer Overide',self)
                action.triggered.connect(self.removeOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
            else:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Create Layer Override',self)
                action.triggered.connect(self.createOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
        else:
            popMenu = QtWidgets.QMenu()
            action = QtWidgets.QAction('Create Layer Override',self)
            action.triggered.connect(self.createOverride)
            popMenu.addAction(action)
            popMenu.exec_(QtGui.QCursor.pos())

    def createOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr)
        self.override_item.setStyleSheet("color: rgb(255, 127, 0);")

    def removeOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr,remove=True)
        self.override_item.setStyleSheet("color:"";")

    def matteEnable_CB_hit(self):
        CB_list=[
            self.matteShowBackground_CB,
            self.matteApplyToSecondaryRays_CB,
            self.matteAffectedByMatteLights_CB,
            self.matteNoSelfShadow_CB,
            self.matteAlpha_LE,
            self.matteReflectionScale_LE,
            self.matteRefractionScale_LE,
            self.matteDiffuseScale_LE,
            self.matteAlpha_slider,
            self.matteReflectionScale_slider,
            self.matteReflectionScale_slider,
            self.matteRefractionScale_slider,
            self.matteDiffuseScale_slider
            ]
        if self.matteEnable_CB.checkState():
            for i in CB_list:
                i.setEnabled(True)        
        else:
            for i in CB_list:
                i.setEnabled(False)

    def shadowEnable_CB_hit(self):
        CB_list=[
            self.shadowAffectAlpha_CB,
            self.shadowColorSet_PB,
            self.shadowColor_slider,
            self.shadowTransparency_LE,
            self.shadowTransparency_slider,
            ]
        if self.matteEnable_CB.checkState():
            for i in CB_list:
                i.setEnabled(True)        
        else:
            for i in CB_list:
                i.setEnabled(False)

#---------------------------------------------------------------------------------------------------#
class redShiftTools_objSet_objectId_ui(QtWidgets.QWidget,redShiftTools_objSet_objectId_ui.Ui_main_widget):
    def __init__(self,node, parent=None):
        super(redShiftTools_objSet_objectId_ui, self).__init__(parent)
        self.setupUi(self)
        self.node=node
        self.onlyFloat32 = QtGui.QDoubleValidator(0.0,32.0,2)
        self.onlyFloat1 = QtGui.QDoubleValidator(0.0,1.0,2)
        self.onlyInt = QtGui.QIntValidator(0,100)
        self.objectId_LE.setValidator(self.onlyInt)
        self.connectInterface()
        self.setAttr()

    def setAttr(self):
        self.attr_dict={
            self.objectId_enable_CB:self.node.enable,
            self.objectId_label:self.node.objectId
            }
        self.enable_class=setCheckBox(self, self.node.enable, self.objectId_enable_CB)
        self.objectId_class=setLineEditAndSlider(self,self.node.objectId, "int", 0, 100, self.objectId_LE, self.objectId_slider,self.objectId_label)

    def connectInterface(self):
        self.objectId_enable_CB.clicked.connect(self.objectId_enable_CB_hit)

    def objectId_enable_CB_hit(self):
        if self.objectId_enable_CB.checkState():
            self.objectId_LE.setEnabled(True)
            self.objectId_slider.setEnabled(True)
        else:
            self.objectId_LE.setEnabled(False)
            self.objectId_slider.setEnabled(False)

    def mousePressEvent(self,event):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer != 'defaultRenderLayer':
            if event.button() == QtCore.Qt.RightButton:
                point=event.pos()
                item=self.childAt(point)
                if item in self.attr_dict:
                    self.mouseMenu(item,self.attr_dict[item])

    def mouseMenu(self,item,attr):
        override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
        print override_list
        self.override_attr=attr
        self.override_item=item
        if override_list != None:
            if attr in override_list:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Remove Layer Overide',self)
                action.triggered.connect(self.removeOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
            else:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Create Layer Override',self)
                action.triggered.connect(self.createOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
        else:
            popMenu = QtWidgets.QMenu()
            action = QtWidgets.QAction('Create Layer Override',self)
            action.triggered.connect(self.createOverride)
            popMenu.addAction(action)
            popMenu.exec_(QtGui.QCursor.pos())

    def createOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr)
        self.override_item.setStyleSheet("color: rgb(255, 127, 0);")

    def removeOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr,remove=True)
        self.override_item.setStyleSheet("color:"";")

#---------------------------------------------------------------------------------------------------#
class redShiftTools_objSet_visbility_ui(QtWidgets.QWidget,redShiftTools_objSet_visbility_ui.Ui_main_widget):
    def __init__(self,node, parent=None):
        super(redShiftTools_objSet_visbility_ui, self).__init__(parent)
        self.setupUi(self)
        self.node=node
        self.onlyFloat32 = QtGui.QDoubleValidator(0.0,32.0,2)
        self.onlyFloat1 = QtGui.QDoubleValidator(0.0,1.0,2)
        self.onlyInt = QtGui.QIntValidator(0,100)
        self.CB_list=[
            self.primaryRayVis_CB,
            self.seconderayRayVis_CB,
            self.castShadow_CB,
            self.receivesShadow_CB,
            self.selfShadow_CB,
            self.castAo_CB,
            self.visInRefl_CB,
            self.visInRefr_CB,
            self.castsRefl_CB,
            self.castsRefr_CB,
            self.visToNonPhotonGi_CB,
            self.visToGiPhotons_CB,
            self.visCausticPhotons_CB,
            self.receivesGi_CB,
            self.forceBruteForceGi_CB,
            self.castsGiPhotons_CB,
            self.castsCausticPhotons_CB,
            self.receivesGiPhotons_CB,
            self.receivesCausticPhotons_CB
            ]
        self.attr_list=[
            self.node.primaryRayVisible,
            self.node.secondaryRayVisible,
            self.node.shadowCaster,
            self.node.shadowReceiver,
            self.node.selfShadows,
            self.node.aoCaster,
            self.node.reflectionVisible,
            self.node.refractionVisible,
            self.node.reflectionCaster,
            self.node.refractionCaster,
            self.node.fgVisible,
            self.node.giVisible,
            self.node.causticVisible,
            self.node.fgCaster,
            self.node.forceBruteForceGI,
            self.node.giCaster,
            self.node.causticCaster,
            self.node.giReceiver,
            self.node.causticReceiver
            ]
        self.connectInterface()
        self.setAttr()

    def setAttr(self):
        self.attr_dict={
            self.globalEnable_CB:self.node.enable,
            self.CB_list[0]:self.attr_list[0],
            self.CB_list[1]:self.attr_list[1],
            self.CB_list[2]:self.attr_list[2],
            self.CB_list[3]:self.attr_list[3],
            self.CB_list[4]:self.attr_list[4],
            self.CB_list[5]:self.attr_list[5],
            self.CB_list[6]:self.attr_list[6],
            self.CB_list[7]:self.attr_list[7],
            self.CB_list[8]:self.attr_list[8],
            self.CB_list[9]:self.attr_list[9],
            self.CB_list[10]:self.attr_list[10],
            self.CB_list[11]:self.attr_list[11],
            self.CB_list[12]:self.attr_list[12],
            self.CB_list[13]:self.attr_list[13],
            self.CB_list[14]:self.attr_list[14],
            self.CB_list[15]:self.attr_list[15],
            self.CB_list[16]:self.attr_list[16],
            self.CB_list[17]:self.attr_list[17],
            self.CB_list[18]:self.attr_list[18]
            }
        self.seconderayRayVis_CB_hit()
        self.enable_class=setCheckBox(self, self.node.enable, self.globalEnable_CB)
        self.primaryRayVisible_class=setCheckBox(self, self.attr_list[0], self.CB_list[0])
        self.secondaryRayVisible_class=setCheckBox(self, self.attr_list[1], self.CB_list[1])
        self.shadowCaster_class=setCheckBox(self, self.attr_list[2], self.CB_list[2])
        self.shadowReceiver_class=setCheckBox(self, self.attr_list[3], self.CB_list[3])
        self.selfShadows_class=setCheckBox(self, self.attr_list[4], self.CB_list[4])
        self.aoCaster_class=setCheckBox(self, self.attr_list[5], self.CB_list[5])
        self.reflectionVisible_class=setCheckBox(self, self.attr_list[6], self.CB_list[6])
        self.refractionVisible_class=setCheckBox(self, self.attr_list[7], self.CB_list[7])
        self.reflectionCaster_class=setCheckBox(self, self.attr_list[8], self.CB_list[8])
        self.refractionCaster_class=setCheckBox(self, self.attr_list[9], self.CB_list[9])
        self.fgVisible_class=setCheckBox(self, self.attr_list[10], self.CB_list[10])
        self.giVisible_class=setCheckBox(self, self.attr_list[11], self.CB_list[11])
        self.causticVisible_class=setCheckBox(self, self.attr_list[12], self.CB_list[12])
        self.fgCaster_class=setCheckBox(self, self.attr_list[13], self.CB_list[13])
        self.forceBruteForceGI_class=setCheckBox(self, self.attr_list[14], self.CB_list[14])
        self.giCaster_class=setCheckBox(self, self.attr_list[15], self.CB_list[15])
        self.causticCaster_class=setCheckBox(self, self.attr_list[16], self.CB_list[16])
        self.giReceiver_class=setCheckBox(self, self.attr_list[17], self.CB_list[17])
        self.causticReceiver_class=setCheckBox(self, self.attr_list[18], self.CB_list[18])


    def connectInterface(self):
        self.seconderayRayVis_CB.stateChanged.connect(self.seconderayRayVis_CB_hit)

    def seconderayRayVis_CB_hit(self):
        CB_list=[
            self.visInRefl_CB,
            self.visInRefr_CB,
            self.castsRefl_CB,
            self.castsRefr_CB,
            self.visToNonPhotonGi_CB,
            self.receivesGi_CB,
            self.forceBruteForceGi_CB,
            self.receivesGiPhotons_CB,
            self.receivesCausticPhotons_CB
            ]
        if self.seconderayRayVis_CB.checkState():
            for i in CB_list:
                i.setEnabled(True)

        else:
            for i in CB_list:
                i.setEnabled(False)


    def mousePressEvent(self,event):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer != 'defaultRenderLayer':
            if event.button() == QtCore.Qt.RightButton:
                point=event.pos()
                item=self.childAt(point)
                if item in self.attr_dict:
                    self.mouseMenu(item,self.attr_dict[item])

    def mouseMenu(self,item,attr):
        override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
        print override_list
        self.override_attr=attr
        self.override_item=item
        if override_list != None:
            if attr in override_list:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Remove Layer Overide',self)
                action.triggered.connect(self.removeOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
            else:
                popMenu = QtWidgets.QMenu()
                action = QtWidgets.QAction('Create Layer Override',self)
                action.triggered.connect(self.createOverride)
                popMenu.addAction(action)
                popMenu.exec_(QtGui.QCursor.pos())
        else:
            popMenu = QtWidgets.QMenu()
            action = QtWidgets.QAction('Create Layer Override',self)
            action.triggered.connect(self.createOverride)
            popMenu.addAction(action)
            popMenu.exec_(QtGui.QCursor.pos())
        
    def createOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr)
        self.override_item.setStyleSheet("color: rgb(255, 127, 0);")
        print self.override_attr

    def removeOverride(self):
        pm.editRenderLayerAdjustment(self.override_attr,remove=True)
        self.override_item.setStyleSheet("color:"";")
        print self.override_attr    

#---------------------------------------------------------------------------------------------------#
class setLineEditAndSlider(object):
    """docstring for ClassName"""
    def __init__(self,parent,attr,valueType,min,max,lineEdit,slider,label):
        super(setLineEditAndSlider, self).__init__()
        self.parent =parent
        self.attr = attr
        self.label=label
        self.valueType=valueType
        self.min=min
        self.max=max
        self.lineEdit=lineEdit
        self.slider=slider
        self.setSliderValue()

    def setSliderValue(self):
        if self.valueType=='float':
            onlyFloat = QtGui.QDoubleValidator(self.min,self.max,2)
            self.lineEdit.setValidator(onlyFloat)
            value=round(self.attr.get(), 2)
            self.slider.setSingleStep(0.1)
        elif self.valueType=='int':
            onlyInt = QtGui.QIntValidator(self.min,self.max)
            self.lineEdit.setValidator(onlyInt)
            value=self.attr.get()
        self.lineEdit.setText(str(value))
        self.slider.setValue(value)
        self.lineEdit.textChanged.connect(self.connectLineEditToSlider)
        self.slider.valueChanged.connect(self.connectSliderToLineEdit)
        self.checkOverride()

    def connectLineEditToSlider(self,value):
        #value=self.lineEdit.text()
        if self.valueType=="float":
            value=round(float(value), 2)
        elif self.valueType=="int":
            value=int(value)
        self.attr.set(value)
        self.slider.setValue(value)

    def connectSliderToLineEdit(self,value):
        #value=self.lineEdit.value()
        if self.valueType=="float":
            value=round(float(value), 2)
        elif self.valueType=="int":
            value=int(value)
        self.attr.set(value)
        self.lineEdit.setText(str(value))

    def checkOverride(self):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer!='defaultRenderLayer':
            override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
            if override_list != None:
                if self.attr  in override_list:
                    self.label.setStyleSheet("color: rgb(255, 127, 0);")

#---------------------------------------------------------------------------------------------------#
class setLineEditAndSliderB(object):
    """docstring for ClassName"""
    def __init__(self,parent,attr,valueType,textMin,textMax,lineEdit,slider,label):
        super(setLineEditAndSliderB, self).__init__()
        self.parent =parent
        self.attr = attr
        self.label=label
        self.valueType=valueType
        self.textMin=textMin
        self.textMax=textMax
        self.textGrp=textMax-textMin
        self.lineEdit=lineEdit
        self.slider=slider
        self.sliderMin=0.0
        self.sliderMax=100.0
        self.sliderGap=self.sliderMax-self.sliderMin
        self.slider.setRange(self.sliderMin,self.sliderMax)
        self.setSliderValue()

    def setSliderValue(self):
        if self.valueType=='float':
            onlyFloat = QtGui.QDoubleValidator(self.textMin,self.textMax,2)
            self.lineEdit.setValidator(onlyFloat)
            value=round(self.attr.get(), 2)
        elif self.valueType=='int':
            onlyInt = QtGui.QIntValidator(self.textMin,self.textMax)
            self.lineEdit.setValidator(onlyInt)
            value=self.attr.get()
        self.lineEdit.setText(str(value))
        num=int((value-self.textMin)/self.textGrp*self.sliderGap+self.sliderMin)
        self.slider.setValue(num)
        self.lineEdit.textChanged.connect(self.connectLineEditToSlider)
        self.slider.valueChanged.connect(self.connectSliderToLineEdit)
        self.checkOverride()

    def connectLineEditToSlider(self,value):
        #value=self.lineEdit.text()
        if self.valueType=="float":
            value=round(float(value), 2)
        elif self.valueType=="int":
            value=int(value)
        self.attr.set(value)
        num=int((value-self.textMin)/self.textGrp*self.sliderGap+self.sliderMin)
        self.slider.setValue(num)

    def connectSliderToLineEdit(self,value):
        num=float(value-self.sliderMin)/self.sliderGap*self.textGrp+self.textMin
        if self.valueType=="float":
            num=round(float(num), 2)
        elif self.valueType=="int":
            num=int(num)
        self.attr.set(num)
        self.lineEdit.setText(str(num))

    def checkOverride(self):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer!='defaultRenderLayer':
            override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
            if override_list != None:
                if self.attr  in override_list:
                    self.label.setStyleSheet("color: rgb(255, 127, 0);")

#---------------------------------------------------------------------------------------------------#
class setCheckBox(object):
    """docstring for ClassName"""
    def __init__(self,parent,attr,checkBox):
        super(setCheckBox, self).__init__()
        self.parent =parent
        self.attr = attr
        self.checkBox=checkBox
        self.setValue()

    def setValue(self):
        value=self.attr.get()
        self.checkBox.setChecked(value)
        self.checkBox.stateChanged.connect(self.checkBox_hit)
        self.checkOverride()

    def checkBox_hit(self,stage):
        if self.checkBox.checkState():
            self.attr.set(True)
        else:
            self.attr.set(False)

    def checkOverride(self):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer!='defaultRenderLayer':
            override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
            if override_list != None:
                if self.attr  in override_list:
                    self.checkBox.setStyleSheet("color: rgb(255, 127, 0);")

#---------------------------------------------------------------------------------------------------#
class setComboBox(object):
    """docstring for ClassName"""
    def __init__(self,parent,attr,comboBox,label):
        super(setComboBox, self).__init__()
        self.parent =parent
        self.attr = attr
        self.comboBox=comboBox
        self.label=label
        self.setValue()

    def setValue(self):
        value=self.attr.get()
        self.checkOverride()
        self.comboBox.setCurrentIndex(value)
        self.comboBox.currentIndexChanged.connect(self.comboBox_hit)

    def comboBox_hit(self,index):
        self.attr.set(index)

    def checkOverride(self):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer!='defaultRenderLayer':
            override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
            if override_list != None:
                if self.attr  in override_list:
                    self.label.setStyleSheet("color: rgb(255, 127, 0);")

#---------------------------------------------------------------------------------------------------#
class setColorEdit(object):
    """docstring for ClassName"""
    def __init__(self,parent,attr,textMin,textMax,pushButton,slider,label):
        super(setColorEdit, self).__init__()
        self.parent =parent
        self.attr = attr
        self.pushButton=pushButton
        self.slider=slider
        self.label=label
        self.textMin=textMin
        self.textMax=textMax
        self.textGrp=textMax-textMin
        self.sliderMin=0.0
        self.sliderMax=100.0
        self.sliderGap=self.sliderMax-self.sliderMin
        self.setColorValue()

    def setColorValue(self):
        self.setSliderValue()
        self.setPushButtonColor()
        self.pushButton.clicked.connect(self.pushButton_hit)
        self.slider.valueChanged.connect(self.slider_hit)
        self.checkOverride()

    def pushButton_hit(self):
        original_color=self.attr.get()
        cmds.colorEditor(rgbValue=[original_color[0],original_color[1],original_color[2]])
        if cmds.colorEditor(query=True, result=True):
            values = cmds.colorEditor(query=True, rgb=True)
            self.attr.set(values)
            self.setSliderValue()
            self.setPushButtonColor()

    def slider_hit(self,value):
        num=float(value-self.sliderMin)/self.sliderGap*self.textGrp+self.textMin
        oldColor=self.attr.get()
        hsv=colorsys.rgb_to_hsv(oldColor[0],oldColor[1],oldColor[2])
        rgb=colorsys.hsv_to_rgb(hsv[0],hsv[1],num)
        self.attr.set(rgb)
        self.setPushButtonColor()

    def setSliderValue(self):
        values=self.attr.get()
        hsv=colorsys.rgb_to_hsv(values[0],values[1],values[2])
        num=int((hsv[2]-self.textMin)/self.textGrp*self.sliderGap+self.sliderMin)
        self.slider.setValue(num)

    def setPushButtonColor(self):
        values=self.attr.get()
        sRGB=[srgbtransform.linear_to_srgb_8bit(values[0]),srgbtransform.linear_to_srgb_8bit(values[1]),srgbtransform.linear_to_srgb_8bit(values[2])]
        self.pushButton.setStyleSheet("\
            QPushButton {\
                border-style: none;\
                color: rgb(%s,%s,%s);\
                background-color: rgb(%s,%s,%s);\
            }\
            "%(sRGB[0],sRGB[1],sRGB[2],sRGB[0],sRGB[1],sRGB[2])
            )

    def checkOverride(self):
        self.layer=pm.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if self.layer!='defaultRenderLayer':
            override_list=cmds.editRenderLayerAdjustment( self.layer,layer=True,q=True)
            if override_list != None:
                if self.attr  in override_list:
                    self.label.setStyleSheet("color: rgb(255, 127, 0);")


def create():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def main():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def create():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def redShiftToolsMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()
