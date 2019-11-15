Values = [100, 10, 10]
Power = 3

# Addition #
def Add(Vals):
    total = 0
    print('Addition:')
    for i in Vals:
        total += i
    print(total)
    return total
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
    import statistics
    total = Vals
    print statistics.mean(total)
Mean(Values)

# Median #
def Median(Vals):
    print('Median:')
    import statistics
    total = Vals
    print statistics.median(total)
Median(Values)

# Mode #
def Mode(Vals):
    import statistics
    print("Mode:")
    total = Vals
    print statistics.mode(total)
Mode(Values)



