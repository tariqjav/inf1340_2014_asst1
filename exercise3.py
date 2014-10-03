#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock Paper Scissors Result

This module contains one function decide_result. Two players each choose Rock, Paper or Scissors.
Rock beats Scissors. Scissors beat Paper. Paper beats Rocks. Other results are tie.
The program returns 0 for tie, 1 if player 1 wins and 2 if player 2 wins.
Example:
    $ python exercise3.py
"""

__author__ = Javeria Tariq
__email__ = javeria.tariq@mail.utoronto.ca


def decide_result(player1, player2):

    # assign parameters
    player1_options = "Rock", "Paper", "Scissors"
    player2_options = "Rock", "Paper", "Scissors"

    # check to see if parameter matches
     if player1 in player1_options:
         pass

    if player2 in player2_options:
        pass


    # all the possible situations when two players choose between rock, paper, scissors
    P_one = (Rock, Rock)
    P_two = (Rock, Paper)
    P_three = (Rock, Scissors)
    P_four = (Paper, Paper)
    P_five = (Paper, Rock)
    P_six = (Paper, Scissors)
    P_seven = (Scissors, Scissors)
    P_eight = (Scissors, Rock)
    P_nine = (Scissors, Paper)

    # the results for all the possible situations from above are summarized in this dictionary

    Results = {P_one: 0, P_two: 2, P_three: 1, P_four: 0, P_five: 1, P_six: 2, P_seven: 0, P_eight: 2, P_nine: 1}



    return Results

