"""
        Write a python code that loops from 1 to 60 with the following specifications:
        a. It prints “Multiple of 3” when the loop variable is a multiple of 3
        b. It prints “Multiple of 4” when the loop variable is a multiple of 4
        c. It prints “Multiple of 3 and 4” when the loop variable is a multiple of
        d. both 3 and 4
        e. Otherwise, it prints the loop variable
    """    
for number in range(1, 61):
    if number % 3 == 0 and number % 4 == 0:
        print("Multiple of 3 and 4", end=", ")
    elif number % 3 == 0:
        print("Multiple of 3", end=", ")
    elif number % 4 == 0:
        print("Multiple of 4", end=", ")
    else:
        print(number, end=", ")