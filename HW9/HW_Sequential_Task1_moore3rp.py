# Activity Sequential: Task 1
# File: HW_Sequential_Task1_moore3rp.py 
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
# This script recieves the credit hours and grade points of 5 courses from the user, calculates, and prints the weighted GPA. 
#
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

# Get inputs
g1 = float(input("Grade points for course 1: "))
c1 = float(input("Credit hours for course 1: "))

g2 = float(input("Grade points for course 2: "))
c2 = float(input("Credit hours for course 2: "))

g3 = float(input("Grade points for course 3: "))
c3 = float(input("Credit hours for course 3: "))

g4 = float(input("Grade points for course 4: "))
c4 = float(input("Credit hours for course 4: "))

g5 = float(input("Grade points for course 5: "))
c5 = float(input("Credit hours for course 5: "))

# Calculate
x = g1*c1 + g2*c2 + g3*c3 + g4*c4 + g5*c5
y = c1 + c2 + c3 + c4 + c5
gpa = x/y

# Output
print(f"Your GPA is: {gpa:.2f}")