import maya.cmds as mc

UserDefinedColor = 'blue'
UserDefinedRadius = 1

    # Selection #
sels = mc.ls(sl = True)
    # Create control #
def createControl(UserDefinedRadius):
    pivCen = mc.xform(sels, q = True, ws = True, scalePivot = True)
    Rot = mc.xform(sels, q = True, ws = True, rotation = True)
    createC = mc.circle(center = pivCen, radius = UserDefinedRadius)
    mc.select(all = True, vis = True)
    sel2 = mc.ls(sl = True)
    mc.rotate(Rot[0], Rot[1], Rot[2], sel2)       
createControl(UserDefinedRadius)

def colorControl(UserDefinedColor):   
    # Color converter #
    if UserDefinedColor == 'red':
        colCode = 13
    elif UserDefinedColor == 'blue':
        colCode = 6
    elif UserDefinedColor == 'yellow':
        colCode = 17  
    elif UserDefinedColor == 'green':
        colCode = 14 
    elif UserDefinedColor == 'purple':
        colCode = 9
    else:
        colCode = 0      
       
    # Color changer #
    for sel in sels:
        shapes = mc.listRelatives(sel, c = True, shapes = True)
        
        for shape in shapes:
            mc.setAttr('%s.overrideEnabled' % shape, True)
            mc.setAttr('%s.overrideColor' % shape, colCode)

colorControl(UserDefinedColor)                     