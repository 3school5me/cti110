# Adds even numbers together
# 25 Jun 17
# CTI-110 M4HW1 - Sum of Numbers
# Gonzaga, Nigel
#
x=0
y=0
while x>=0:
    x=float(input('positive interger to add negative interger to stop and display sum: '))
    if x>0:
        y=x+y
    if x<0:
        print('The sum of all positive values is',y)
