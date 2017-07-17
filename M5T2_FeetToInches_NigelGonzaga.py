# Converts feet to inches
# 2 July 17
# CTI-110 M5T2_FeetToInches 
# Nigel Gonzaga
# Define main function
def main():
    feet=user_input()
    inches=conversion(feet)
    display(inches)
# Define user input function
def user_input():
    x=float(input('Input a length in feet: '))
    return x
# Define conversion function
def conversion(x):
    CV=12
    y=x*CV
    return y
# Define display funtion
def display(x):
    print(format(x, '.2f'),'in')
# Calls main function and starts program
main()
    
