#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock Paper Scissors Result

This module contains one function decide_result. Two players each choose Rock, Paper or Scissors.
Rock beats Scissors. Scissors beat Paper. Paper beats Rocks. Other results are tie.
The program returns 0 for tie, 1 if player 1 wins and 2 if player 2 wins.
Example:
    $ python exercise3.py
"""

__author__ = 'Javeria Tariq'
__email__ = "javeria.tariq@mail.utoronto.ca"


def decide_result(player1, player2):

    # assign parameters
    player1_options = 'rock', 'paper', 'scissors'
    player2_options = 'rock', 'paper', 'scissors'

    # check to see if parameter matches
    if player1 in player1_options:
        pass

    if player2 in player2_options:
        pass

    # all the possible options when two players choose between rock, paper, scissors

    p_one = ("rock", "rock")
    p_two = ("rock", "paper")
    p_three = ("rock", "scissors")
    p_four = ("paper", "paper")
    p_five = ("paper", "rock")
    p_six = ("paper", "scissors")
    p_seven = ("scissors", "scissors")
    p_eight = ("scissors", "rock")
    p_nine = ("scissors", "paper")

    # the results for all the possible situations from above are in this dictionary
    results = {}

    results[p_one] = 0
    results[p_two] = 2
    results[p_three] = 1
    results[p_four] = 0
    results[p_five] = 1
    results[p_six] = 2
    results[p_seven] = 0
    results[p_eight] = 2
    results[p_nine] = 1


    return results.values()


print (decide_result("rock","paper"))

