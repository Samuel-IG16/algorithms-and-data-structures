# Introduction
# Python recognizes and supports both primitive and non-primitive datatypes

# Primitive datatypes are pre-defined or built-in dataypes
print(type(1234567890))             # int - integers
print(type('Hi'))                   # str - strings
print(type(True))                   # bool - boolean
print(type(3.142))                  # float - floating point number

# Non-primitive datatypes are user defined and are derived from primitive datatypes
print(type([]))                     # list
print(type({}))                     # dict - dictionary

# Functions
# Python has alot of built in functions
print()                             # A print function call
type(10)                            # A type function call
help(dir)                           # A help function call
int('42')                           # An int function call
len("hi")                           # A len function call
list()                              # A list function call
max(5, 11, 2)                       # A max fucntion call
str(23)                             # A str function call......e.t.c.

# Integer Arithmetic
# Python does multiplication and division before addition and subtraction unless 
# there are parenthesis
print(5+4)                          # 9
print(2*3)                          # 6
print(5/2)                          # 2.5
print(5//2)                         # 2
print(5%2)                          # 1

# String Delimiters
print("Hello Wolrd")                # A double quote delimiter
print('Hello World')                # A single quote delimeter

# String concatenation
# Strings also have operation symbols which produce results depending on the operaands
print('Happy'+'sad')                # Happysad
print(3*'happy'+'sad')              # happyhappyhappysad
print('40'+'4')                     # 404
#print('40'+4)                      # error: operands must both be strings

# Exercise:
print(5*'Yes')                      # YesYesYesYesYes
print(3*'Maybe'+5*'Yes')            # MaybeMaybeMaybeYesYesYesYesYes

# Variables and assignment
# In python a variable is a reserved memory location
width = 20                          # assigned 20 to a variable called width
height = 20                         # assigned 20 to a variable called height
area = width * height               # assigned the product to a variable called area
print(area)                         # 400
# 12 = height                       # error: assignment is from right to left
width = width + 14                  # 34
first = 'Micheal'
last = 'Ogundero'
name = first + ' ' + last
print(name)

# Literals and identifiers
# Expressions like 27 or ’hello’ are called literals. 
# An identifier is the sequence of characters used to identify Python's variables or other entity. 
_snakeCase = 'December'           # A naming convention that begins with `_`
camelCase = 'Micheal'             # A naming convention that begins with lowercase
PascalCase = 'Ogundero'           # A naming convention that begins with uppercase ...(Note: Python is case sensitive)

# Keywords or reserved words in Python
True
False #...e.t.c

# Print Function
x = 3
y = 5
print('The sum of', x, 'plus', y, 'is', x + y)                  # comma separated adds space

# Strings
# We can have multi-line strings using triple ''' or """
sillyTest = '''Say, "I'm in!
This is line 3'''
print(sillyTest)                                                # The line structure is preserved in output

# Escape codes
print("This \"escapes\" the quotes using \\.\nI'm in a newline")
print('I\'m in single quotes')

# Input and Output
person = input('Enter your name: ')                             # Ask user for name as input
print('Hello', person, '!')

# Print with keyboard parameter `sep`
person = input("Enter your name: ")
print('Hello', person, '!', sep='')

# Numbers and Strings of Digits
x = input("Enter a number: ")
y = input("Enter a second number: ")
print("The sum of ", x, "and", y, "is", x + y, ".", sep=" ")    # To correct this convert x and y to int
x = int(x)
y = int(y)
print("The sum of ", x, "and", y, "is", x + y, ".", sep=" ")

# String format operation
person = input('Enter your name: ')
greeting = 'Hello, {}!'.format(person)                          # Double the braces to include braces in output
print(greeting)

# Defining Functions
def happyBirthdayTayo():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday dear Tayo.")
    
print(happyBirthdayTayo)                                        # Gives memory location of function
happyBirthdayTayo()

# Function parameters
def happyBirthday(name):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday dear " + name + ".")
    
happyBirthday("Jibola")                                         # Pass an argument to function on call
happyBirthday("Emmanuel")

# Return Function values
def f(x):
    return x*x                                                  # Can return any type of data, not just numbers

print(f(3))
print(f(3) + f(4))

# Local Scope
#def main():
#    r = 3
#    d()
    
#def d():
#    print(r)
    
#main()                                                          # error: r is local to main

def main():
    r = 3
    d(r)
    
def d(r):
    print(r)
    
main()                                                          # fixed 

# Global Constants
PI = 3.14159265358979                                           # global constant
def circleArea(radius): 
    return PI*radius*radius

print('circle area with radius 5: ', circleArea(5))

# Dictionaries
# A dictionary is a collection of key pair elements
myDict = {'firstName': 'Micheal', 'lastName': 'Ogundero'}
print(myDict)
print(myDict['firstName'])
print(myDict['lastName'])