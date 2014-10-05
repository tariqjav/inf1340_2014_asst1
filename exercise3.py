#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock Paper Scissors Result

This module contains one function decide_result. Two players each choose Rock, Paper or Scissors.
Rock beats Scissors. Scissors beat Paper. Paper beats Rocks. Other results are tie.
The program returns 0 for tie, 1 if player 1 wins and 2 if player 2 wins.
Example:
    $ python exercise3.py
"""


def decide_result(key, key1):

    # assign parameters
    player1_options = "Rock", "Paper", "Scissors"
    player2_options = "Rock", "Paper", "Scissors"

    # check to see if parameter matches
    if key in player1_options:
        pass

    elif key != player1_options:
        print("Error")
        raise TypeError("Invalid type passed as parameter")

    if key1 in player2_options:
        pass

    elif key1 != player2_options:
        print("Error")
        raise TypeError("Invalid type passed as parameter")

    # create a dictionary
    decide_rps = {}

    # the results for all the possible situations from above are summarized in this dictionary

    decide_rps["Rock", "Rock"] = "0"
    decide_rps["Rock", "Paper"] = "2"
    decide_rps["Rock", "Scissors"] = "1"
    decide_rps["Paper", "Paper"] = "0"
    decide_rps["Paper", "Rock"] = "1"
    decide_rps["Paper", "Scissors"] = "2"
    decide_rps["Scissors", "Scissors"] = "0"
    decide_rps["Scissors", "Rock"] = "2"
    decide_rps["Scissors", "Paper"] = "1"

    for (key, key1), value in decide_rps.items():
        print((key, key1), value)


