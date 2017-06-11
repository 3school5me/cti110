# A brief program that displays the distance a car travels.
# 10 Jun 17
# CTI-110 M2HW1 - Distance Traveled 
# Nigel Gonzaga
#
# User Imput for variable time.
Variabletime = float(input('How many hours were you driving? (must provide an interger): '))
# Car's speed
speed = 70
#Distance variables
sixhours = speed*6
tenhours = speed*10
fifteenhours = speed*15
Variablehours = speed*Variabletime
#Distance output strings
six = 'The distance traveled in 6 hours is %s miles.'
ten = 'The distance traveled in 10 hours is %s miles.'
fifteen = 'The distance traveled in 15 hours is %s miles.'
Variable = 'The distance Traveled in %s hours is %s miles.'
#Output
print(six % sixhours)
print(ten % tenhours)
print(fifteen % fifteenhours)
print(Variable % (Variabletime, format(Variablehours, '.0f')))
