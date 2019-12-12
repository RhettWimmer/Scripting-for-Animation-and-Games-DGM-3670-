''' This tool renames a selection 
        User defined parameters: 
        LorR = Left or right.
        Apndg = The appendage Example: Leg, Arm, finger, etc.
        Type = Type of object Example: Geo, Joint, Control, etc. '''
import maya.cmds as mc
import Toolbox
reload (Toolbox)
LorR = Toolbox.newLorR
Apndg = Toolbox.newApndg
Type = Toolbox.newType

class Namer():
    Number = 0
    def renamer(self, lorR, apndg, type):
    
           sel = mc.ls(sl = True)
           
           if ((len(sel)) == 0):
               mc.warning('! ! ! Must make a selection ! ! !')
           else:
               mc.warning('! ! ! Rename Successful ! ! !') 
           
           for i in range(len(sel)):
                  if (i < 10): 
                      mc.rename(sel[i], lorR + "_" + apndg + "_" + "00" + str(i) + "_" + type)                            
                  elif (i >= 10 and i < 100):
                      mc.rename(sel[i], lorR + "_" + apndg + "_" + "0" + str(i) + "_" + type)
                  elif (i >= 100):
                      mc.rename(sel[i], lorR + "_" + apndg + "_" + str(i) + "_" + type)                   
    
RN = Namer()
RN.renamer(LorR, Apndg, Type)