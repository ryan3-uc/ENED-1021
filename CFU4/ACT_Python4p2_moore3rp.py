# Activity Python 4: Task 2
# File: ACT_Python4p2_moore3rp.py 
# Date:    13 11 26
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
# This script flips a coin a given amount of times and then calculates/outputs the percentage of heads and tails.

from random import randint

num_flips = int(input("Number of coin flips: "))
heads = tails = 0.0

for i in range(num_flips):
    flip = randint(0, 1)
    if flip:
        heads += 1
    else:
        tails += 1

p_heads = 100 * heads / num_flips
p_tails = 100 * tails / num_flips

print(f"{p_heads:.2f}% Heads | {p_tails:.2f}% Tails")

