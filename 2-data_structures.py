# More on lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))                                # Counts the number of occurence
print(fruits.index('orange'))                               # Returns index position of item
fruits.reverse()                                            # Reverses the list
print(fruits)
fruits.append('Cashew')                                     # Adds item to end of list
print(fruits)
fruits.sort()                                               # Order the list in ascending or descending order
print(fruits)
print(fruits.pop())                                         # Deletes the last item in array and returns it
print(fruits)

# Using lists as stacks
# In stacks it's Last in First out (LIFO)
# Python's list methods makes this easy to implement

stack = []
print(stack)
stack.append('first arrival, gonna leave last!')             # To add item to top of stack use append
print(stack)
stack.append('Second arrival!')
print(stack)
stack.append('last arrival, gonna leave first :)')
print(stack)
firstRetrieved = stack.pop()                                  # To retreive item from top of the stack use pop
print('Hey!', firstRetrieved, 'got out first :)')
print(stack)

# using lists as queues
# In queues it's First in First out (FIFO)
# Python's list are not efficient for this purpose instead collections.deque works
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")                                           # Terry arrives
print(queue)
queue.append("Graham")                                          # Graham arrives
print(queue)
queue.popleft()                                                 # The first to arrive now leaves
print(queue)
queue.popleft()                                                 # The second to arrive now leaves
print(queue)                                                    # Remaining queue in order of arrival

# List comprehension
# Concise way of creating lists
squares = [x**2 for x in range(10)]
print(squares)
listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]             # an expression followed by one or more for and if statements
print(listcomp)

# Nested list comprehension
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
tranposeMat = [[row[i] for row in matrix] for i in range(4)]
print(tranposeMat)

# The del statement
# A way to remove an item from a list given its index instead of its value
# Can also be used to remove slices from a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]                                    # delete element at index
print(a)
del a[2:4]                                  # delete slice
print(a)
del a[:]                                    # delete entire list
print(a)
del a                                       # delete variable
#print(a)                                   # error: var a can no longer be accessed

# Tuples and sequences
# A tuple consists of a number of values separated by commas
t = 12345, 54321, 'hello!'
print(t[0])
u = t, (1,2,3,4,5)
print(u)
# t[0] = 8888                               # error: tuple is immutable
empty = ()                                  # empty tuple
singleton = 'hello',                        # tuple with a single member
print(singleton)

# Tuple unpacking
j, k, l = t
print(j, k, l)
# Note: Sequence unpacking requires that there are as many variables on the left side of 
# the equals sign as there are elements in the sequence

# Sets
# Set is a unique collection
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

# Set operations
print(a - b)                                # letters in a but not in b
print(a | b)                                # letters in a or b or both
print(a & b)                                # letters in both a and b
print(a ^ b)                                # letters in a or b but not in both