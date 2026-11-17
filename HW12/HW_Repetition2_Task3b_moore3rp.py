# Repetition 2: Task 3
# File: HW_Repetition2_Task3b_moore3rp.py 
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
# This script recieves a total number of rental units from the user, 
# then iterates through each unit asking for rent and if the tenant is new. 
# It then calculates the total and average income and prints them.

units = int(input("Number of rental units: "))

income = 0
for unit in range(units):
    rent = float(input(f"Rent for Unit {unit+1}: "))
    new = input("Is the tenant new? (y/n) ")
    if new.lower() == 'y':
        income += rent - 250.0
    else:
        income += rent

average_income = income / units

print(f"Total monthly income: ${income:.2f}")
print(f"Average monthly income per unit: ${average_income:.2f}")








