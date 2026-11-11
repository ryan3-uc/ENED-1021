# Activity Python 3: Task 3
# File: ACT_Python3p3_moore3rp.py 
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
# This script plays a dice game until a certain number of points.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

import random
score = int(input("Max score: "))
p1_score = p2_score = 0

while p1_score < score and p2_score < score:
    p1_score += random.randint(1, 6)
    p2_score += random.randint(1, 6)

if p1_score > score and p2_score > score:
    print("It's a tie!")
elif p1_score < score:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")
