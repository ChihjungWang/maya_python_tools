# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtUiTools,QtWidgets
import maya.cmds as cmds
import pymel.core as pm
import os
import sys
import threading
import signal
import time
import multiprocessing
import datetime
import getpass
import csv
prman_path=os.getenv('RMANTREE')
ice_path=prman_path+"lib\python2.7\Lib\site-packages\ice"
sys.path.append(ice_path)
import ice

maya_version=cmds.about(version=True)
username=getpass.getuser()
ui_path='C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")
import prmanDenoiseToolsCMD_ui;reload(prmanDenoiseToolsCMD_ui)
import prmanDenoiseToolsMergeEXR_ui;reload(prmanDenoiseToolsMergeEXR_ui)


dialog=None
class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('renderman denoise tools'+' v0.5'+u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800,600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0,0,0,0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        self.denoiseCMD_wid=denoiseCMD_ui()
        self.mergeEXR_wid=mergeEXR_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.denoiseCMD_wid, "denoiseCMD")
        main_tab_Widget.addTab(self.mergeEXR_wid, "mergeEXR")
        self.layout().addWidget(main_tab_Widget)
        self.python_temp='C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv=self.python_temp+'/prmanDenoiseTools.csv'
        denoiseCMD_save_UI_list=[self.denoiseCMD_wid.varianceFile_LE,self.denoiseCMD_wid.aovLightGrpName_LE,self.denoiseCMD_wid.outDir_LE,self.denoiseCMD_wid.frameRangeStart_LE,self.denoiseCMD_wid.frameRangeEnd_LE]
        mergeEXR_save_UI_list=[self.mergeEXR_wid.filterExr_LE,self.mergeEXR_wid.baseName_LE,self.mergeEXR_wid.aovLightGrpName_LE,self.mergeEXR_wid.outDir_LE,self.mergeEXR_wid.frameRangeStart_LE,self.mergeEXR_wid.frameRangeEnd_LE]
        self.save_UI_list=denoiseCMD_save_UI_list+mergeEXR_save_UI_list
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

