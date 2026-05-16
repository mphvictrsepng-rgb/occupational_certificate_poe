# 1.1 Function to return the sum of positive numbers

def sum_positive(numbers):                     # This function takes a list of numbers and returns the sum of all positive numbers in the list
    total = 0                                 # I started the value in this variable as 0 because adding 0 does not change the sum.

    for num in numbers:
        if num > 0:
            total += num

    return total


#Example
print(sum_positive([3, -2, 5, -1, 4]))


# 1.2 Function to return the product of all numbers

def multiply_numbers(numbers):                  # This function takes a list of numbers and returns the product of all the numbers in the list
    product = 1                                 # I started with 1 because multiplying by 1 does not change the product

    for num in numbers:
        product *= num

    return product


# Example
print(multiply_numbers([2, 3, 4]))


# 1.3 Function to calculate the circumference of a circle

import math                           # This line imports the math module, which provides access to mathematical functions and constants, including the pi


def circumference(radius):          # This function takes the radius of a circle as input and returns the circumference of the circle using the formula C = 2 * pi * r
    return 2 * math.pi * radius


# Example
print(circumference(7))


# 1.4 Function to calculate the height of a triangle

def triangle_height(area, base):       # This function takes the area and base of a triangle as input and returns the height of the triangle using the formula A = (1/2) * b * h, which can be rearranged to h = (2 * A) / b
    return (2 * area) / base


# e.g
print(triangle_height(20, 5))
