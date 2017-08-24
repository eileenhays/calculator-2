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
    test = string.split(" ")
    token = []
    for item in test[1:]:
        if item.isdigit():
            token.append(int(item))
        else:
            break
    if len(token) < 1:
        print "Give me a command and at least one number, you fool!"
    command = test[0]
    print token
    if command == "q":
        quit()
    elif command == "+":
        print reduce(lambda sum, next_number: sum+next_number, token)
    elif command == "-":
        print reduce(lambda difference, next_number: difference-next_number, token)
    elif command == "*":
        print reduce(lambda product, next_number: product*next_number, token)
    elif command == "/":
        print reduce(lambda quotient, next_number: quotient/next_number, token)
    elif command == "square":
        print square(token)
    elif command == "cube":
        print cube(token)
    elif command == "pow":
        print reduce(lambda pow, next_number: pow**next_number, token)
    else:
        print "Give me a command and at least one number, you fool!"

while True:
    string = raw_input("Input a string to tokenize ")
    tokenize(string)