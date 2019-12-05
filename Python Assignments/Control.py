''' This tool creates a NURBS circle at the pivot of an object.
    This tool aslo colors it to desired color. 
    ! ! ! Note: This tool freezes transformations of geo on runtime ! ! !
    
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
    mc.makeIdentity(sels, apply = True) 
    if len(sels):
        for sel in sels:
            pivCen = mc.xform(sel, q = True, ws = True, scalePivot = True)
            Rot = mc.xform(sel, q = True, ws = True, rotation = True)
            createC = mc.circle (radius = UserDefinedRadius)
            mc.move(pivCen[0], pivCen[1], pivCen[2], createC)
            mc.rotate(Rot[0], Rot[1], Rot[2], createC)
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

# Questions #
# When I create a new nurb, it is place in the right area, but it's pivot is at 0  
    # Solution, create at 0, then move to desired location
# Issues #
# Rotation inconsistancies            