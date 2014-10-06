#!/usr/bin/env python3

""" Module to test exercise1.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

import exercise1

from exercise1 import grade_to_gpa


# tests for valid values
def test_letter_grade():
    """
    Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 4.0
    assert grade_to_gpa("B+") == 4.0
    assert grade_to_gpa("B") == 4.0
    assert grade_to_gpa("B-") == 4.0
    assert grade_to_gpa("FZ") == 4.0

    # tests for invalid values
    with exercise1.raises(ValueError):
        grade_to_gpa("q")
        grade_to_gpa("E")
        grade_to_gpa("BP")
        grade_to_gpa("z")


def test_percentage_grade():
    """
    Numeric grade inputs
    """
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    # test for invalid values
    with exercise1.raises(ValueError):
        grade_to_gpa(101)
        grade_to_gpa(-1)
        grade_to_gpa(-50)
        grade_to_gpa(120)


# tests for float inputs that are invalid
def test_float_input():
    """
    Float inputs
    """
    with exercise1.raises(TypeError):
        grade_to_gpa(82.5)

    with exercise1.raises(TypeError):
        grade_to_gpa(-30.07)

    with exercise1.raises(TypeError):
        grade_to_gpa(50600)


# tests for string inputs that are invalid
def test_string_input():
    """
    String inputs
    """
    with exercise1.raises(ValueError):
        grade_to_gpa("Sentences")

    with exercise1.raises(ValueError):
        grade_to_gpa("This is")

    with exercise1.raises(ValueError):
        grade_to_gpa("Invalid")

