''' This tool renames a selection 
        User defined parameters: 
        LorR = Left or right.
        Apndg = The appendage Example: Leg, Arm, finger, etc.
        Type = Type of object Example: Geo, Joint, Control, etc. '''

LorR = 'L'
Apndg = 'Leg'
Type = 'Geo'

import maya.cmds as mc
Number = 0
def renamer(lorR, apndg, number, type):

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

renamer(LorR, Apndg, Number, Type)