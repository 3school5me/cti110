# Calculates the required tip tax and total bill from a restauraunt.
# 10 Jun 17
# CTI-110 M2HW2 - Tip Tax Total
# Nigel Gonzaga
#
#User Imput for price of meal
Initial = float(input('Cost of meal without tip and tax factored in: '))
#Calculations 
Tax = float(format(.07*Initial, '.2f'))
Tip = float(format(.18*Initial, '.2f'))
Total = (Tax+Tip+Initial)
#Output
print('The tax is $%s' % Tax)
print('The tip is $%s' % Tip)
print('The total is Cost of the meal is $%s' % Total)
