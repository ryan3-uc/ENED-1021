# Activity Python 4: Task 1
# File: ACT_Python4p1_moore3rp.py 
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
# This script recieves a negative integer and counts up by one until it reaches 0 and prints the results.

num = int(input("Please enter an integer: "))
print(num)

total = num
print("The sequence is:")
for i in range(abs(num)):
    num += 1
    print(num)
    total += num
print(f"The sum of the sequence is {total}.")


