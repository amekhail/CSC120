"""
    File: strings_and_input.py
    Author: Adam Mekhail
    Purpose: 
"""
txt = input("input string: ") # prompts the user to input a string 

print(str(len(txt))) # prints the length of the string. str() is used since len() returns type int

print(txt[1]) # prints the second element in the string


print(txt[0:9]) # prints the first 10 elements in the string. if there are less that 10 characters, it will print the entire string

print(txt[-5:]) # prints the last 5 characters in the string

# prints the string in both lower case and upper case using the .lower() and .upper() functions
print(txt.lower())
print(txt.upper())

if txt[0].upper() == "Q" or txt[0].upper() == "W" or txt[0].upper() == "E" or txt[0].upper() == "R" or txt[0].upper() == "T" or txt[0].upper() == "Y":
    print("QWERTY") # print QWERTY if the first element is any letter in QWERTY
elif txt[0] == "U" or txt[0].upper() == "I" or txt[0].upper() == "O" or txt[0].upper() == "P":
    print("UIOP") # print UIOP if the first element is any letter in UIOP
elif txt[0].isalpha():
    print("LETTER") # if the first element is not a letter in QWERTY or UIOP, but isalpha() returns true, print "LETTER"
elif txt[0].isdigit():
    print("DIGIT")  # if the first element is a digit, print "DIGIT"
else:
    print("OTHER")

num1 = input()
num2 = input()

print(str(int(num1) * int(num2))) # print the product of 2 numbers entered by the user