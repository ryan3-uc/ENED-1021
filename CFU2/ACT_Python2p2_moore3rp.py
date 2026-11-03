# Activity Python 2: Task 2
# File: ACT_Python2p2_moore3rp.py 
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
# This script recieves two inputs from the user (t and p), and determines/prints the state of a reactor.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

t = float(input("Temperature (C): "))
p = float(input("Pressure (atm): "))

if t > 355 and p > 0.100:
    print("Melt Down")
elif 345 < t and t <= 355 and 0.095 < p and p <= 0.1:
    print("Very Severe")
elif 335 < t and t <= 345 and 0.09 < p and p <= 0.095:
    print("Severe")
elif 325 < t and t <= 335 and 0.085 < p and p <= 0.09:
    print("Moderate")
else:
    print("Normal")