# 1.write a program to create a new string made of an input string's first, middle and last character

# def create_new_string(input_string):
#     if len(input_string) == 0:
#         print("Please enter a string")
#         new_input = input("Enter a string: ")
#         create_new_string(new_input)
#     else:
#         first_character = input_string[0]
#         middle_character = input_string[int(len(str1) / 2)]
#         result = first_character+middle_character
#         last_character = input_string[-1]
#         result = result+last_character
#         print(result)
# str1 = input("Enter a string:")
# create_new_string(str1)

#2.Write a program to create a new string made of the middle three characters of an input string

# def middle_three_characters(string1):
#     middle_letter_index = int(len(string1)/2)
#     print(middle_letter_index)
#     new_string =  string1[middle_letter_index - 1:middle_letter_index+2]
#     print(new_string)
# string1 = input("Enter a string:")
# middle_three_characters(string1)

#3.Append new string in the middle of a given string

def append_string(str1, str2):
    middle_index = int(len(str1)/2)
    result = str1[0:middle_index]+str2+str1[middle_index:]
    return result
str1 = input("Enter string:")
str2 = input("Enter another string:")
result = append_string(str1, str2)
print(result)

#4..
