"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two input integers."""

    return int(num1) + int(num2)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return int(num1) - int(num2)

def multiply(num1, num2):
    """Multiply the two inputs together."""
    return int(num1) * int(num2)

def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
    return float(num1) / float(num2)

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

def add_mult(num1, num2, num3):
    """return num1 and num2 added and multiply by num3"""
    return (int(num1) + int(num2)) * int(num3)

def add_cubes(num1, num2):
    """Cube both numbers and sum them"""
    return int(num1) **3 + int(num2)**3


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