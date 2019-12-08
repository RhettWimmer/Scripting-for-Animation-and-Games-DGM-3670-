import maya.cmds as mc

class RWTools():
    def __init__(self):
        self.winName = "Rhett Wimmer's RADICAL ToolBox"
        
    def create(self):
        self.winName = mc.window(self.winName, width=400, height=400)
        self.m_column = mc.columnLayout(p = self. winName, 
                        adj = True, 
                        bgc = [0,0.6,0.4])
        # Buttons #                 
        mc.button(label = 'Select All',
                  p = self.m_column,
                  command = lambda *args: mc.select(all = True),
                  bgc = [0, 0,0])
        mc.button(label = 'Center Locator',
                  p = self.m_column,
                  command = lambda *args: self.Center())       
        mc.showWindow(self.winName)
        
        # Center Locator #
    def Center(Self):
            import CenterLocator
            reload (CenterLocator)
            CenterLocator.CenLoc()
           
        # Delete Window #     
    def delete(self):
        if mc.window(self.winName, exists = True):
            mc.deleteUI(self.winName) 
        
rwTools = RWTools()
rwTools.create()

#Issues: 
#    Window not deleting properly
#_________________________________________________