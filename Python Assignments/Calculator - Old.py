Values = [100, 10, 5, 1,1]
Power = 3


# Addition #
def Add(Vals):
    total = 0
    print('Addition:')
    for i in Vals:
        total += i
    print(total)


Add(Values)


# Subtraction #
def Sub(Vals):
    total = 0
    print('Subtraction:')
    for i in Vals:
        total -= i
    print(total)


Sub(Values)


# Multiplication #
def Multi(Vals):
    total = 1
    print('Multiplication:')
    for i in Vals:
        total *= i
    print(total)


Multi(Values)


# Division #
def Divi(Vals):
    total = Vals[0]
    print('Division:')
    for i in Vals[1:]:
        total /= i
    print(total)


Divi(Values)


# Power # 
def Pow(Vals, PowerVal):
    import math
    print('Power Totals Are:')
    for i in Vals:
        print math.pow(i, PowerVal)


Pow(Values, Power)


# Mean #
def Mean(Vals):
    print('Mean:')
    Vals.sort()
    total = 0
    size = len(Vals)
    for i in Vals:
        total += i
    print(total / size)


Mean(Values)


# Median #
def Median(Vals):
    print('Median:')
    Vals.sort()
    med = int((len(Vals) / 2))
    if len(Vals) % 2 == 0:
        total = (Vals[med - 1] + Vals[med]) / 2
    else:
        total = Vals[med]
    print(total)


Median(Values)


# Mode #
def Mode(Vals):

    import statistics
    print("Mode:")
    total = Vals
    print statistics.mode(total)

Mode(Values)
