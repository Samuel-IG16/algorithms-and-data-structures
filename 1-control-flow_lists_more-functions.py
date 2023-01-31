# List, Control flow and more functions

# List
squares = [1, 4, 9, 16, 30]                     # creates a list
print(squares)

# Some list methods
squares[0]                                      # 1 - indexing
squares[:2]                                     # [1, 4] - slicing
print(squares + [36, 50, 64, 81, 100])          # concatenation
squares[4] = 25                                 # change value by index
print(squares)
squares[:] = []                                 # change value by slicing
print(squares)
print(len(squares))                             # 0 - length of list
squares.append(1)                               # add item at end of list
print(squares)

# If Statement
x = int(input('Please enter an integer: '))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# While loop
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b                               # Fibonacci Series

# For loop
words = ['cat', 'window', 'defense']
for word in words:
    print(word, len(word))

# The Range Function
# Used to generate a range of numbers
for num in range(10):                           # Optionally takes start, step arguments
    print(num)

# Break statements
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
else:
    print(n, 'is a prime number')

# Continue statement
for num in range(2, 10): 
    if num%2==0:
        print("Found an even number", num) 
        continue 
    print("Found a number", num)

# Exercise:
# 1
givenList = [5, 20, 15, 20, 25, 50, 20]
for num in givenList:
    if num == 20:
        givenList[givenList.index(num)] = 200
        break

print(givenList)

# 2
givenList2 = [5, 20, 15, 20, 25, 50, 20]
for num in givenList2:
    if num == 20:
        givenList2.remove(num)

print(givenList2)
        
# 3
myList = [1, 2, 3, 4, 5]
sum = 0
for num in myList:
    sum += num

print(sum)

# 4
result = [x**x for x in range(1, 31)]
print(result[:5] + result[-5:])

# More on Functions
def fib(n):
    """Print a Fibonacci series up to n."""                 # Function documentation
    a, b=0, 1
    while a < n: 
        print(a, end='')
        a, b = b, a+b
    print() 

fib(2000)

# Rename functions
print(fib)
f = fib
print(f(100))

# Functions retun None if no return statement is given

# Default argument values
def add(a, b=5):                                            # Positional arguments refers to the order of the function parameters
    sum = a + b
    return sum

print(add(2))                                               # Function call with required argument omitting default argument uses default value
print(add(2, 3))                                            # Function call with required argument and a value for default uses new default value

# Keyword argument
print(add(7, b=7))                                          # Function call with required argument and default argument assigned a value by calling the key `b` and assigning a new value to it

# Note: In a function call, keyword arguments must follow positional arguments.
#       All the keyword arguments passed must match one of the arguments accepted by the function
#       and their order is not important. No argument may receive a value more than once.

# Passing tuples and dictionary as function argument
def myFunc(*arg, **args):
    print(arg)
    print(args)

myFunc("Jammy")                                             # return a tuple with `jammy` and an empty dictionary
myFunc("Stephen", 1, 2, 3, shoe="nike")                     # because there is an assignment passed as an argument our dictionary is not returned empty

# Unpacking argument lists
firstList = [1, 2, 3]
secondList = [*firstList]                                   # unpack firstlist into secondlist
print(firstList)
print(secondList)

# Unpacking argument dictionaries
firstDict = {'age': 34}
secondDict = {**firstDict}                                  # unpacking firstdict into seconddict
print(firstDict)
print(secondDict)

# Lambda expressions
# Used to create small anonymous functions. used where function objects are required
v = 0
myFun = lambda u: u + v
print(myFun(3))