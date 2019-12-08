import maya.cmds as cmds

def test():
    '''
    sl = cmds.ls(sl= True)
    string = str(sl)
    selName = str(sl)
    selN = selName.split()
    
    if 'Geo' in string:
        gName = selN.replace("Geo","Ctrl")
        for i in sl:
            mc.circle(name = gName)
'''
    sl = cmds.ls(sl= True)  
    string = str(sl)  
    items = []
    
    for i in string:
        items.append(string)  
    print items
  
   #if string contains geo or jnt replace it with ctrl 
    #for s in sl:
     #   string = str(s)   
      #  x = s.find("1")
       # newString = s.replace("Cube","Ctrl")
        #print newString



#for "Cube" in s:
    #print(s.replace("Cube","Penis"))  
    
    
     
    #print (string.find('2'))
    
#cmds.select(sl)
test()