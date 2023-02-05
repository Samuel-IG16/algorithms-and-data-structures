"""
    Define a function in python that accepts 3 values and returns the maximum of three
    numbers
"""
try:
    value1 = eval(input("Enter first number: "))
    value2 = eval(input("Enter second number: "))
    value3 = eval(input("Enter third number: "))

    def maximum_number (value1,value2,value3):
        print("max:", max(value1,value2,value3))

    maximum_number(value1,value2,value3)
except:
    print("Invalid input")