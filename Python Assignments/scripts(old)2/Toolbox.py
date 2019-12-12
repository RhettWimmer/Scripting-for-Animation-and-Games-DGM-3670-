# !! !! !! ! 

import maya.cmds as mc
newLorR = "Turd"
newApndg = 'nugget'
newType = 'Geo'

class RWTools():
    def __init__(self):
        self.winName = "Rhett Wimmer's RADICAL ToolBox"
        
    def create(self):
        self.delete()
        self.winName = mc.window(self.winName, width=400, height=400)
        self.m_column = mc.columnLayout(p = self. winName, 
                        adj = True, 
                        bgc = [0,0.6,0.4])
# _______________________________ UI _______________________________#                 
        mc.button(label = 'Select All',
                  p = self.m_column,
                  command = lambda *args: mc.select(all = True),
                  bgc = [0, 0,0])
        # Center Locator UI #          
        mc.button(label = 'Create Center Locator',
                  p = self.m_column,
                  command = lambda *args: self.Center())
        # Renamer UI #                    
        self.N = mc.textField(p = self.m_column,
                              width = 15)                 
        mc.button(label = 'Rename Selection',
                  p = self.m_column,
                  command = lambda *args: self.RenamerFunc())     
        # Random Generator UI #          
        mc.button(label = 'Random Placement Generator',
                  p = self.m_column,
                  command = lambda *args: self.randGen())  
        # Control Creator UI #          
        mc.button(label = 'Create Controls',
                  p = self.m_column,
                  command = lambda *args: self.ContCtrl()) 
        # Color Changer UI #          
        mc.button(label = 'Change Color',
                  p = self.m_column,
                  command = lambda *args: self.ColChng())
        # Calculator UI #          
        mc.button(label = 'Add',
                  p = self.m_column,
                  command = lambda *args: calc.Add(Values))                 
        mc.button(label = 'Subtract',
                  p = self.m_column,
                  command = lambda *args: calc.Sub(Values))
        mc.button(label = 'Multiply',
                  p = self.m_column,
                  command = lambda *args: calc.Multi(Values))                  
        mc.button(label = 'Divide',
                  p = self.m_column,
                  command = lambda *args: calc.Divi(Values))                    
        mc.button(label = 'Power',
                  p = self.m_column,
                  command = lambda *args: calc.Pow(Values,Power))                   
        mc.button(label = 'Mean',
                  p = self.m_column,
                  command = lambda *args: calc.Mean(Values))                    
        mc.button(label = 'Median',
                  p = self.m_column,
                  command = lambda *args: calc.Median(Values))                   
        mc.button(label = 'Mode',
                  p = self.m_column,
                  command = lambda *args: calc.Mode(Values))                                                                                                                      
        mc.showWindow(self.winName)
# _________________________ Functions _______________________________________ #         
        # Center Locator #
    def Center(Self):
            import CenterLocator
            reload (CenterLocator)
            CenterLocator.CenLoc()
            
        # Renamer #
    def RenamerFunc(Self):
            import Renamer
            reload (Renamer)   
            print newLorR
        # Random Generator #    
    def randGen(Self):
            import RandomBlockGenerator
            reload (RandomBlockGenerator)       
        # Control Creator #
    def ContCtrl(Self):
            import Control
            reload (Control)
        # Color Changer #
    def ColChng(Self):
            import Color
            reload (Color) 
        # Calculator # 
    def TheCal(Self):    
        import Calculator
        reload (Calculator)                           
        # Delete Window #   
    def delete(self):
        if (mc.window(self.winName, exists = True)):
            mc.deleteUI(self.winName) 
        
rwTools = RWTools()
rwTools.create()

#Issues: 
#    Window not deleting properly
#_________________________________________________