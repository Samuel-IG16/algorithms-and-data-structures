"""
    Write a program to accept percentage from the user and display the grade according to
    the following criteria:
    Marks Grade
    > 90 A
    > 80 and <= 90 B
    >= 60 and <= 80 C
    below 60 D
"""
try:
    percentage = eval(input("Enter score percentage: "))
    if (percentage > 100 or percentage < 0):
        print("Percentage must be between 0 and 100")
    else:
        print("Grade: ", end="")
        if percentage > 90:
            print("A")
        elif percentage > 80 and percentage <= 90:
            print("B")
        elif percentage >= 60 and percentage <= 80:
            print("C")
        else:
            print("D")
except:
    print("Invalid input")

