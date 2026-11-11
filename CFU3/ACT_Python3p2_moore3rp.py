# Activity Python 3: Task 2
# File: ACT_Python3p2_moore3rp.py 
# Date:    06 11 26
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
# This script plays a dice game.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

import random
rounds = int(input("Number of rounds: "))
p1_wins = p2_wins = 0

while rounds > 0:
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)
    if p1 < p2:
        p2_wins += 1
    elif p1 > p2:
        p1_wins += 1
    rounds -= 1

if p1_wins > p2_wins:
    print("Player 1 wins!")
elif p1_wins < p2_wins:
    print("Player 2 wins!")
else:
    print("It's a tie!")
