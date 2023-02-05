"""
    Write a Python program which iterates the integers from 1 to 50. For multiples of three
    print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
    which are multiples of both three and five print "FizzBuzz".
"""
for number in range (1,51):
    if number % 3 == 0 and number  % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

