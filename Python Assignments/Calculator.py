Values = [2]
Power = [3]

# Addition #
def Add(Vals):
    total=0
    for i in Vals:
        total += i
    print(total)
    
Add(Values)

# Subtraction # 
def Sub(Vals):
    total=0
    for i in Vals:
        total -= i
    print(total)
Sub(Values)   

# Multiplication #
def Multi(Vals):
    total=1
    for i in Vals:
        total *= i
    print(total)
Multi(Values)

# Division # !!!!!!!!!!!!Help!!!!!!!!!!!!!!!!!
def Divi(Vals):
    total=0
    for i in Vals:
        total /= i
    print(total)
Divi(Values)  

# Power # !!!!!!!!!!!!Help!!!!!!!!!!!!!!!!!
def Pow(Vals,PowerVal):
    import math
    print math.pow(Vals,PowerVal)

Pow(Values,Power)