#!/usr/bin/python3
import sys

# Function Description: This function calculates the factorial of a given number using recursion.
# Parameters: The function takes one parameter 'n', which is the number for which we want to calculate the factorial.
# Return: The function returns the factorial of the number 'n'.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))


print(f)