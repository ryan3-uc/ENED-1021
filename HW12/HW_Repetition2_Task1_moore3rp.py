# Activity Repetition 2: Task 1
# File: HW_Repetition2_Task1_moore3rp.py 
# Date:    16 11 2026
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
# This script recieves the total number of courses and each course's grade and credit hours, then it prints the calculated GPA.

num_courses = int(input("Number of courses: "))
count = 0
grade_points = 0
credits = 0

for i in range(num_courses):
    print(f"Course {i+1}")
    letter = input("Letter grade: ")
    hours = float(input("Credit hours: "))

    # Match-case is better practice here
    if letter == "A": points = 4.0000
    elif letter == "A-": points = 3.6667
    elif letter == "B+": points = 3.3333
    elif letter == "B": points = 3.0000
    elif letter == "B-": points = 2.6667
    elif letter == "C+": points = 2.3333
    elif letter == "C": points = 2.0000
    elif letter == "C-": points = 1.6667
    elif letter == "D+": points = 1.3333
    elif letter == "D": points = 1.0000
    elif letter == "D-": points = 0.6667
    else: points = 0.0000

    grade_points += points * hours
    credits += hours
    count += 1

gpa = grade_points / credits

print(f"GPA is: {gpa:.2f}")