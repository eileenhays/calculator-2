"""Math functions for calculator."""


def add(input_list):
    """Return the sum of the two input integers."""
    sum = 0
    for number in input_list:
        if type(number) == int:
            sum = sum + number
    return sum

def subtract(input_list):
    """Return the second number subtracted from the first."""

    difference = 0
    for number in input_list:
        if type(number) == int:
            difference = difference - number
    return difference

def multiply(input_list):
    """Multiply the two inputs together."""
    product = 0
    for number in input_list:
        if type(number) == int:
            product = product * number
    return product


def divide(input_list):
    """Divide the first input by the second, returning a floating point."""
    quotient = input_list[0]
    for number in input_list[1:-1]:
        if type(number) == int:
            quotient = quotient / number
    return quotient

def square(num1):
    """Return the square of the input."""
    return int(num1) * int(num1)

def cube(num1):
    """Return the cube of the input."""
    return int(num1) * int(num1) * int(num1)

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return int(num1) ** int(num2)


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return int(num1)% int(num2)


# num1 = 10
# num2 = 3
# num3 = 2
# print add(num1, num2)
# print subtract(num1, num2)
# print multiply(num1, num2)
# print divide(num1, num2)
# print square(num1)
# print cube(num1)
# print power(num1, num2)
# print mod(num1, num2)
# print add_mult(num1, num2, num3)
# print add_cubes(num1, num2)