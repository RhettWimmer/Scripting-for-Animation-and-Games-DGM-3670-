import maya.cmds as m

m.polySphere(name = 'Top', r = 3)
m.xform('Top',
        ws = True,
        t = [0,8,0], 
        scale = [.3,.3,.3])


m.polyCylinder(name = 'Vase',
               r = 3, 
               subdivisionsHeight = 3,
               subdivisionsCaps = 1)
m.xform('Vase',
        ws = True,
        t = [0,1.8,0], 
        scale = [.77,1.78,.77],
        )
     
m.scale(1, 1, 1, 
        'Vase.e[0:19]')
m.scale(.6, 1, .6, 
        'Vase.e[20:39]')
m.polyExtrudeFacet('Vase.f[40:59]')
m.scale(2, 2, 2,  
        'Vase.e[40:59]')

m.duplicate('Vase', 
             name = 'VaseL2')
m.xform('VaseL2',
        t = [0, 4.9, 0],
        s = [0.6, 1.4, .6])
        
m.duplicate('Vase', 
             name = 'VaseL3')
m.xform('VaseL3',
        t = [0, 7, 0],
        s = [.4, .9, .4])
        
m.polyPlane(subdivisionsWidth = 0, 
            subdivisionsHeight = 0, 
            name = 'Water')
            
m.xform('Water',
        rotation = [89.5,10.5,-0.2],
        scale = [.6,1,2],
        t= [.42,6.6,2.4])
        
m.polyDisc()
m.xform(t = [0,2.9,0],
        scale = [4.2,4.2,4.2])
        
m.duplicate()
m.xform(t = [0,5.7,0],
        scale = [3.2,3.2,3.2])
        
m.duplicate()
m.xform(t = [0,7.515,0],
        scale = [2.2,2.2,2.2])
        
m.duplicate('Water', 
            name = 'Water2')
m.xform('Water2',
        t = [2.4,4.2,2.6],
        ro = [92.6,44.7,-0.6],
        scale = [.8,1,3.4])
        
m.duplicate('Water', 
            name = 'Water3')
m.xform('Water3',
        t = [-1.4,4.1,3.2],
        ro = [92.4,-27.1,.12],
        scale = [.3,1,3.4])
        

#Notes
#Why can't I name a polyDisk?
#Show how to set up maya in pycharm