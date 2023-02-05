"""
    Write a python code that prints all odd numbers between 1 and 100 using a while
 statement
"""
num = 1
while num <= 100:
    if num % 2 != 0:
        print(str(num) + ", ", end="")
    num += 1