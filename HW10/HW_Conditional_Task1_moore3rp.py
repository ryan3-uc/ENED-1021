# Activity Conditional: Task 1
# File: HW_Conditional_Task1_moore3rp.py 
# Date:    02 11 2026
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
# This script recieves a letter grade from the user and prints the equivalent grade points.
#
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

letter = input("Letter grade: ")

match letter:
    case "A": points = 4.0000
    case "A-": points = 3.6667
    case "B+": points = 3.3333
    case "B": points = 3.0000
    case "B-": points = 2.6667
    case "C+": points = 2.3333
    case "C": points = 2.0000
    case "C-": points = 1.6667
    case "D+": points = 1.3333
    case "D": points = 1.0000
    case "D-": points = 0.6667
    case _: points = 0.0000

print(f"{points:.4f}")