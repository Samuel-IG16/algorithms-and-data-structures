# Question 1
print("These are the numbers between 1500 and 2700 that are divisible 7 and a multiple of 5")
for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print (i)

# Question 2
for number in range (1,51):
    if number % 3 == 0 and number  % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

# Question 3

int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))
sum_of_integers =  int1 + int2
if sum_of_integers >= 15 and sum_of_integers <= 20:
    print("sum of integers = 20")
else:
    print(f"sum of integers = {sum_of_integers}")


# Question 4

color_list = ["Red","Green","White","Black","Pink","Yellow"]
color_list.pop(0)
color_list.pop(3)
color_list.pop(3)
print(color_list)


# Question 5
num = 1
while num < 100:
    if num % 2 != 0:
        print(num)
    num += 1

# Question 6

percentage = eval(input("Enter score percentage: "))
if percentage > 90:
    print("Grade = A")
elif percentage > 80 and percentage <= 90:
    print("Grade = B")
elif percentage >= 60 and percentage <= 80:
    print("Grade = C")
else:
    print("Grade = D")

# Question 7
day_number = int(input("Enter a number between 1- 7: "))
if day_number == 1:
    print("Sunday")
elif day_number == 2:
    print("Monday")
elif day_number == 3:
    print("Tuesday")
elif day_number == 4:
    print("Wednesday")
elif day_number == 5:
    print("Thursday")
elif day_number == 6:
    print("Friday")
elif day_number == 2:
    print("Saturday")
else:
    print("Invalid Input")

# Question 8
birthdays = {"Anita":"April 22","Hansel":"August 3"}
name = input("Enter name: ").title()
if name in birthdays:
    print(f"{birthdays[name]} is the birthday of {name}")
else:
    print(f"I do not have birthday information for {name}")


# Question 9

def info(name,age):
    print(f" Name = {name} \n Age = {age}")

name = input("Enter your name: ")
age = input("Enter your age: ")
info(name,age)


# Question 10
value1 = eval(input("Enter first number: "))
value2 = eval(input("Enter second number: "))
value3 = eval(input("Enter third number: "))

def maximum_number (value1,value2,value3):
    print(max(value1,value2,value3))

maximum_number(value1,value2,value3)

# Question 11
for number in range(1,61):
    if number % 3 == 0 and number % 4 == 0:
        print("Multiple of 3 and 4")
    elif number % 3 == 0:
        print("Multiple of 3")
    elif number % 4 == 0:
        print("Multiple of 4")
    else:
        print(number)




############### Python Input and Output Exercises ####################

# Question 1
city = input("What city did you grow up in? ")
pet_name_2 = input("What's your pet's name ")
band_name = city + pet_name_2
print(band_name)

# Question 2
fave_color = input("What's your favorite color: ")
birth_month = input("What month were you born in (The number): ")
pet_name = input("What's your pet's name: ")
password = fave_color + birth_month + pet_name
print(password)

# Question 3
name_2 = 'Tani'
phone_no = '0812345667'
print('Contact Info')
print("Name: "+name_2)
print("Number: "+str(phone_no))

# Question 4
name = 'Tanitolorun'
age = 20
print("My name is "+ name + " and I am "+str(age)+" years old.")