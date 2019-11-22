# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm


def fixTagAttr(rootGrp):
    root_grp = pm.PyNode(rootGrp)
    mesh_list = pm.listRelatives(root_grp, allDescendents=True, type='mesh')
    joint_list = pm.listRelatives(root_grp, allDescendents=True, type='joint')
    for joint in joint_list:
        bone_parent = pm.listRelatives(joint, p=True)
        joint.setAttr('bone_parent', bone_parent)
        joint.setAttr('bone_name', joint.nodeName())
        children_list = pm.listRelatives(joint, children=True)
        slot = False
        for i in children_list:
            if i.getShape() is not None:
                if i.getShape().type() == 'mesh':
                    slot = True
                    slot_name = i.nodeName()
        if slot is False:
            joint.setAttr('bone_slot', '')
        else:
            joint.setAttr('bone_slot', slot_name)
    for mesh in mesh_list:
        mesh_t = mesh.getTransform()
        slot_bone = pm.listRelatives(mesh_t, p=True)
        mesh_t.setAttr('slot_name', mesh_t.nodeName())
        mesh_t.setAttr('slot_bone', slot_bone)


def fixRotateObj(rootGrp):
    root_grp = pm.PyNode(rootGrp)
    temp_joint_list = pm.listRelatives(root_grp, allDescendents=True, type='joint')
    joint_list = filter(lambda x: pm.getAttr('%s.spine_tag' % (x)) == "spine_bone", temp_joint_list)
    set_key_dict = {}
    for joint in joint_list:
        count = pm.keyframe(joint, q=True, keyframeCount=True, attribute='rotateZ')
        if count > 1:
            obj_dict = setRotateKey(joint, count)
            set_key_dict[joint] = obj_dict
    print set_key_dict
    pm.undoInfo(ock=True)
    for obj in set_key_dict:
        for frame in set_key_dict[obj]:
            volue = set_key_dict[obj][frame]
            pm.setKeyframe(obj, t=[frame, frame], at='rz', v=volue)
    pm.undoInfo(cck=True)


def setRotateKey(obj, count):
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


fixRotateObj('spine_RootSkeleton')
