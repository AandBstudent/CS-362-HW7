# Prints the number from 1 to 100.
# But for multiples of 3 print "Fizz" instead of the number
# For the multiples of Five print "Buzz"
# For numbers which are multiples of both Three and Five
# print "FizzBuzz"

def check_Fizz(x):
    if(x % 3 == 0):
        return 'Fizz'
    else:
        return x

def check_Buzz(x):
    if(x % 5 == 0):
        return 'Buzz'
    else:
        return x
def check_FizzBuzz(x):
    if((x % 3 == 0) and (x % 5 == 0)):
        return 'FizzBuzz'
    else:
        return x

def Fizz_Buzz():
    pass