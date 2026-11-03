# Activity Python 2: Task 1
# File: ACT_Python2p1_moore3rp.py 
# Date:    30 10 2026
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
# This script recieves an input from the user (pH), and determines/prints if it is acidic, basic, neutral, or invalid.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

pH = float(input("Input pH (0 - 14): "))

if 0 <= pH and pH < 7:
    print("Acidic")
elif pH == 7:
    print("Neutral")
elif 7 < pH <= 14:
    print("Basic")
else:
    print("Invalid")
