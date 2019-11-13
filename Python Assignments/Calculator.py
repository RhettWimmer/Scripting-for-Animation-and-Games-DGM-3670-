Values = [10,5,30,50,100]
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

# Division # 
def Divi(Vals):
    total=Vals[0]
    print('Division:')
    for i in Vals:
        total /= i
    print(total)
Divi(Values)  

# Power # 
def Pow(Vals,PowerVal):
    import math
    total=0
    print('Power Totals Are:')
    for i in Vals:
        print math.pow(i,PowerVal)
Pow(Values,Power)

# Mean #
def Mean(Vals):
    print('Mean:')
    total=0
    size=len(Vals)
    for i in Vals:
        total += i
    print(total/size)
Mean(Values)

# Median #
def Median(Vals)
    Vals.sort()
Median(Values)