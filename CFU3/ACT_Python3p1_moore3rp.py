# Activity Python 3: Task 1
# File: ACT_Python3p1_moore3rp.py 
# Date:    06 11 26
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
# This script recieves a negative integer from the user, it then adds 1 to the integer and prints every result until the integer is 0. Finally, it prints the sum of all the numbers.
#
# If you used any resources to complete this assignment (including but # not limited to AI, homework help sites, other students, tutors)  
# please give credit here:
# Resources used. note: if you used an AI please site which AI program you used.

num = int(input("Enter a negative integer: "))
sum = num

print("The sequence is:", num, sep="\n")

while num < 0:
    num += 1
    print(num)
    sum += num

print("The sum of the sequence is", sum)