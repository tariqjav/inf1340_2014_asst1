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


def checksum(upc):
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
        raise ValueError("Length is not 12")

    # convert the string with 12 digits into a list and then into integers
    c_upc = list(upc)

    # generate checksum using the first 11 digits provided
    #1. Adding the odd number digits & multiplying by three
    step_one = ((int(c_upc[0]) + int(c_upc[2]) + int(c_upc[4]) + int(c_upc[6]) + int(c_upc [8]) + int(c_upc[10]))*3
    #2. Adding the even number digits
    step_two = step_one + int(c_upc[1])+int(c_upc[3])+int(c_upc[5])+int(c_upc[7])+int(c_upc[9])
    #3. The result modulo 10
    step_three = step_two % 10
    #4. If result is not 0, subtract from 10

    checksum = 10 - step_three


    # check against the the twelfth digit
    if checksum == c_upc[11]:
           return True
    # return True if they are equal, False otherwise

    elif checksum != c_upc[11]:
        return False


print(checksum("786936224306"))
