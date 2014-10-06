#!/usr/bin/env python3

import exercise3
from exercise3 import decide_result


def test_result():
    """
    Inputs that are the correct format and length
    """
    assert decide_result("Rock", "Paper") == 2
    assert decide_result("Scissors", "Scissors") == 0
    assert decide_result("Rock", "Rock") == 0
    assert decide_result("Rock", "Scissors") == 1
    assert decide_result("Paper", "Paper") == 0
    assert decide_result("Paper", "Rock") == 1
    assert decide_result("Paper", "Scissors") == 1
    assert decide_result("Scissors", "Rock") == 2
    assert decide_result("Scissors", "Paper") == 1


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with exercise3.raises(TypeError):
        decide_result(1,3)
        decide_result("orange", "black")
        decide_result("Hello", 241)
        decide_result(444444)
        decide_result("This_is_wrong")