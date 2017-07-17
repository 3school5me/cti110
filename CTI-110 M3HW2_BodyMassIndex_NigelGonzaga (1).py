# Programming exercise 3 Age classifier
# 18 JUNE 2017
# CTI-110 M3HW2 - Body Mass Index
# Nigel Gonzaga
# Get the persons weight
weight = int(input('Enter weight in pounds: '))
# Get the persons height
height = int(input('Enter height in inches: '))
# Calculate the BMI
bmi = (weight / (height * height)) * 703.0
# Display the persons BMI
print(' Your BMI is', (bmi)) 
# Determine the status of there weight
if bmi >= 0:
    print ('Your weight status is under weight')
else:
    if bmi >= 18.5: 
        print ('Your weight status is optimal weight')
    else:
        if bmi >= 25:
            print (' Your weight status is over wieght')
