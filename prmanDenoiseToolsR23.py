# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets
import maya.cmds as cmds
import pymel.core as pm
import os
import sys
import threading
import signal
import time
import multiprocessing
import datetime
import json
import getpass
import csv
prman_path = os.getenv('RMANTREE')
ice_path = prman_path + "lib\python2.7\Lib\site-packages\ice"
sys.path.append(ice_path)
import ice
maya_version = cmds.about(version=True)
username = getpass.getuser()
ui_path = 'C:/Users/' + username + '/Documents/maya/' + maya_version + '/scripts/ui'
sys.path.append(ui_path)
sys.path.append("//mcd-one/database/assets/scripts/maya_scripts/ui")

import prmanDenoiseToolsCmdR23_ui
reload(prmanDenoiseToolsCmdR23_ui)
import prmanDenoiseToolsMergeEXR_ui
reload(prmanDenoiseToolsMergeEXR_ui)


dialog = None


class Black_UI(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('renderman denoise tools' + ' v0.5' + u' by 小黑')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(800, 600)
        windows_layout = QtWidgets.QVBoxLayout()
        windows_layout.setContentsMargins(0, 0, 0, 0)
        windows_layout.setSpacing(0)
        self.setLayout(windows_layout)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.denoiseCMD_wid = denoiseCMD_ui()
        self.mergeEXR_wid = mergeEXR_ui()
        main_tab_Widget = QtWidgets.QTabWidget()
        main_tab_Widget.addTab(self.denoiseCMD_wid, "denoiseCMD")
        main_tab_Widget.addTab(self.mergeEXR_wid, "mergeEXR")
        self.layout().addWidget(main_tab_Widget)
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/prmanR22_tools.csv'
        self.python_temp_json = self.python_temp + '/prmanR22_tools.json'
        self.save_UI_list = [
            self.denoiseCMD_wid.varianceFile_LE,
            self.denoiseCMD_wid.denoiseFile_LE,
            self.denoiseCMD_wid.outDir_LE,
            self.denoiseCMD_wid.frameRangeStart_LE,
            self.denoiseCMD_wid.frameRangeEnd_LE,
            self.denoiseCMD_wid.outputBasename_CB,
            self.denoiseCMD_wid.output_dir_CB,
            self.denoiseCMD_wid.filterVariance_CB,
            self.denoiseCMD_wid.crossFrame_CB,
            self.denoiseCMD_wid.skipFirst_CB,
            self.denoiseCMD_wid.skipLast_CB,
            self.denoiseCMD_wid.filterLayersIndependently_CB,
            self.denoiseCMD_wid.layer_CB,
            self.denoiseCMD_wid.motionVector_CB,
            self.denoiseCMD_wid.configFile_CB,
            self.denoiseCMD_wid.json_LE,
            self.denoiseCMD_wid.nOfThreads_CB,
            self.denoiseCMD_wid.nOfThreads_SB,
            self.denoiseCMD_wid.GPU_CB,
            self.denoiseCMD_wid.filterVariance_CB,
            self.mergeEXR_wid.filterExr_LE,
            self.mergeEXR_wid.baseName_LE,
            self.mergeEXR_wid.aovLightGrpName_LE,
            self.mergeEXR_wid.outDir_LE,
            self.mergeEXR_wid.frameRangeStart_LE,
            self.mergeEXR_wid.frameRangeEnd_LE
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
        elif wid_type == QtWidgets.QSpinBox:
            widget.setValue(value)


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
        elif widget_type == QtWidgets.QSpinBox:
            return widget.value()

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

class denoiseCMD_ui(QtWidgets.QWidget, prmanDenoiseToolsCmdR23_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(denoiseCMD_ui, self).__init__(parent)
        self.setupUi(self)
        self.connectInterface()
        # self.variance_pathExt='E:/exercise/nuke_pro/sourceimages/beauty_RL/AA_variance.0001.exr'
        # self.AOV_lightGrp_name='key'
        # self.varianceFile_LE.setText(self.variance_pathExt)
        # self.aovLightGrpName_LE.setText(self.AOV_lightGrp_name)
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/denoiseCMD.csv'
        self.frameRangeStart_LE.setText("%04d" % 1)
        self.frameRangeEnd_LE.setText("%04d" % 1)
        self.layer_LE.setText("diffuse,specular,directDiffuse,indirectDiffuse,directSpecular,indirectSpecular,subsurface,transmissive")
        self.newName_LE.setText('filtered')
        self.motionVector_LE.setText('variance')
        self.rman_folder = os.getenv('RMANTREE')
        # self.output_dir_CB.setCheckState(QtCore.Qt.CheckState(2))
        self.newName_LE.setEnabled(False)
        self.layer_LE.setEnabled(False)
        self.motionVector_LE.setEnabled(False)
        self.nOfThreads_SB.setEnabled(False)
        cpu_cores = multiprocessing.cpu_count()
        self.nOfThreads_SB.setRange(1, cpu_cores)
        self.nOfThreads_SB.setValue(cpu_cores)

    def connectInterface(self):
        self.varianceFileOpen_PB.clicked.connect(self.varianceOpenFile)
        self.varianceFileBro_PB.clicked.connect(self.variancePathBro)
        self.denoiseFileOpen_PB.clicked.connect(self.denoiseFileOpen_PB_hit)
        self.denoiseFileBro_PB.clicked.connect(self.denoiseFileBro_PB_hit)
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
        pathExt = self.varianceFile_LE.text()
        pathExt = pathExt.replace('\\', '/')
        if os.path.isfile(pathExt):
            self.variance_pathExt = pathExt
            self.variance_path = os.path.split(pathExt)[0]
            self.variance_name = os.path.split(pathExt)[1]
            name = os.path.splitext(self.variance_name)[0]
            name = os.path.splitext(name)[0]
            '''
            self.img_base_name = name.replace('_variance', '')
            if self.aovLightGrpName_LE.text() != "":
                self.imageName_label.setText(
                    self.img_base_name + "_channel_" + self.aovLightGrpName_LE.text() + "_")
            '''

    def variancePathBro(self):
        pathExt = QtWidgets.QFileDialog.getOpenFileName(filter='*.exr')[0]
        pathExt = pathExt.replace('\\', '/')
        if pathExt != "":
            self.varianceFile_LE.setText(pathExt)
            # self.setVariancePath()

    def varianceOpenFile(self):
        variance_file = self.varianceFile_LE.text()
        variance_path = os.path.split(variance_file)[0]
        os.startfile(variance_path)

    def denoiseFileBro_PB_hit(self):
        pathExt = QtWidgets.QFileDialog.getOpenFileName(filter='*.exr')[0]
        pathExt = pathExt.replace('\\', '/')
        if pathExt != "":
            self.denoiseFile_LE.setText(pathExt)
            # self.setVariancePath()

    def denoiseFileOpen_PB_hit(self):
        denoise_file = self.denoiseFile_LE.text()
        denoise_file = os.path.split(denoise_file)[0]
        os.startfile(denoise_file)

    def outputExrBro(self):
        output_dir = QtWidgets.QFileDialog.getExistingDirectory()
        output_dir = output_dir.replace('\\', '/')
        if output_dir != "":
            self.outDir_LE.setText(output_dir)

    def outputExrOpen(self):
        output_dir = self.outDir_LE.text()
        output_dir = output_dir.replace('/', '\\')
        os.startfile(output_dir)

    def json_window_PB_hit(self):
        self.jsonWindow = jsonWindow(self)
        self.jsonWindow.show()

    def newName_CB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.newName_LE.setEnabled(True)
            self.outputBasename_CB.setChecked(False)
        else:
            self.newName_LE.setEnabled(False)

    def outputBasename_CB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.newName_CB.setChecked(False)

    def outputDirCB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.outDir_LE.setEnabled(True)
        else:
            self.outDir_LE.setEnabled(False)

    def layerCB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.layer_LE.setEnabled(True)
        else:
            self.layer_LE.setEnabled(False)

    def motionVectorCB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.motionVector_LE.setEnabled(True)
            self.crossFrame_CB.setChecked(True)
        else:
            self.motionVector_LE.setEnabled(False)

    def configFileCB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.json_LE.setEnabled(True)
            self.json_window_PB.setEnabled(True)
        else:
            self.json_LE.setEnabled(False)
            self.json_window_PB.setEnabled(False)

    def nOfThreadsCB_hit(self, state):
        if state == QtCore.Qt.Checked:
            self.nOfThreads_SB.setEnabled(True)
        else:
            self.nOfThreads_SB.setEnabled(False)

    def rebuildBat(self):
        self.runCommend_textEdit.clear()
        start_frame = int(self.frameRangeStart_LE.text())
        end_frame = int(self.frameRangeEnd_LE.text())
        num_list = range(start_frame, end_frame + 1)
        variance_tex = self.varianceFile_LE.text()
        var_path, var_name, var_ext = self.path_data(variance_tex)
        print "var_name : %s " % (var_name)
        print "var_path : %s " % (var_path)
        denoise_tex = self.denoiseFile_LE.text()
        denoise_path, denoise_name, denoise_ext = self.path_data(denoise_tex)
        cmd_num = ""
        for num in num_list:
            num = "%04d" % num
            if cmd_num == "":
                cmd_num = num
            else:
                cmd_num = cmd_num + ',' + num
        if ',' in cmd_num:
            cmd_num = '{' + cmd_num + '}'
        print "cmd_num : %s " % (cmd_num)

        denoiseCMD = "\"" + self.rman_folder + "\\bin\\denoise.exe" + "\""
        denoiseCMD = self.denoiseFlagCheck(denoiseCMD)
        denoiseCMD = denoiseCMD + " " + var_path + "\\" + var_name + cmd_num + ".exr" +" " + denoise_path + "\\" + denoise_name + cmd_num + ".exr"
        self.runCommend_textEdit.append(denoiseCMD)

    def exportBat(self):
        x = datetime.datetime.now()
        time_data = "%02d" % x.month + "%02d" % x.day + "%02d" % x.hour + "%02d" % x.minute + "%02d" % x.second
        denoise_bat = self.outDir_LE.text() + '/' + 'prmanDenoise_' + time_data + '.bat'
        file = open(denoise_bat, 'w')
        file.write(self.runCommend_textEdit.toPlainText())
        file.close()

    def denoiseFlagCheck(self, cmd):
        if self.GPU_CB.isChecked():
            cmd = cmd + ' --override gpuIndex 0'
        if self.newName_CB.isChecked():
            newName = self.newName_LE.text()
            cmd = cmd + ' -o ' + newName
        if self.outputBasename_CB.isChecked():
            cmd = cmd + ' -n'
        if self.output_dir_CB.isChecked():
            outDir = self.outDir_LE.text()
            outDir = outDir.replace("/", "\\")
            cmd = cmd + " --outdir " + outDir
        if self.filterVariance_CB.isChecked():
            cmd = cmd + ' --filtervariance'
        if self.crossFrame_CB.isChecked():
            cmd = cmd + ' --crossframe'
        if self.skipFirst_CB.isChecked():
            cmd = cmd + ' --skipfirst'
        if self.skipLast_CB.isChecked():
            cmd = cmd + ' --skiplast'
        if self.filterLayersIndependently_CB.isChecked():
            cmd = cmd + ' --override filterLayersIndependently'
        if self.layer_CB.isChecked():
            layers = self.layer_LE.text()
            cmd = cmd + ' --layers ' + '\'' + layers + '\''
        if self.motionVector_CB.isChecked():
            name = self.motionVector_LE.text()
            cmd = cmd + ' -v ' + name
        if self.configFile_CB.isChecked():
            text = self.json_LE.text()
            json_list = text.split(' + ')
            for json in json_list:
                cmd = cmd + ' -f ' + json
        if self.nOfThreads_CB.isChecked():
            num = self.nOfThreads_SB.value()
            cmd = cmd + ' -t ' + str(num - 1)
        return cmd

    def channelInfo(self):
        channel_info = []
        channels_list = [
            "diffuse",
            "specular",
            "directDiffuse",
            "indirectDiffuse",
            "directSpecular",
            "indirectSpecular",
            "subsurface",
            "transmissive"
        ]
        for channel in channels_list:
            channel_dic = {}
            channel_dic['type'] = channel
            channel_dic['exist'] = []
            channel_dic['exile'] = []
            channel_info.append(channel_dic)
        return channel_info

    def exrList(self, path):
        file_list = os.listdir(path)
        exr_list = []
        for i in file_list:
            if os.path.isfile(path + "/" + i):
                if os.path.splitext(i)[1] == ".exr":
                    exr_list.append(i)
        exr_list.sort()
        return exr_list

    def path_data(self, path):
        path, file = os.path.split(path)
        path = path.replace("/", "\\")
        file_name, ext = os.path.splitext(file)
        file_name = self.withoutNum(file_name)
        return path, file_name, ext

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
            name = name[0:numMax - 1]
        return name


class jsonWindow(QtWidgets.QWidget):
    def __init__(self, parentObj):
        QtWidgets.QWidget.__init__(self)
        self.parentObj = parentObj
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle('select json files')
        self.layout().setContentsMargins(2, 2, 2, 2)
        self.layout().setSpacing(4)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        json_layout = QtWidgets.QVBoxLayout()
        json_layout.setContentsMargins(2, 2, 2, 2)
        json_layout.setSpacing(2)
        self.layout().addLayout(json_layout)
        PB_layout = QtWidgets.QHBoxLayout()
        add_PB = QtWidgets.QPushButton('add')
        PB_layout.addWidget(add_PB)
        clear_PB = QtWidgets.QPushButton('clear')
        PB_layout.addWidget(clear_PB)
        close_PB = QtWidgets.QPushButton('close')
        PB_layout.addWidget(close_PB)
        self.layout().addLayout(PB_layout)
        clear_PB.clicked.connect(self.clear_PB_hit)
        add_PB.clicked.connect(self.add_PB_hit)
        close_PB.clicked.connect(self.close)
        self.rman_folder = os.getenv('RMANTREE')
        json_LE = self.parentObj.json_LE.text()
        json_to_list = json_LE.split(' + ')
        json_folder = self.rman_folder + '/lib/denoise'
        file_list = os.listdir(json_folder)
        json_list = []
        for i in file_list:
            if os.path.splitext(i)[1] == ".json":
                json_list.append(i)
        json_list.sort()
        self.json_info_list = []
        for index, json in enumerate(json_list):
            json_dict = {}
            json_dict['name'] = json
            json_dict['CB'] = QtWidgets.QCheckBox(json)
            self.json_info_list.append(json_dict)
            json_layout.addWidget(json_dict['CB'])

        json_LE = self.parentObj.json_LE.text()
        json_to_list = json_LE.split(' + ')
        for i in self.json_info_list:
            if i['name'] in json_to_list:
                i['CB'].setChecked(True)

    def add_PB_hit(self):
        self.agree_json = []
        for i in self.json_info_list:
            if i['CB'].isChecked():
                self.agree_json.append(i['name'])
        text = ""
        for i in self.agree_json:
            if text == "":
                text = text + i
            else:
                text = text + " + " + i
        self.parentObj.json_LE.setText(text)

    def clear_PB_hit(self):
        for i in self.json_info_list:
            i['CB'].setChecked(False)
        self.parentObj.json_LE.setText("")


class mergeEXR_ui(QtWidgets.QWidget, prmanDenoiseToolsMergeEXR_ui.Ui_main_widget):
    def __init__(self, parent=None):
        super(mergeEXR_ui, self).__init__(parent)
        self.setupUi(self)
        username = getpass.getuser()
        self.python_temp = 'C:/Users/' + username + '/Documents/maya/python_tools_temp'
        self.python_temp_csv = self.python_temp + '/mergeEXR.csv'
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
        file = self.filterExr_LE.text()
        file = file.replace('\\', '/')
        channels_list = [
            "diffuse",
            "specular",
            "directDiffuse",
            "indirectDiffuse",
            "directSpecular",
            "indirectSpecular",
            "subsurface",
            "transmissive"
        ]
        if os.path.isfile(file):
            self.filter_file = file
            self.filter_file_dir = os.path.split(file)[0]
            self.filter_file_name = os.path.split(file)[1]
            channel_info = self.channelInfo()
            for channel in channels_list:
                if channel in self.filter_file_name:
                    self.img_base_name = self.filter_file_name.split("_" + channel)[0]
                    self.baseName_LE.setText(self.img_base_name)

    def filterExrBro(self):
        pathExt = QtWidgets.QFileDialog.getOpenFileName(filter='*.exr')[0]
        pathExt = pathExt.replace('\\', '/')
        if pathExt != "":
            self.filterExr_LE.setText(pathExt)
            self.setFilterInfo()

    def filterExrOpen(self):
        file = self.filterExr_LE.text()
        file_dir = os.path.split(file)[0]
        file_dir = file_dir.replace('\\', '/')
        os.startfile(file_dir)

    def outputExrBro(self):
        output_dir = QtWidgets.QFileDialog.getExistingDirectory()
        output_dir = output_dir.replace('\\', '/')
        if output_dir != "":
            self.outDir_LE.setText(output_dir)

    def outputExrOpen(self):
        output_dir = self.outDir_LE.text()
        os.startfile(output_dir)

    def showChannels(self):
        self.setFilterInfo()
        exr_list = self.exrList(self.filter_file_dir)
        start_frame = int(self.frameRangeStart_LE.text())
        end_frame = int(self.frameRangeEnd_LE.text())
        num_list = range(start_frame, end_frame + 1)
        aov_name = self.aovLightGrpName_LE.text()
        aov_list = aov_name.split(',')
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(len(num_list) * len(aov_list))
        self.progressBar.setValue(0)
        self.channel_info = self.channelInfo()
        self.affect_channel_list = []

        for exr in exr_list:
            for channel in self.channel_info:
                full_name = self.img_base_name + "_" + \
                    channel['type'] + "_" + channel['aov'] + "_filtered"
                if full_name in exr:
                    channel['exist'].append(exr)
        for channel in self.channel_info:
            full_name = self.img_base_name + "_" + \
                channel['type'] + "_" + channel['aov'] + "_filtered"
            if len(channel['exist']) > 0:
                for i in num_list:
                    num = "%04d" % i
                    if full_name + '.' + num + '.exr' not in channel['exist']:
                        channel['exile'].append(num)
            if len(channel['exist']) > 0 and len(channel['exile']) == 0:
                if channel['type'] not in self.affect_channel_list:
                    self.affect_channel_list.append(channel['type'])
        for channel in self.channel_info:
            if len(channel['exile']) > 0:
                if channel['type'] in self.affect_channel_list:
                    self.affect_channel_list.remove(channel['type'])
        self.affect_channel_list.sort()
        self.checkChannel_LE.setText("")
        channels = ""
        for channel in self.affect_channel_list:
            channels = channels + " " + channel
        self.checkChannel_LE.setText(channels)

    def channelInfo(self):
        aov_name = self.aovLightGrpName_LE.text()
        aov_list = aov_name.split(',')
        channel_info = []
        channels_list = ["diffuse", "specular", "directDiffuse", "indirectDiffuse",
                         "directSpecular", "indirectSpecular", "subsurface", "transmissive"]
        for aov in aov_list:
            for channel in channels_list:
                channel_dic = {}
                channel_dic['aov'] = aov
                channel_dic['type'] = channel
                channel_dic['exist'] = []
                channel_dic['exile'] = []
                channel_info.append(channel_dic)
        return channel_info

    def exrList(self, path):
        file_list = os.listdir(path)
        exr_list = []
        for i in file_list:
            if os.path.isfile(path + "/" + i):
                if os.path.splitext(i)[1] == ".exr":
                    exr_list.append(i)
        exr_list.sort()
        return exr_list

    def is_number(self, s):
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
        start_frame = int(self.frameRangeStart_LE.text())
        end_frame = int(self.frameRangeEnd_LE.text())
        num_list = range(start_frame, end_frame + 1)
        thread_class = merge_thread(num_list, self.img_base_name, self.final_name_LE.text(
        ), self.aovLightGrpName_LE.text(), self.outDir_LE.text(), self.affect_channel_list, self.filter_file_dir)
        thread_class.count.connect(self.updateProgressBar)
        thread_class.img_complete.connect(self.updateInfoBar)
        thread_class.all_complete.connect(self.updateInfoBar_complete)
        thread_class.cost_time.connect(self.time_cost)
        thread_class.start()
        time.sleep(0.5)

    def appendTextEdit(self):
        self.info_textEdit.clear()

    def updateProgressBar(self, count):
        self.progressBar.setValue(count)

    def updateInfoBar(self, export):
        self.info_textEdit.append(export + ' has been created')

    def updateInfoBar_complete(self):
        self.info_textEdit.append('complete...')

    def time_cost(self, real_time):
        text = "It cost %.2f sec" % (real_time)
        self.info_textEdit.append(text)


class merge_thread(QtCore.QThread):
    count = QtCore.Signal(int)
    img_complete = QtCore.Signal(str)
    all_complete = QtCore.Signal()
    cost_time = QtCore.Signal(float)

    def __init__(self, num_list, img_base_name, final_name, aovName, outDir, affect_channel_list, filter_file_dir):
        QtCore.QThread.__init__(self)
        self.num_list = num_list
        self.img_base_name = img_base_name
        self.final_name = final_name
        self.aov_list = aovName.split(',')
        self.outDir = outDir
        self.affect_channel_list = affect_channel_list
        self.filter_file_dir = filter_file_dir

    def run(self):
        time_Start = time.time()
        count = 0
        for aov in self.aov_list:
            for i in self.num_list:
                ice_images_list = []
                num = "%04d" % i
                beauty_name = self.img_base_name + "_" + \
                    self.final_name + "_" + aov + "_filtered" + "." + num + ".exr"
                export_file = self.outDir + "/" + beauty_name
                for channel in self.affect_channel_list:
                    image = self.filter_file_dir + "/" + self.img_base_name + \
                        "_" + channel + "_" + aov + "_filtered" + "." + num + ".exr"
                    ice_image = ice.Load(image)
                    ice_images_list.append(ice_image)

                box = ice_images_list[0].DataBox()
                color = [0, 0, 0, 0]
                black_card = ice.FilledImage(ice.constants.FLOAT, box, color)
                result = black_card
                for image in ice_images_list:
                    result = result.Add(image)
                final_result = result.Interleave(black_card, [-3, -2, -1, 4])
                final_result.Save(export_file, ice.constants.FMT_EXRFLOAT)
                count = count + 1
                self.count.emit(count)
                self.img_complete.emit(beauty_name)
            time.sleep(0.5)
        time_end = time.time()
        real_time = time_end - time_Start
        self.cost_time.emit(real_time)
        self.all_complete.emit()
        self.quit()

# ---------------------------------------------------------------------------------------------------
def main():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()


def prmanDenoiseToolsR23Main():
    global dialog
    if dialog is None:
        dialog = Black_UI()
    dialog.show()
