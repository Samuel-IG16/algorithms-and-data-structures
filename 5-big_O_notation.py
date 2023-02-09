# Introduction to big O notation
# The big O measures the time complexity of an algorithm. It measures the worst case scenerio

# Simplification of the Big O notation

# O(n) - Proportional
def logItems(n):
    for i in range(n):
        print(i)

logItems(2)                                                     # for any value of n this program will run n times

# K*O(n) = O(n) - Drop constants
def logItems(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

logItems(3)                                                     # for any value of n this program will run n+n times

# O(n^2) - Loop within a loop
def logItems(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

logItems(4)                                                     # for any value of n this program will run n*n times

# O(n^2) + O(n) = O(n^2) - Drop Non-Dominants
def logItems(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for i in range(n):
        print(i)

logItems(5)                                                     # for any value of n this program will run n*n times

# O(1) - Constant time
def addItems(n):
    return n + n

print(addItems(6))                                              # for any value of n this program will run just once

# O(log n) - Divide and conquer

# O(a + b) - Different terms for input
def logItems(a, b):
    for i in range(a):
        print(i)
    
    for j in range(b):
        print(j)

logItems(7, 8)                                                  # for any value of a or b this program will run a+b times

# O(a * b) - Different terms for input
def logItems(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

logItems(9, 10)                                                 # for any value of a or b this program is going to run a*b times