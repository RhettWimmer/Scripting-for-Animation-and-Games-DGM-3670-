''' This tool finds the center of selection of polygon objects. '''
import maya.cmds as mc

class CenLoc():
    def centerLocator(self):
       loc = [0,0,0]
       sel = mc.ls(sl = True)
       big = len(sel)
       
       if (big > 0):
           dup =  mc.group(sel)
           
           box = mc.xform(dup, q = True, bb = True)
    
           loc[0] = ((box[0] + box [3]) / 2)
           loc[1] = ((box[1] + box [4]) / 2)
           loc[2] = ((box[2] + box [5]) / 2)
           mc.warning("! ! ! Locator Successfully Placed ! ! !")
       
           SpaceLoc = mc.spaceLocator( name = "Center_Locator")
           mc.move(loc[0], loc[1], loc[2], SpaceLoc)
           mc.ungroup(dup)
            
       if (big == 0):
            mc.warning(" ! ! ! Must make a selection ! ! !")
cenL = CenLoc()
cenL.centerLocator()