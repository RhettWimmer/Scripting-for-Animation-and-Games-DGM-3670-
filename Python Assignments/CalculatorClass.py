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

Values = [1,10,50,50]
Power = 3
userInput = 2

class Calculator:
    # Addition input 1 #
    def Add(self, Vals):
        total = 0
        for i in Vals:
            total += i
        if userInput == 1:
            print 'Adding ' + str(Values) + ' = '
            print total
            return total

    # Subtraction input 2#
    def Sub(self, Vals):
        total = Vals[0]
        for i in Vals[1:]:
            total -= i
        if userInput == 2:
            print 'Subtracting ' + str(Values) + ' = '
            print total
            return total

    ''' # Multiplication input 3 #
    def Multi(self, Vals):
        total = 1
        for i in Vals:
            total *= i
        return total'''

    # Division input 4 #
    '''def Divi(self, Vals):
        total = Vals[0]
        for i in Vals[1:]:
            total /= i
        return total'''

    # Power input 5#
    def Pow(self, Vals, PowerVal):
        import math
        if userInput == 5:
            print 'The powers of ' + str(Values) + " to the power of " + str(Power) + ' = '
        for i in Vals:
            if userInput == 5:
                print math.pow(i, PowerVal)

    # Mean input 6 #
    def Mean(self, Vals):
        import statistics
        total = Vals
        if userInput == 6:
            print 'The mean of ' + str(Values) + ' = '
            print statistics.mean(total)
        return statistics.mean(total)

    # Median input 7 #
    def Median(self, Vals):
        import statistics
        total = Vals
        if userInput == 7:
            print 'The median of ' + str(Values) + ' = '
            print statistics.median(total)
        return statistics.median(total)

    # Mode input 8 #
    def Mode(self, Vals):
        import statistics
        total = Vals
        if userInput == 8:
            print 'The mode of ' + str(Values) + ' = '
            print statistics.mode(total)
            return statistics.mode(total)

calc = Calculator()
calc.Add(Values)
calc.Sub(Values)
calc.Pow(Values, Power)
calc.Mean(Values)
calc.Median(Values)
calc.Mode(Values)