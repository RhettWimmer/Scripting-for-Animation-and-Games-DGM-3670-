''' This tool creates a NURBS circle at the pivot of an object.
    This tool aslo colors it to desired color. 
    
    User defined parameters: 
      -  UserDefinedColor = Sets the NURB to the selected color.
            Accepted inputs (Lowercase only): 'red', 'blue', 'yellow', 'green', 'purple'
      -  UserDefinedRadius = Sets the size of NURBS circle. Accepts a float or int value. 
'''

import maya.cmds as mc

UserDefinedColor = 'green'
UserDefinedRadius = 1

    # Create control function#
def createControl(UserDefinedRadius):
    
     # Selection #
    sels = mc.ls(sl = True)
    
    if len(sels):
        for sel in sels:
            selName1 = str(sel).replace("_Geo","")
            selName2 = selName1.replace("_Jnt","")
            pivCen = mc.xform(sel, q = True, ws = True, scalePivot = True)
            Rot = mc.xform(sel, q = True, ws = True, rotation = True)
            createC = mc.circle (name = selName2 + '_Ctrl ', radius = UserDefinedRadius)
            mc.move(pivCen[0], pivCen[1], pivCen[2], createC)
            mc.rotate(Rot[0], Rot[1], Rot[2], createC)
            
    if (len(sels) == 0):
        mc.circle(nr = [0, 1, 0], name = '_Ctrl',radius = UserDefinedRadius)
        print("peepe")       
    mc.warning('! ! ! Control placed sucessfully ! ! !')       
createControl(UserDefinedRadius)
    # Change color function #
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
    # Nurb Selector # 
    nurbs = mc.ls(type='nurbsCurve')
    mc.select(nurbs) 
        
    # Color changer #
    for shape in nurbs:
        mc.setAttr('%s.overrideEnabled' % shape, True)
        mc.setAttr('%s.overrideColor' % shape, colCode)

colorControl(UserDefinedColor)         