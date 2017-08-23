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
string = raw_input("Input a string to tokenize")

def tokenize(string):
    while True:
        token = string.split(" ")
        command = token[0]
        num1 = token[1]
        num2 = token[2]
        num3 = token[3]
        if command == "q":
            break
        elif command == "add":
            add(num1, num2)
        elif command == "subtract":
            subtract(num1, num2)
        elif command == "multiply":
            multiply(num1, num2)
        elif command == "divide":
            divide(num1, num2)
        elif command == "square":
            square(num1)
        elif command == "cube":
            cube(num1)
        elif command == "power":
            power(num1, num2)
        elif command == "mod":
            mod(num1, num2)
        elif command == "add_mult":
            add_mult(num1, num2, num3)
        elif command == "add_cubes":
            add_cubes(num1, num2)

# def add(num1, num2):
#     """Return the sum of the two input integers."""

#     return num1 + num2


# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""

#     return num1 - num2

# def multiply(num1, num2):
#     """Multiply the two inputs together."""
#     return num1 * num2

# def divide(num1, num2):
#     """Divide the first input by the second, returning a floating point."""
#     return float(num1) / float(num2)

# def square(num1):
#     """Return the square of the input."""
#     return num1 * num1

# def cube(num1):
#     """Return the cube of the input."""
#     return num1 * num1 * num1

# def power(num1, num2):
#     """Raise num1 to the power of num2 and return the value."""
#     return num1 ** num2


# def mod(num1, num2):
#     """Return the remainder of num1 / num2."""
#     return num1%num2

# def add_mult(num1, num2, num3):
#     """return num1 and num2 added and multiply by num3"""
#     return (num1 + num2) * num3

# def add_cubes(num1, num2):


