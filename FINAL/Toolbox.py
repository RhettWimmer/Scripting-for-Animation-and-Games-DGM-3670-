import maya.cmds as mc
import Color
import Calculator
import Renamer 
reload (Renamer)
reload (Color)
reload (Calculator)

LorR = "L"
Apndg = 'Leg'
Type = 'Geo'

Value = [1,10,50,50,100]
Power = 3

class RWTools():
    def __init__(self):
        self.winName = "Rhett Wimmer's RADICAL ToolBox"
            # Calculator # 
    def TheCal(self):    
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
                                      
        #self.RenameText = mc.textField(p = self.m_column, pht = "Rename")                                                                                        
        mc.button(label = 'Rename Selection',
                  p = self.m_column,
                  command = lambda *args: Renamer.renamer(LorR, Apndg, Type))

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
        mc.button(label = 'Change Controls to Yellow',
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
        #self.CalIn = mc.textField(p = self.m_column, pht = "Calculator")
        #CalVal = mc.textField(self.CalIn, q = True, text = True)   
     
        mc.button(label = 'Add',
                  p = self.m_column,
                  command = lambda *args: Calculator.Add(Value))                 
        mc.button(label = 'Subtract',
                  p = self.m_column,
                  command = lambda *args: Calculator.Sub(Value))
        mc.button(label = 'Multiply',
                  p = self.m_column,
                  command = lambda *args: Calculator.Multi(Value))                  
        mc.button(label = 'Divide',
                  p = self.m_column,
                  command = lambda *args: Calculator.Divi(Value))                    
        mc.button(label = 'Power',
                  p = self.m_column,
                  command = lambda *args: Calculator.Pow(Value,Power))                   
        mc.button(label = 'Mean',
                  p = self.m_column,
                  command = lambda *args: Calculator.Mean(Value))                    
        mc.button(label = 'Median',
                  p = self.m_column,
                  command = lambda *args: Calculator.Median(Value))                   
        mc.button(label = 'Mode',
                  p = self.m_column,
                  command = lambda *args: Calculator.Mode(Value))                                                                                                                      
        mc.showWindow(self.winName)
# _________________________ Functions _______________________________________ #         
        # Center Locator #
    def Center(self):
            import CenterLocator
            reload (CenterLocator)
            CenterLocator.CenLoc()
            
        # Renamer #
    '''def RenamerFunc(self):           
        RTValue = mc.textField(self.RenameText, q = True, text = True)
        RTX = RTValue.split()
        spli = []
        for i in RTX:
           spli.append(i)
        Renamer.renamer(spli)'''
        # Random Generator #    
    def randGen(self):
            import RandomBlockGenerator
            reload (RandomBlockGenerator) 
        # Control Creator #
    def ContCtrl(self):
            import Control
            reload (Control)                         
        # Delete Window #   
    def Delete(self):
        if (mc.window(self.winName, exists = True)):
            mc.deleteUI(self.winName)       
rwTools = RWTools()
rwTools.create()