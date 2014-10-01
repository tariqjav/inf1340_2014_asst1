#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

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
    checksum = list(upc)
    #Put the string with 12 digits into a list. 
    
    # generate checksum using the first 11 digits provided
    a1 = checksum(1)+checksum(3)+checksum(5)+checksum(7)+checksum(9)+checksum(11)
    #1. Adding the odd number digits, and multiple by three.
    a2 = a1*3 + checksum(2)+checksum(4)+checksum(6)+checksum(8)+checksum(10)
    #2. Adding the even number digits.
    a3 = a2 % 10
    #3. Calcultating the modulo ten.
    result = 10 - a3
    #4. Subtrating by ten and generating the result.
    # check against the the twelfth digit
    if result == checksum(12):
           return True
    # return True if they are equal, False otherwise

    return False
