import maya.cmds as mc

UserDefinedColor = 'red'

def colorControl(UserDefinedColor):   
    
    # Color converter #
    if UserDefinedColor == 'red':
        colCode = 13
    
    # Selection #
    sels = mc.ls(sl = True)
    
    # Color changer #
    for sel in sels:
        shapes = mc.listRelatives(sel, c = True, shapes = True)
        
        for shape in shapes:
            mc.setAttr('%s.overrideEnabled' % shape, True)
            mc.setAttr('%s.overrideColor' % shape, colCode)

colorControl(UserDefinedColor)        
#piv = (mc.xform(sels, q = True, scalePivot = True))        
#print piv
        
        