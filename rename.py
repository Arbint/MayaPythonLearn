from maya import cmds


SUFFIXES = {"mesh" : "geo",
            "joint" : "jnt",
            "camera" : None,
            "ambientLight" : "lgt"
            }
DEFAULT_SUFFIX = "grp"
def rename():
    selection = cmds.ls(selection=True)

    if len(selection) == 0:
        selection = cmds.ls(dag=True, long=True)

    selection.sort(key=len, reverse=True)
    for obj in selection:
        TransName = obj.split("|")[-1]
        Shapes = cmds.listRelatives(obj, children=True, fullPath=True) or [];
        if len(Shapes) == 1:
            ObjType = cmds.objectType(Shapes[0])
        else:
            ObjType = cmds.objectType(obj)

        subfix = SUFFIXES.get(ObjType, DEFAULT_SUFFIX)

        if not subfix:
            continue

        if obj.endswith(subfix):
            continue

        newName = TransName + "_" + subfix
        cmds.rename(obj, newName)