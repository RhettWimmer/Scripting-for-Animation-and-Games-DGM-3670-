'''
Enter a list of values for the calculator to solve in "Values"
Enter a value in to "Power" to calculate the power of "Values"
Define "userInput" to tell the calculator what function to solve for.
    1 = Add
    2 = Subtract
    3 = Multiply
    4 = Divide
    5 = Power
    6 = Mean
    7 = Median
    8 = Mode
'''
Values = [1,5,10,100,10,5,10]
Power = 3
userInput = 1

# Addition input 1 #
def Add(Vals):
    total = 0
    for i in Vals:
        total += i
    return total
Add(Values)


# Subtraction input 2 #
def Sub(Vals):
    total = 0
    for i in Vals:
        total -= i
    return total
Sub(Values)


# Multiplication input 3 #
def Multi(Vals):
    total = 1
    for i in Vals:
        total *= i
    return total
Multi(Values)


# Division input 4 #
def Divi(Vals):
    total = Vals[0]
    for i in Vals[1:]:
        total /= i
    return total
Divi(Values)


# Power input 5#
def Pow(Vals, PowerVal):
    import math
    if userInput == 5:
        print 'The powers of ' + str(Values) + " to the power of " + str(Power) + ' = '
    for i in Vals:
        if userInput == 5:
            print math.pow(i, PowerVal)
Pow(Values, Power)

# Mean input 6 #
def Mean(Vals):
    import statistics
    total = Vals
    if userInput == 6:
        print 'The mean of ' + str(Values) + ' = '
        print statistics.mean(total)
    return statistics.mean(total)
Mean(Values)

# Median input 7 #
def Median(Vals):
    import statistics
    total = Vals
    if userInput == 7:
        print 'The median of ' + str(Values) + ' = '
        print statistics.median(total)
    return statistics.median(total)
Median(Values)

# Mode input 8 #
def Mode(Vals):
    import statistics
    total = Vals
    if userInput == 8:
        print 'The mode of ' + str(Values) + ' = '
        print statistics.mode(total)
        return statistics.mode(total)
Mode(Values)

# Input Function #
def calculator(input):
    if input == 1:
        print 'Adding ' + str(Values) + ' = '
        print Add(Values)
    if input == 2:
        print 'Subtracting ' + str(Values) + ' = '
        print Sub(Values)
    if input == 3:
        print 'Multiplying ' + str(Values) + ' = '
        print Multi(Values)
    if input == 4:
        print 'Dividing ' + str(Values) + ' = '
        print Divi(Values)
calculator(userInput)

