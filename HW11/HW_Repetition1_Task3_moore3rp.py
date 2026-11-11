# Activity Repetition 1: Task 3
# File: HW_Repetition1_Task3_moore3rp.py 
# Date:    09 11 2026
# By:      Ryan Moore
# Section: 20
# 
# ELECTRONIC SIGNATURE
# Ryan Moore
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This script plays blackjack vs a player's inputted score and determines the winner.
#
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

from random import randint

def draw_card():
    val = randint(1, 14)
    if val > 11:
        val = 10
    return val

p = int(input("Player score: "))
d = 0
for i in range(2):
    d += draw_card()

while d < 17:
    d += draw_card()

if d > 21:
    print("Dealer busts, Player wins!")
    print(f"Player: {p} | Dealer: {d}")
elif d < p:
    print("Player wins!")
    print(f"Player: {p} | Dealer: {d}")
else:
    print("Dealer wins!")
    print(f"Player: {p} | Dealer: {d}")