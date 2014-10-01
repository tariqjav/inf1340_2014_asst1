#!/usr/bin/env python3


""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.
    Testing
    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    # assign the two types of parameters, integer or string

    letter_grade = "A+", "A", "A-", "B+", "B", "B-", "FZ"

    mark_to_letter= list(range(0, 101))

    if type(grade) is str:

      # check to see if the parameter matches

        if grade in letter_grade:
            pass


        # assign grade to letter_grade

        if grade == "A+":
             gpa = 4.0

        elif grade == "A":
            gpa = 4.0

        elif grade == "A-":
            gpa = 3.7

        elif grade == "B+":
            gpa = 3.3

        elif grade == "B":
            gpa = 3.0

        elif grade == "B-":
            gpa = 2.7

        elif grade == "FZ":
            gpa = 0.0

    elif type(grade) is int:

        #check to see if the parameter matches

        if grade in mark_to_letter:
            pass

        # convert the numeric grade to a letter grade

        if grade in list(range (90, 101)):
            grade = "A+"

        elif grade in list(range (85, 90)):
            grade = "A"

        elif grade in list(range (80, 85)):
            grade = "A-"

        elif grade in list(range (77, 80)):
            grade = "B+"

        elif grade in list(range (73, 77)):
            grade = "B"

        elif grade in list(range (70, 73)):
            grade = "B-"

        elif grade in list(range (0, 70)):
            grade = "FZ"

        # assign the value to letter_grade

        if grade == "A+":
             gpa = 4.0

        elif grade == "A":
            gpa = 4.0

        elif grade == "A-":
            gpa = 3.7

        elif grade == "B+":
            gpa = 3.3

        elif grade == "B":
            gpa = 3.0

        elif grade == "B-":
            gpa = 2.7

        elif grade == "FZ":
            gpa = 0.0
    else:
        # raise a TypeError exception
        print ("Error")
        raise TypeError("Invalid type passed as parameter")
    # assign the value to gpa
    return gpa

print(grade_to_gpa(5))
