#!/usr/bin/env python3

import exercise3
from exercise3 import decide_result


def test_result():
    """
    Inputs that are the correct format and length
    """
    assert decide_result("rock", "paper") == 2
    assert decide_result("scissors", "scissors") == 0
    assert decide_result("rock", "rock") == 0
    assert decide_result("rock", "scissors") == 1
    assert decide_result("paper", "paper") == 0
    assert decide_result("paper", "rock") == 1
    assert decide_result("paper", "scissors") == 1
    assert decide_result("scissors", "rock") == 2
    assert decide_result("scissors", "paper") == 1


