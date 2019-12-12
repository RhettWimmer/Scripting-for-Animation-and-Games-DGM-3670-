# !! !! !! ! 
import maya.cmds as mc
import Color
reload (Color)
newLorR = "L"
newApndg = 'Leg'
newType = 'Geo'
class RWTools():
    def __init__(self):
        self.winName = "Rhett Wimmer's RADICAL ToolBox"
            # Calculator # 
    def TheCal(Self):    
        import Calculator
        reload (Calculator)     
    def create(self):
        self.Delete()
        self.winName = mc.window(self.winName, width=400, height=400)
        self.m_column = mc.columnLayout(p = self. winName, 
                        adj = True, 
                        bgc = [0,0.6,0.4])
# _______________________________ UI _______________________________#                 
        mc.button(label = 'Select All',
                  p = self.m_column,
                  command = lambda *args: mc.select(all = True),
                  bgc = [0, 0,0])
        # Center Locator UI (DONE)#          
        mc.button(label = 'Create Center Locator',
                  p = self.m_column,
                  command = lambda *args: self.Center())
        # Renamer UI # 
                                  
        print (mc.textField(p=self.m_column))    
                                                                                                   
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
                  command = lambda *args: (self.ContCtrl())) 
        # Color Changer UI (DONE) #          
        mc.button(label = 'Change Controls to Red',
                  p = self.m_column,
                  bgc = [0.5,0,0],
                  command = lambda *args: Color.ColorControl('red'))
        mc.button(label = 'Change Controls to Blue',
                  p = self.m_column,
                  bgc = [0,0,0.3],
                  command = lambda *args: Color.ColorControl('blue'))
        mc.button(label = 'Change Controls to Blue',
                  p = self.m_column,
                  bgc = [0.5,0.5,0],
                  command = lambda *args: Color.ColorControl('yellow'))                    
        mc.button(label = 'Change Controls to Green',
                  p = self.m_column,
                  bgc = [0,0.5,0],
                  command = lambda *args: Color.ColorControl('green'))                    
        mc.button(label = 'Change Controls to Purple',
                  p = self.m_column,
                  bgc = [0.5,0,0.5],
                  command = lambda *args: Color.ColorControl('purple'))                                                     
        # Calculator UI #          
        mc.button(label = 'Add',
                  p = self.m_column,
                  command = lambda *args: Calculator.Add(Values))                 
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
    #def ColChng(Self):
            #import Color
           # reload (Color)
            #Color.ColSel()                         
        # Delete Window #   
    def Delete(self):
        if (mc.window(self.winName, exists = True)):
            mc.deleteUI(self.winName) 
        
rwTools = RWTools()
rwTools.create()

#Issues: 
#    Window not deleting properly
#_________________________________________________