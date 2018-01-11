import sys, pprint
import os
import getpass
from pyside2uic import compileUi

maya_version=cmds.about(version=True)
username=getpass.getuser()
ui_path='C:/Users/'+username+'/Documents/maya/'+maya_version+'/scripts/ui'


def convertUI(ui_name):
	ui_name=ui_name
	py_name=os.path.splitext(ui_name)[0]+'_ui.py'
	ui_file=ui_path+'/'+ui_name
	py_file=open(ui_path+'/'+py_name, 'w')
	compileUi(ui_file, py_file, False, 4,False)
	py_file.close()


convertUI('redShiftTools_objSet.ui')
convertUI('redShiftTools_objSet_mesh.ui')
convertUI('redShiftTools_objSet_objectId.ui')
convertUI('redShiftTools_objSet_visbility.ui')
convertUI('redShiftTools_objSet_matte.ui')

