"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# # No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token
# string = raw_input("Input a string to tokenize")

def tokenize(string):
    token = string.split(" ")
    print token
    command = token[0]
    num1 = token[1]
    num2 = token[2]
    if command == "q":
        quit()
    elif command == "+":
        print add(num1, num2)
    elif command == "-":
        print subtract(num1, num2)
    elif command == "*":
        print multiply(num1, num2)
    elif command == "/":
        print divide(num1, num2)
    elif command == "square":
        print square(num1)
    elif command == "cube":
        print cube(num1)
    elif command == "pow":
        print power(num1, num2)
    elif command == "mod":
        print mod(num1, num2)

while True:
    string = raw_input("Input a string to tokenize")
    tokenize(string)