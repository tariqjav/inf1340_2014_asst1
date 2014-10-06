#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"


import exercise2
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum ("435804790143") is False
    assert checksum ("823911165203") is False
    assert checksum ("314439932290") is False
    assert checksum ("590467329014") is False
    assert checksum ("671298457041") is False
    assert checksum ("474365717905") is False
    assert checksum ("172346155116") is True


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with exercise2.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)
        checksum(444444)

    with exercise2.raises(ValueError):
        checksum("1")
        checksum("1234567890")
        checksum("142323")
        checksum("42412421341329324")



