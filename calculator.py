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
        print add(token)
    elif command == "-":
        print subtract(token)
    elif command == "*":
        print multiply(token)
    elif command == "/":
        print divide(token)
    elif command == "square":
        print square(token)
    elif command == "cube":
        print cube(token)
    elif command == "pow":
        print power(token)
    else:
        print "Give me a command and at least one number, you fool!"

while True:
    string = raw_input("Input a string to tokenize ")
    tokenize(string)

    # '3 + 1'
    # test = ["3","+","1"]
    # token = [+, 1]