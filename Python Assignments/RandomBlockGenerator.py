''' This tool scatters objects randomly in the scene.
    User defined parameters: 
    AmountOfBlocks = How many objects will be spawned.
    MinXVal, MaxXVal = Scale of were blocks can be spawned on X axis
    MinYVal, MaxYVal = Scale of were blocks can be spawned on Y axis
    MinZVal, MaxZVal = Scale of were blocks can be spawned on Z axis'''    

AmountOfBlocks = 10
MinXVal = -10
MaxXVal = 10
MinYVal = -10
MaxYVal = 10
MinZVal = -10
MaxZVal = 10

import maya.cmds as mc
def randItem(amntBlock, minValX, maxValX, minValY, maxValY, minValZ, maxValZ):
    import random
    sel = mc.ls(sl = True)
    for i in range(amntBlock):
        randX = random.randint(minValX, maxValX)
        randY = random.randint(minValY, maxValY) 
        randZ = random.randint(minValZ, maxValZ)  
        
        mc.duplicate(sel)
        mc.move(randX, randY, randZ, sel)
    
randItem(AmountOfBlocks, MinXVal, MaxXVal, MinYVal, MaxYVal, MinZVal, MaxZVal)
