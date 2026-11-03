# Activity Python 2: Task 3
# File: ACT_Python2p3_moore3rp.py 
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
# This script recieves inputs (k1, k2, ftotal, and config) and calculates spring forces and positions.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

k1 = float(input("Spring coefficient of spring 1: "))
k2 = float(input("Spring coefficient of spring 2: "))
ftotal = float(input("Total force: "))
config = float(input("Series (1) or parallel (2)? "))

if config == 1:
    keq = (k1*k2) / (k1 + k2)
    f1 = f2 = ftotal
    x1 = f1 / k1
    x2 = f2 / k2
    xtotal = x1 + x2
else:
    keq = k1 + k2
    xtotal = ftotal / keq
    x1 = x2 = xtotal
    f1 = x1*k1
    f2 = x2*k2

print(
    f"K(eq) = {keq:.2f} N/m", 
    f"F1 = {f1:.2f} N", 
    f"F2 = {f2:.2f} N", 
    f"x1 = {x1:.2f} m", 
    f"x2 = {x2:.2f} m", 
    f"x(total) = {xtotal:.2f} m", 
sep="\n")