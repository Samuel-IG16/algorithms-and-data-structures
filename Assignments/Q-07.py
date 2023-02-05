"""
    Write a program to accept a number from 1 to 7 and display the name of the day like 1
    for Sunday , 2 for Monday and so on.
"""
try:    
    day_number = int(input("Enter a number between 1 and 7: "))
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    print(days[day_number])
except:
    print("Invalid Input")