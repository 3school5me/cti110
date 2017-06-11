# Predict Profit based on total sales
# 10 Jun 17
# CTI-110 M2T1 - Sales Prediction
# Nigel Gonzaga
#
#Get the projected total sales from user.
total_sales = float(input('Enter the projected sales as an interger: '))
#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23
#Display the Profit.
print('The profit is $', format(profit, '.2f'))
