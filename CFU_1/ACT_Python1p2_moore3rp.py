# Activity Python 1: Task 2b
# File: ACT_Python1p2_moore3rp.py 
# Date:    23 10 2026
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
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

spl = float(input("Maximum allowable SPL in dB: "))
pRef = float(input("Reference pressure in Pa: "))
v = float(input("Particle velocity in m/s: "))

intensity = pRef*v*(10**(spl/20))
print(f"Maximum sound intensity: {intensity:.2f}")