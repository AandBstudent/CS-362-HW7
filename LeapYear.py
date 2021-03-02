# Conditions for a leap year:
# Years that are evenly divisble by 4
# except years that are evenly divisible by 100
# unless the years are also evenly divisble by 400.
def DivFour(x):
    if(x % 4 == 0):
        return True
    else:
        return False
def DivHundred(x):
    if(x % 100 == 0):
        return True
    else:
        return False

def DivHundredFour(x):
    if(x % 400 == 0):
        return True
    else:
        return False

def LeapYear():
    x = int(input("Enter a year: "))
    # Check if the year is divisible by Four
    if(DivFour(x)):
        # Check if the year is divisible by One Hundred
        if(DivHundred(x)):
            # Check if the year us divisible by Four Hundred
            if(DivHundredFour(x)):
                return print(str(x) + ' is a leap year')
            else:
                return print(str(x) + ' is not a leap year')
        else:
            return print(str(x) + ' is a leap year')
    else:
        return print(str(x) + ' is not a leap year')

LeapYear()