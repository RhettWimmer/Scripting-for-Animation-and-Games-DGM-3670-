Values = [3,10]
Power = 3

# Addition #
def Add(Vals):
    total=0
    print('Addition:')
    for i in Vals:
        total += i
    print(total)
    
Add(Values)

# Subtraction # 
def Sub(Vals):
    total=0
    print('Subtraction:')
    for i in Vals:
        total -= i
    print(total)
Sub(Values)   

# Multiplication #
def Multi(Vals):
    total=1
    print('Multiplication:')
    for i in Vals:
        total *= i
    print(total)
Multi(Values)

# Division # !!!!!!!!!!!!Help!!!!!!!!!!!!!!!!!
def Divi(Vals):
    total=0
    print('Division:')
    for i in Vals:
        total /= i
    print(total)
Divi(Values)  

# Power # !!!!!!!!!!!!Help!!!!!!!!!!!!!!!!!
def Pow(Vals,PowerVal):
    import math
    total=0
    print('Power Totals Are:')
    for i in Vals:
        print math.pow(i,PowerVal)

Pow(Values,Power)

# Mode #
#import statistics 