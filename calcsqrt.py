#! /usr/bin/env python3

# Cuan O Conchuir
# Python newton root
# Calculate the square root of a number

#Python uses indentation for code structure and hierarchy
#Everything at the unindented level will be run

def sqrt(x):
    """
    Calculate the square root of argument x
    """
    
    # Check that x is positive
    if x < 0:
        print("Error: Negative value supplied")
        return -1
    else:
        print("Here we go...")

    # initial guess for the square root
    z = x/2.0

    # Continuously improve the guess.
    # Adapted from https://tour.golang.org/flowcontrol/8
    # Comparing to 0 is not a good idea
    # abs will always give you back positive value
    # will loop as long as the difference between x and z is > 0.01

    while abs(x - (z * z)) > 0.000001:
        z = z - ((z * z) -x) / (2 * z)
    
    # z is actual square root
    return z

myval = 63.0
print("The square root of ", myval, "is", sqrt(myval))


