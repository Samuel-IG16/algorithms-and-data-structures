############### Python Input and Output Exercises ####################

def input_and_output_exercises():
    try:
        # Question 1
        print("Band Name Generator")
        city = input("What city did you grow up in? ")
        pet_name = input("What's your pet's name? ")
        band_name = "Your band name could be " + city + pet_name
        print(band_name + '\n')

        # Question 2
        print("Password Generator")
        fave_color = input("What's your favorite color: ")
        birth_month = input("What month were you born in (The number): ")
        pet_name_2 = input("What's your pet's name: ")
        password = fave_color + birth_month + pet_name_2
        print("password: " + password + '\n')

        # Question 3
        print("Contact Info")
        name_2 = input("What's your name: ")
        phone_no = input("What is your number: ")
        print('\n' + 'Contact Info')
        print("Name: " + name_2)
        print("Number: " + phone_no + '\n')

        # Question 4
        print("Tell me about yourself")
        name = input("What's your name: ")
        age = int(input("What's your age: "))
        print("My name is "+ name + " and I am "+str(age)+" years old." + '\n')
    except:
        print("invalid input")

if __name__ == "__main__":
    input_and_output_exercises()