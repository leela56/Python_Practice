# 1.write a program to create a new string made of an input string's first, middle and last character

def create_new_string(input_string):
    if len(input_string) == 0:
        print("Please enter a string")
        new_input = input("Enter a string: ")
        create_new_string(new_input)
    else:
        first_character = input_string[0]
        middle_character = input_string[int(len(str1) / 2)]
        result = first_character+middle_character
        last_character = input_string[-1]
        result = result+last_character
        print(result)
str1 = input("Enter a string:")
create_new_string(str1)
#2..