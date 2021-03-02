# Checks if Number is multiple of 3
# Prints Fizz
def check_Fizz(x):
    if(x % 3 == 0):
        return 'Fizz'
    else:
        return x
# Checks if Number is multiple of Five
# prints Buzz
def check_Buzz(x):
    if(x % 5 == 0):
        return 'Buzz'
    else:
        return x
# Checks if Number is multiple of THREE and FIVE
# Prints FizzBuzz
def check_FizzBuzz(x):
    if((x % 3 == 0) and (x % 5 == 0)):
        return 'FizzBuzz'
    else:
        return x

# Prints the number from 1 to 100.
# But for multiples of 3 print "Fizz" instead of the number
# For the multiples of Five print "Buzz"
# For numbers which are multiples of both Three and Five
# print "FizzBuzz"
def Fizz_Buzz():

    for x in range(1, 101, 1):
        if ((x % 3 == 0) and (x % 5 == 0)):
            print(check_FizzBuzz(x))
        elif (x % 5 == 0):
            print(check_Buzz(x))
        elif (x % 3 == 0):
            print(check_Fizz(x))
        else:
            print(x)