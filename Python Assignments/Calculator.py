'''
Enter a list of values for the calculator to solve in "Values"
Enter a value in to "Power" to calculate the power of "Values"
Define "userInput" to tell the calculator what function to solve for. '''
Values = [100, 10, 10]
Power = 3
userInput = 1000

# Addition #
def Add(Vals):
    total = 0
    for i in Vals:
        total += i
    return total
Add(Values)


# Subtraction #
def Sub(Vals):
    total = 0
    for i in Vals:
        total -= i
    return total
Sub(Values)


# Multiplication #
def Multi(Vals):
    total = 1
    for i in Vals:
        total *= i
    return total
Multi(Values)


# Division #
def Divi(Vals):
    total = Vals[0]
    for i in Vals[1:]:
        total /= i
    return total
Divi(Values)


# Power #
def Pow(Vals, PowerVal):
    import math
    for i in Vals:
        print math.pow(i, PowerVal)
Pow(Values, Power)

# Mean #
def Mean(Vals):
    import statistics
    total = Vals
    return statistics.mean(total)
Mean(Values)

# Median #
def Median(Vals):
    import statistics
    total = Vals
    return statistics.median(total)
Median(Values)

# Mode #
def Mode(Vals):
    import statistics
    total = Vals
    return statistics.mode(total)
Mode(Values)

# Input Function #
def calculator(input):
    if input == 0:
        print Add(Values)
    if input == 1:
        print Sub(Values)
    if input == 2:
        print Multi(Values)
    if input == 3:
        print Divi(Values)
    if input == 4:
        Pow(Values, Power)
    if input == 5:
        Mean(Values)
    if input == 6:
        Median(Values)
    if input == 7:
        Mode(Values)
    else:
        print ('!!! Must determine a function to run. Refer to Help for user input directory. !!!')
calculator(userInput)

