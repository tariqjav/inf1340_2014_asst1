#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock Paper Scissors Result

This module contains one function decide_result. Two players each choose Rock, Paper or Scissors.
Rock beats Scissors. Scissors beat Paper. Paper beats Rocks. Other results are tie.
The program returns 0 for tie, 1 if player 1 wins and 2 if player 2 wins.
Example:
    $ python exercise3.py
"""


def decide_result(player1, player2):

    # assign parameters
    player1_options = "Rock", "Paper", "Scissors"
    player2_options = "Rock", "Paper", "Scissors"

    # check to see if parameter matches
    if player1 in player1_options:
        pass

    elif player1 != player1_options:
        print("Error")
        raise TypeError("Invalid type passed as parameter")

    if player2 in player2_options:
        pass

    elif player2 != player2_options:
        print("Error")
        raise TypeError("Invalid type passed as parameter")

    # all the possible situations when two players choose between rock, paper, scissors
    decide_rps = {}
    p_one = ("Rock", "Rock")
    p_two = ("Rock", "Paper")
    p_three = ("Rock", "Scissors")
    p_four = ("Paper", "Paper")
    p_five = ("Paper", "Rock")
    p_six = ("Paper", "Scissors")
    p_seven = ("Scissors", "Scissors")
    p_eight = ("Scissors", "Rock")
    p_nine = ("Scissors", "Paper")

    # the results for all the possible situations from above are summarized in this dictionary

    decide_rps[p_one] = "0"
    decide_rps[p_two] = "2"
    decide_rps[p_three] = "1"
    decide_rps[p_four] = "0"
    decide_rps[p_five] = "1"
    decide_rps[p_six] = "2"
    decide_rps[p_seven] = "0"
    decide_rps[p_eight] = "2"
    decide_rps[p_nine] = "1"

    for player1, player2 in decide_rps.items():
        print (player1, player2)


print(decide_result("Paper","Paper"))
