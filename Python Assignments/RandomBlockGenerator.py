import maya.cmds as mc

AmountOfBlocks = 10
MinXVal = -10
MaxXVal = 10
MinYVal = -10
MaxYVal = 10
MinZVal = -10
MaxZVal = 10

def randItem(amntBlock, minValX, maxValX, minValY, maxValY, minValZ, maxValZ):
    import random
    for i in range(amntBlock):
        randX = random.randint(minValX, maxValX)
        randY = random.randint(minValY, maxValY) 
        randZ = random.randint(minValZ, maxValZ)  
        
        mc.polyCube()
        mc.move(randX, randY, randZ)
    
randItem(AmountOfBlocks, MinXVal, MaxXVal, MinYVal, MaxYVal, MinZVal, MaxZVal)