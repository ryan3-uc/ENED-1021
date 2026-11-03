# Activity Python 1: Task 1b
# File: ACT_Python1p1_moore3rp.py 
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

velocity = float(input("Fluid velocity in mi/hr: "))
length = float(input("Typical length in inches: "))
viscosity = float(input("Dynamic viscosity in lb/(in*s): "))
density = float(input("Density in lb/in³: "))

# These are conversion ratios easily found on the internet
velocity *= 0.44704
length *= 0.0254
viscosity *= 17.8579673
density *= 27679.9

re = (density*velocity*length)/viscosity
print(f"Reynold's number: {re:.2f}")