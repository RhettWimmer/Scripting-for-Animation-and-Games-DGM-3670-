''' This tool creates a NURBS circle at the pivot of an object.
    This tool aslo colors it to desired color. 
    
    User defined parameters: 
      -  UserDefinedColor = Sets the NURB to the selected color.
            Accepted inputs (Lowercase only): 'red', 'blue', 'yellow', 'green', 'purple'
      -  UserDefinedRadius = Sets the size of NURBS circle. Accepts a float or int value. 
'''
import maya.cmds as mc

UserDefinedRadius = 1

class CC():
    def createControl(self, UserDefinedRadius):
    
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
        mc.warning('! ! ! Control placed sucessfully ! ! !')       
create = CC()
create.createControl(UserDefinedRadius)
