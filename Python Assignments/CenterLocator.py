import maya.cmds as mc
def CenterLocator():
   # Variables #
   box = 0
   loc = [0,0,0]
   
   # Determines selection and size #
   sel = mc.ls(sl = True)
   big = len(sel)
   
   # If selection is only 1 object # 
   if (big == 1):
        box = mc.xform(q = True, bb = True)
   
        loc[0] = ((box[0] + box [3]) / 2)
        loc[1] = ((box[1] + box [4]) / 2)
        loc[2] = ((box[2] + box [5]) / 2)
        mc.warning("! ! ! Locator Successfully Placed ! ! !")
   
        mc.spaceLocator(p = (loc[0], loc[1], loc[2]))
   # If selection is bigger than 1 object #     
   if (big > 1):
       dup =  mc.duplicate(sel)
       dup = mc.polyUnite(dup)
       
       box = mc.xform(dup, q = True, bb = True)

       loc[0] = ((box[0] + box [3]) / 2)
       loc[1] = ((box[1] + box [4]) / 2)
       loc[2] = ((box[2] + box [5]) / 2)
       mc.warning("! ! ! Locator Successfully Placed ! ! !")
   
       mc.spaceLocator(p = (loc[0], loc[1], loc[2]))
       mc.delete(dup, ch = True)
       mc.delete(dup[0])
       
   # If selection is 0, will not run #     
   if (big == 0):
        mc.warning(" ! ! ! Must make a selection ! ! !")
CenterLocator()
