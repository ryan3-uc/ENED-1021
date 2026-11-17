# Activity Python 4: Task 3
# File: ACT_Python4p3_moore3rp.py 
# Date:    13 11 26
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
# This script computes the Jacobsthal sequence from an inputted number and prints it.

n = int(input("Input a positive, real integer: "))

j0 = 0
j1 = 1

print("Sequence:")
print("0")
print("1")
if n == 1:
    print(j1)
else:
    for i in range(2, n + 1):
        jt = j1 + 2*j0
        print(jt)
        j0 = j1
        j1 = jt



