"""
    Write a program to create a function that takes two arguments, name and age, and print
    their value.
"""
name = input("Enter your name: ")
age = input("Enter your age: ")

def info(name, age):
    print(f" Name = {name} \n Age = {age}")

info(name, age)