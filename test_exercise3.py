#!/usr/bin/env python3

import exercise3
from exercise3 import decide_result


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_result("rock", "paper") == 2
    assert decide_result("scissors", "scissors") == 0
    assert decide_result("rock", "scissors") == 1
    # other tests