class denoiseCMD_ui(QtWidgets.QWidget,prmanDenoiseToolsCMD_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(denoiseCMD_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        #self.variance_pathExt='E:/exercise/nuke_pro/sourceimages/beauty_RL/AA_variance.0001.exr'
        #self.AOV_lightGrp_name='key'
        #self.varianceFile_LE.setText(self.variance_pathExt)
        #self.aovLightGrpName_LE.setText(self.AOV_lightGrp_name)
        username=getpass.getuser()
        self.python_temp='C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv=self.python_temp+'/denoiseCMD.csv'
        self.frameRangeStart_LE.setText("%04d" % 1)
        self.frameRangeEnd_LE.setText("%04d" % 1)
        self.layer_LE.setText("diffuse,specular,directDiffuse,indirectDiffuse,directSpecular,indirectSpecular,subsurface,transmissive")
        self.newName_LE.setText('filtered')
        self.motionVector_LE.setText('variance')
        self.rman_folder=os.getenv('RMANTREE')
        self.output_dir_CB.setCheckState(QtCore.Qt.CheckState(2))
        self.newName_LE.setEnabled(False)
        self.layer_LE.setEnabled(False)
        self.motionVector_LE.setEnabled(False)
        self.nOfThreads_SB.setEnabled(False)
        cpu_cores=multiprocessing.cpu_count()
        self.nOfThreads_SB.setRange(1,cpu_cores)
        self.nOfThreads_SB.setValue(cpu_cores)

    def connectInterface(self):
        self.varianceFileOpen_PB.clicked.connect(self.varianceOpenFile)
        self.varianceFileBro_PB.clicked.connect(self.variancePathBro)
        self.checkChannel_PB.clicked.connect(self.showChannels)
        self.rebuildBat_PB.clicked.connect(self.rebuildBat)
        self.exportBat_PB.clicked.connect(self.exportBat)
        self.varianceFile_LE.textChanged.connect(self.setVariancePath)
        self.outDirBro_PB.clicked.connect(self.outputExrBro)
        self.outDirOpen_PB.clicked.connect(self.outputExrOpen)
        self.nOfThreads_CB.stateChanged.connect(self.nOfThreadsCB_hit)
        self.newName_CB.stateChanged.connect(self.newName_CB_hit)
        self.output_dir_CB.stateChanged.connect(self.outputDirCB_hit)
        self.layer_CB.stateChanged.connect(self.layerCB_hit)
        self.motionVector_CB.stateChanged.connect(self.motionVectorCB_hit)
        self.configFile_CB.stateChanged.connect(self.configFileCB_hit)
        self.outputBasename_CB.stateChanged.connect(self.outputBasename_CB_hit)
        self.json_window_PB.clicked.connect(self.json_window_PB_hit)

    def setVariancePath(self):
        pathExt=self.varianceFile_LE.text()
        pathExt=pathExt.replace('\\','/')
        if os.path.isfile(pathExt):
            self.variance_pathExt=pathExt
            self.variance_path=os.path.split(pathExt)[0]
            self.variance_name=os.path.split(pathExt)[1]
            name=os.path.splitext(self.variance_name)[0]
            name=os.path.splitext(name)[0]
            self.img_base_name=name.replace('_variance','')
            if self.aovLightGrpName_LE.text()!="":
                self.imageName_label.setText(self.img_base_name+"_channel_"+self.aovLightGrpName_LE.text()+"_")

    def variancePathBro(self):
        pathExt= QtWidgets.QFileDialog.getOpenFileName(filter='*.exr')[0]
        pathExt=pathExt.replace('\\','/')
        if pathExt !="":
            self.varianceFile_LE.setText(pathExt)
            self.setVariancePath()

    def varianceOpenFile(self):
        variance_file=self.varianceFile_LE.text()
        variance_path=os.path.split(variance_file)[0]
        os.startfile(variance_path)

    def outputExrBro(self):
        output_dir= QtWidgets.QFileDialog.getExistingDirectory()
        output_dir=output_dir.replace('\\','/')
        if output_dir !="":
            self.outDir_LE.setText(output_dir)

    def outputExrOpen(self):
        output_dir=self.outDir_LE.text()
        output_dir=output_dir.replace('/','\\')
        os.startfile(output_dir)

    def json_window_PB_hit(self):
        self.jsonWindow = jsonWindow(self)
        self.jsonWindow.show()

    def newName_CB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.newName_LE.setEnabled(True)
            self.outputBasename_CB.setChecked(False)
        else:
            self.newName_LE.setEnabled(False)

    def outputBasename_CB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.newName_CB.setChecked(False)

    def outputDirCB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.outDir_LE.setEnabled(True)
        else:
            self.outDir_LE.setEnabled(False)

    def layerCB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.layer_LE.setEnabled(True)
        else:
            self.layer_LE.setEnabled(False)

    def motionVectorCB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.motionVector_LE.setEnabled(True)
            self.crossFrame_CB.setChecked(True)
        else:
            self.motionVector_LE.setEnabled(False)

    def configFileCB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.json_LE.setEnabled(True)
            self.json_window_PB.setEnabled(True)
        else:
            self.json_LE.setEnabled(False)
            self.json_window_PB.setEnabled(False)

    def nOfThreadsCB_hit(self,state):
        if state==QtCore.Qt.Checked:
            self.nOfThreads_SB.setEnabled(True)
        else:
            self.nOfThreads_SB.setEnabled(False)

    def showChannels(self):
        self.setVariancePath()
        exr_list=self.exrList(self.variance_path)
        self.channel_info=self.channelInfo()
        start_frame=int(self.frameRangeStart_LE.text())
        end_frame=int(self.frameRangeEnd_LE.text())
        num_list=range(start_frame,end_frame+1)

        self.affect_channel_list=[]
        for exr in exr_list:
            for channel in self.channel_info:
                full_name=self.img_base_name+"_"+channel['type']+"_"+self.aovLightGrpName_LE.text()
                if full_name in exr:
                    channel['exist'].append(exr)

        self.cannot_find_exr=[]
        for channel in self.channel_info:
            if len(channel['exist'])>0:
                full_name=self.img_base_name+"_"+channel['type']+"_"+self.aovLightGrpName_LE.text()
                for i in num_list:
                    num="%04d" % i
                    if full_name+'.'+num+'.exr' not in channel['exist']:
                        self.cannot_find_exr.append(full_name+'.'+num+'.exr')
                        channel['exile'].append(num)
            if len(channel['exist'])>0 and len(channel['exile'])==0:
                self.affect_channel_list.append(channel['type'])

        self.affect_channel_list.sort()
        self.checkChannel_LE.setText("")
        for channel in self.affect_channel_list:
            channels=self.checkChannel_LE.text()
            channels=channels+" "+channel
            self.checkChannel_LE.setText(channels)

    def rebuildBat(self):
        self.showChannels()
        if len(self.affect_channel_list)>0:
            start_frame=int(self.frameRangeStart_LE.text())
            end_frame=int(self.frameRangeEnd_LE.text())
            num_list=range(start_frame,end_frame+1)
            variance_path=self.variance_path.replace("/","\\")
            variance_pathExt=self.variance_pathExt.replace("/","\\")
            cmd_num=""
            for num in num_list:
                num="%04d" % num
                if cmd_num=="":
                    cmd_num=num
                else:
                    cmd_num=cmd_num+','+num
            if ',' in cmd_num:
                cmd_num='{'+cmd_num+'}'
            denoiseCMD="\""+self.rman_folder+"bin\\denoise.exe"+"\""
            denoiseCMD=self.denoiseFlagCheck(denoiseCMD)
            denoiseCMD=denoiseCMD+" "+variance_path+"\\"+self.img_base_name+"_variance"+"."+cmd_num+".exr"
            for channel in self.affect_channel_list:
                denoiseCMD=denoiseCMD+" "+variance_path+"\\"+self.img_base_name+"_"+channel+"_"+self.aovLightGrpName_LE.text()+"."+cmd_num+".exr"
            self.final_denoiseCMD=denoiseCMD
            self.runCommend_textEdit.clear()
            #self.runCommend_textEdit.append('commend .bat is fine')
            self.runCommend_textEdit.append(self.final_denoiseCMD)

        else:
            self.runCommend_textEdit.clear()
            for exr in self.cannot_find_exr:
                self.runCommend_textEdit.append("cannot find ... "+exr)

    def exportBat(self):
        x = datetime.datetime.now()
        time_data ="%02d" % x.month+"%02d" % x.day+"%02d" % x.hour+"%02d" % x.minute+"%02d" % x.second
        denoise_bat=self.outDir_LE.text()+'/'+'prmanDenoise_'+time_data+'.bat'
        file = open(denoise_bat,'w')
        file.write(self.final_denoiseCMD)
        file.close()

    def denoiseFlagCheck(self,cmd):
        if self.GPU_CB.isChecked():
            cmd=cmd+' --override gpuIndex 0'
        if self.newName_CB.isChecked():
            newName=self.newName_LE.text()
            cmd=cmd+' -o '+newName
        if self.outputBasename_CB.isChecked():
            cmd=cmd+' -n'
        if self.output_dir_CB.isChecked():
            outDir=self.outDir_LE.text()
            outDir=outDir.replace("/","\\")
            cmd=cmd+" --outdir "+outDir
        if self.filterVariance_CB.isChecked():
            cmd=cmd+' --filtervariance true'
        if self.crossFrame_CB.isChecked():
            cmd=cmd+' --crossframe true'
        if self.skipFirst_CB.isChecked():
            cmd=cmd+' --skipfirst true'
        if self.skipLast_CB.isChecked():
            cmd=cmd+' --skiplast true'
        if self.filterLayersIndependently_CB.isChecked():
            cmd=cmd+' --override filterLayersIndependently true'
        if self.layer_CB.isChecked():
            layers=self.layer_LE.text()
            cmd=cmd+' --layers '+'\''+layers+'\''
        if self.motionVector_CB.isChecked():
            name=self.motionVector_LE.text()
            cmd=cmd+' -v '+name
        if self.configFile_CB.isChecked():
            text=self.json_LE.text()
            json_list=text.split(' + ')
            for json in json_list:
                cmd=cmd+' -f '+json
        if self.nOfThreads_CB.isChecked():
            num=self.nOfThreads_SB.value()
            cmd=cmd+' -t '+str(num-1)

        return cmd

    def channelInfo(self):
        channel_info=[]
        channels_list=["diffuse","specular","directDiffuse","indirectDiffuse","directSpecular","indirectSpecular","subsurface","transmissive"]
        for channel in channels_list:
            channel_dic={}
            channel_dic['type']=channel
            channel_dic['exist']=[]
            channel_dic['exile']=[]
            channel_info.append(channel_dic)
        return channel_info

    def exrList(self,path):
        file_list=os.listdir(path)
        exr_list=[]
        for i in file_list:
            if os.path.isfile(path+"/"+i):
                if os.path.splitext(i)[1]==".exr":
                    exr_list.append(i)
        exr_list.sort()
        return exr_list

    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        return False


class jsonWindow(QtWidgets.QWidget):
    def __init__(self,parentObj):
        QtWidgets.QWidget.__init__(self)
        self.parentObj=parentObj
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle('select json files')
        self.layout().setContentsMargins(2,2,2,2)
        self.layout().setSpacing(4)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        json_layout = QtWidgets.QVBoxLayout()
        json_layout.setContentsMargins(2,2,2,2)
        json_layout.setSpacing(2)
        self.layout().addLayout(json_layout)
        PB_layout = QtWidgets.QHBoxLayout()
        add_PB=QtWidgets.QPushButton('add')
        PB_layout.addWidget(add_PB)
        clear_PB=QtWidgets.QPushButton('clear')
        PB_layout.addWidget(clear_PB)
        close_PB=QtWidgets.QPushButton('close')
        PB_layout.addWidget(close_PB)

        self.layout().addLayout(PB_layout)

        clear_PB.clicked.connect(self.clear_PB_hit)
        add_PB.clicked.connect(self.add_PB_hit)
        close_PB.clicked.connect(self.close)

        self.rman_folder=os.getenv('RMANTREE')
        json_LE=self.parentObj.json_LE.text()
        json_to_list=json_LE.split(' + ')
        json_folder=self.rman_folder+'/lib/denoise'
        file_list=os.listdir(json_folder)
        json_list=[]
        for i in file_list:
            if os.path.splitext(i)[1]==".json":
                json_list.append(i)
        json_list.sort()
        self.json_info_list=[]
        for index,json in enumerate(json_list):
            json_dict={}
            json_dict['name']=json
            json_dict['CB']=QtWidgets.QCheckBox(json)
            self.json_info_list.append(json_dict)
            json_layout.addWidget(json_dict['CB'])

        json_LE=self.parentObj.json_LE.text()
        json_to_list=json_LE.split(' + ')
        for i in self.json_info_list:
            if i['name'] in json_to_list:
                i['CB'].setChecked(True)

    def add_PB_hit(self):
        self.agree_json=[]
        for i in self.json_info_list:
            if i['CB'].isChecked():
                self.agree_json.append(i['name'])
        text=""
        for i in self.agree_json:
            if text=="":
                text=text+i
            else:
                text=text+" + "+i
        self.parentObj.json_LE.setText(text)

    def clear_PB_hit(self):
        for i in self.json_info_list:
            i['CB'].setChecked(False)
        self.parentObj.json_LE.setText("")

class mergeEXR_ui(QtWidgets.QWidget,prmanDenoiseToolsMergeEXR_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(mergeEXR_ui, self).__init__(parent)
        self.setupUi(self)
        username=getpass.getuser()
        self.python_temp='C:/Users/'+username+'/Documents/maya/python_tools_temp'
        self.python_temp_csv=self.python_temp+'/mergeEXR.csv'
        self.connectInterface()

    def connectInterface(self):
        self.filterExrBro_PB.clicked.connect(self.filterExrBro)
        self.filterExrOpen_PB.clicked.connect(self.filterExrOpen)
        self.runMerge_PU.clicked.connect(self.mergerEXR_run)
        self.outDirBro_PB.clicked.connect(self.outputExrBro)
        self.outDirOpen_PB.clicked.connect(self.outputExrOpen)
        self.checkChannel_PB.clicked.connect(self.showChannels)
        self.stop_PU.clicked.connect(self.appendTextEdit)

    def setFilterInfo(self):
        file=self.filterExr_LE.text()
        file=file.replace('\\','/')
        channels_list=["diffuse","specular","directDiffuse","indirectDiffuse","directSpecular","indirectSpecular","subsurface","transmissive"]
        if os.path.isfile(file):
            self.filter_file=file
            self.filter_file_dir=os.path.split(file)[0]
            self.filter_file_name=os.path.split(file)[1]
            channel_info=self.channelInfo()
            for channel in channels_list:
                if channel in self.filter_file_name:
                    self.img_base_name=self.filter_file_name.split("_"+channel)[0]
                    self.baseName_LE.setText(self.img_base_name)

    def filterExrBro(self):
        pathExt= QtWidgets.QFileDialog.getOpenFileName(filter='*.exr')[0]
        pathExt=pathExt.replace('\\','/')
        if pathExt !="":
            self.filterExr_LE.setText(pathExt)
            self.setFilterInfo()

    def filterExrOpen(self):
        file=self.filterExr_LE.text()
        file_dir=os.path.split(file)[0]
        file_dir=file_dir.replace('\\','/')
        os.startfile(file_dir)

    def outputExrBro(self):
        output_dir= QtWidgets.QFileDialog.getExistingDirectory()
        output_dir=output_dir.replace('\\','/')
        if output_dir !="":
            self.outDir_LE.setText(output_dir)

    def outputExrOpen(self):
        output_dir=self.outDir_LE.text()
        os.startfile(output_dir)

    def showChannels(self):
        self.setFilterInfo()
        exr_list=self.exrList(self.filter_file_dir)
        start_frame=int(self.frameRangeStart_LE.text())
        end_frame=int(self.frameRangeEnd_LE.text())
        num_list=range(start_frame,end_frame+1)
        aov_name=self.aovLightGrpName_LE.text()
        aov_list=aov_name.split(',')
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(len(num_list)*len(aov_list))
        self.progressBar.setValue(0)
        self.channel_info=self.channelInfo()
        self.affect_channel_list=[]

        for exr in exr_list:
            for channel in self.channel_info:
                full_name=self.img_base_name+"_"+channel['type']+"_"+channel['aov']+"_filtered"
                if full_name in exr:
                    channel['exist'].append(exr)
        for channel in self.channel_info:
            full_name=self.img_base_name+"_"+channel['type']+"_"+channel['aov']+"_filtered"
            if len(channel['exist'])>0:
                for i in num_list:
                    num="%04d" % i
                    if full_name+'.'+num+'.exr' not in channel['exist']:
                        channel['exile'].append(num)
            if len(channel['exist'])>0 and len(channel['exile'])==0:
                if channel['type'] not in self.affect_channel_list:
                    self.affect_channel_list.append(channel['type'])
        for channel in self.channel_info:
            if len(channel['exile'])>0:
                if channel['type'] in self.affect_channel_list:
                    self.affect_channel_list.remove(channel['type'])
        self.affect_channel_list.sort()
        self.checkChannel_LE.setText("")
        channels=""
        for channel in self.affect_channel_list:
            channels=channels+" "+channel
        self.checkChannel_LE.setText(channels)

    def channelInfo(self):
        aov_name=self.aovLightGrpName_LE.text()
        aov_list=aov_name.split(',')
        channel_info=[]
        channels_list=["diffuse","specular","directDiffuse","indirectDiffuse","directSpecular","indirectSpecular","subsurface","transmissive"]
        for aov in aov_list:
            for channel in channels_list:
                channel_dic={}
                channel_dic['aov']=aov
                channel_dic['type']=channel
                channel_dic['exist']=[]
                channel_dic['exile']=[]
                channel_info.append(channel_dic)
        return channel_info

    def exrList(self,path):
        file_list=os.listdir(path)
        exr_list=[]
        for i in file_list:
            if os.path.isfile(path+"/"+i):
                if os.path.splitext(i)[1]==".exr":
                    exr_list.append(i)
        exr_list.sort()
        return exr_list

    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        return False

    def mergerEXR_run(self):
        self.info_textEdit.clear()
        self.info_textEdit.append("run merge ...")
        self.showChannels()
        start_frame=int(self.frameRangeStart_LE.text())
        end_frame=int(self.frameRangeEnd_LE.text())
        num_list=range(start_frame,end_frame+1)
        thread_class=merge_thread(num_list,self.img_base_name,self.final_name_LE.text(),self.aovLightGrpName_LE.text(),self.outDir_LE.text(),self.affect_channel_list,self.filter_file_dir)
        thread_class.count.connect(self.updateProgressBar)
        thread_class.img_complete.connect(self.updateInfoBar)
        thread_class.all_complete.connect(self.updateInfoBar_complete)
        thread_class.cost_time.connect(self.time_cost)
        thread_class.start()
        time.sleep(0.5)

    def appendTextEdit(self):
        self.info_textEdit.clear()

    def updateProgressBar(self,count):
        self.progressBar.setValue(count)

    def updateInfoBar(self,export):
        self.info_textEdit.append(export+' has been created')

    def updateInfoBar_complete(self):
        self.info_textEdit.append('complete...')

    def time_cost(self,real_time):
        text="It cost %.2f sec" % (real_time)
        self.info_textEdit.append(text)
            
class merge_thread(QtCore.QThread):
    count = QtCore.Signal(int)
    img_complete= QtCore.Signal(str)
    all_complete= QtCore.Signal()
    cost_time= QtCore.Signal(float)
    def __init__(self,num_list,img_base_name,final_name,aovName,outDir,affect_channel_list,filter_file_dir):
        QtCore.QThread.__init__(self)
        self.num_list=num_list
        self.img_base_name=img_base_name
        self.final_name=final_name
        self.aov_list=aovName.split(',')
        self.outDir=outDir
        self.affect_channel_list=affect_channel_list
        self.filter_file_dir=filter_file_dir
        
    def run(self):
        time_Start = time.time()
        count=0
        for aov in self.aov_list:
            for i in self.num_list:
                ice_images_list=[]
                num="%04d" % i
                beauty_name=self.img_base_name+"_"+self.final_name+"_"+aov+"_filtered"+"."+num+".exr"
                export_file=self.outDir+"/"+beauty_name
                for channel in self.affect_channel_list:
                    image=self.filter_file_dir+"/"+self.img_base_name+"_"+channel+"_"+aov+"_filtered"+"."+num+".exr"
                    ice_image = ice.Load(image)
                    ice_images_list.append(ice_image)

                box=ice_images_list[0].DataBox()
                color = [0, 0, 0, 0]
                black_card = ice.FilledImage(ice.constants.FLOAT, box, color)
                result = black_card
                for image in ice_images_list:
                    result=result.Add(image)
                final_result = result.Interleave(black_card, [-3,-2, -1, 4])
                final_result.Save(export_file, ice.constants.FMT_EXRFLOAT)
                count=count+1
                self.count.emit(count)
                self.img_complete.emit(beauty_name)
            time.sleep(0.5)
        time_end = time.time()
        real_time = time_end - time_Start
        self.cost_time.emit(real_time)
        self.all_complete.emit()
        self.quit()



#---------------------------------------------------------------------------------------------------#
def main():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def prmanDenoiseToolsMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()
