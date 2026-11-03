# Activity Conditional: Task 3
# File: HW_Conditional_Task3_moore3rp.py 
# Date:    03 11 2026
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
# This script revieves biological info and machine type from the user and then prints their calories burned and activity level.
#
# This script is a header template that will be used for 
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

machine = input("Enter machine type (manual/auto): ")
weight = float(input("Enter weight (lbs): "))
age = float(input("Enter age (years): "))
chr = float(input("Enter current heartrate (bpm): "))

if machine.lower() == "manual":
    mhr = 206 - 0.88*age
    cal = 60 * (age*0.074 - weight*0.05741 + chr*0.4472 - 20.4022) / 4.184
else:
    mhr = 205.8 - 0.685*age
    cal = 60 * (age*0.2017 + weight*0.09036 + chr*0.6309 - 55.0969) / 4.184

level = chr / mhr
if level < 0.6:
    level = "Below Level"
elif 0.6 <= level and level < 0.7:
    level = "Weight Loss"
elif 0.7 <= level and level < 0.8:
    level = "Cardio"
elif 0.8 <= level and level < 0.9:
    level = "Anaerobic"
else:
    level = "Above Level"

print(f"Calories burnt per hour is: {cal:.2f}, for an activity level of: {level}")