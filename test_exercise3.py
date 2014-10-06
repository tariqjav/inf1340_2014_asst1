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
    assert decide_result("Paper", "paper") == 0
    assert decide_result("paper", "rock") == 1
    assert decide_result("paper", "scissors") == 1
    assert decide_result("scissors", "rock") == 2
    assert decide_result("scissors", "paper") == 1


