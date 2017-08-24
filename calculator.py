"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def my_reduce(command, token):
    if command == "q":
        quit()
    elif command == "+":
        return add(token)
    elif command == "-":
        return subtract(token)
    elif command == "*":
        return multiply(token)
    elif command == "/":
        return divide(token)
    elif command == "square":
        return square(token)
    elif command == "cube":
        return cube(token)
    elif command == "pow":
        return power(token)
    else:
        return "Give me a command and at least one number, you fool!"

def tokenize(string):
    test = string.split(" ")
    token = []
    for item in test[1:]:
        if item.isdigit():
            token.append(float(item))
        else:
            break
    if len(token) < 1:
        print "Give me a command and at least one number, you fool!"
    command = test[0]
    print token
    output = (my_reduce(command, token))
    # print "output: ", output
    print "{0:.2f}".format(output)

while True:
    string = raw_input("Input a string to tokenize ")
    tokenize(string)


     # if command == "q":
    #     quit()
    # elif command == "+":
    #     print my_reduce(lambda sum, next_number: sum+next_number, token)
    # elif command == "-":
    #     print my_reduce(lambda difference, next_number: difference-next_number, token)
    # elif command == "*":
    #     print my_reduce(lambda product, next_number: product*next_number, token)
    # elif command == "/":
    #     print my_reduce(lambda quotient, next_number: quotient/next_number, token)
    # elif command == "square":
    #     print square(token)
    # elif command == "cube":
    #     print cube(token)
    # elif command == "pow":
    #     print my_reduce(lambda pow, next_number: pow**next_number, token)