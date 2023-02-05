"""
    Write a Python program to find the sum of two given integers. However, if the sum is
    between 15 and 20 it will return 20
"""
def Q3(a, b):
    sum = a + b
    if sum >= 15 and sum <= 20:
        return 20
    else:
        return sum

if __name__ == "__main__":
    try:    
        print("sum:", Q3(int(input("integer a: ")), int(input("integer b: "))))
    except ValueError:
        print("Integers only")
