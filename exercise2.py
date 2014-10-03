#!/usr/bin/env python3

"""
    Perform a checksum on a UPC
    This program will accept a string and check if it is a Universal Product Code (UPC) by turing it into a list
    and using the definition function of UPC. 

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string
    if type(upc) is not str:
        print("Type error")
        raise TypeError("Invalid input as parameter")

    # check length of string
    # raise ValueError if not 12
    if len(upc) is not 12:
        print("Length error")
        raise ValueError("Length is 12")

    # convert string to array
    # hint: use the list function
     upc = map(int,upc)
    #Put the string with 12 digits into a list. 
    
    # generate checksum using the first 11 digits provided
    a1 = upc[0]+upc[2]+upc[4]+upc[6]+upc[8]+upc[10]
    #1. Adding the odd number digits, and multiple by three.
    a2 = a1*3 + upc[1]+upc[3]+upc[5]+upc[7]+upc[9]
    #2. Adding the even number digits.
    a3 = a2 % 10
    #3. Calcultating the modulo ten.
    result = 10 - a3
    #4. Subtrating by ten and generating the result.
    # check against the the twelfth digit
    if result == upc[11]:
           return True
    # return True if they are equal, False otherwise

    return False

print checksum("786936224306")
