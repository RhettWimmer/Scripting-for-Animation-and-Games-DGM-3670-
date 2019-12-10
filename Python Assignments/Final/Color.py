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