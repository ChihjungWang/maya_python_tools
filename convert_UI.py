import sys, pprint
import os
import getpass
import maya.cmds as cmds
from pyside2uic import compileUi


maya_version = cmds.about(version=True)
username = getpass.getuser()
maya_path = 'C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'
print maya_path

def convertUI(ui_path, ui_name):
    py_name = os.path.splitext(ui_name)[0]+'_ui.py'
    ui_file = ui_path+'/'+ui_name
    py_file = open(ui_path+'/'+py_name, 'w')
    compileUi(ui_file, py_file, False, 4, False)
    py_file.close()


convertUI(maya_path, 'prmanToolsDelUnknow.ui')

convertUI(maya_path, 'pixiTools_export_spine_json.ui')



convertUI(maya_path, 'prmanR22_tools_archiveEdit.ui')
convertUI(maya_path, 'prmanR22_tools_renderSets.ui')
convertUI(maya_path, 'prmanR22_tools_renderSetUp.ui')



nuke_ui_path = 'C:/Users/'+username+'/.nuke/ui'
convertUI(nuke_ui_path, 'blackToolkit_imagesArchive.ui')
convertUI(nuke_ui_path, 'blackToolkit_textureEdit.ui')
