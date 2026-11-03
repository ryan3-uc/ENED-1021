# Activity Sequential: Task 3c
# File: HW_Sequential_Task3c_moore3rp.py 
# Date:    28 10 2026
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
# This script recieves velocity, length, and altitude of an object from the user, then it calculates and prints the Reynold's Number. 
#
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

# Inputs
v = float(input("Enter velocity (ft/s): "))
l = float(input("Enter length (ft): "))
h = float(input("Enter altitude (ft): "))

# Calculate Re
temp = 59 - 0.00356*h
pressure = 2116*((temp + 459.7) / 518.6)**5.256
density = pressure / (1718*(temp + 459.7))
temp = (temp - 32)*5/9 + 273.15
tempSL = 288.15
viscSL = 0.0000003737
viscDyn = ((110 + tempSL) / (110 + temp)) * viscSL * (temp / tempSL)**1.5
re = (density*v*l) / viscDyn

# Print
print(f"Reynold's number: {re:.3f}")