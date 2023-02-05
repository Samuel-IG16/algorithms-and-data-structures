"""
    Write a Python program to print a specified list after removing the 0th, 4th and 5th
    elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Expected Output : ['Green', 'White', 'Black']
"""
def Q4(sample_list):
    print(sample_list)
    sample_list.pop(5)    
    sample_list.pop(4)
    sample_list.pop(0)
    print(sample_list)

if __name__ == "__main__":
    try:    
        list_length = int(input("Length of list: "))
        if (list_length < 6):
            print("List must be greater than 5")
        else:
            i = 0
            item_list = []
            while i < list_length:
                item_list.append(input(f"item {i}: "))
                i += 1
            Q4(item_list)
    except ValueError:
        print("Integers only")
