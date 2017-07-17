# Modular Kilometer Converter
# 2 July 17
# CTI-110 M5T1_KilometerConverter 
# Nigel Gonzaga
#GLOBAL CONSTANT
CV=0.6214

#Main Function
def main():
    km=user_input()
    miles=convert_miles(km)
    display_miles(miles)
#Function that asks for user input.
def user_input():
    km=float(input('Enter a distance in Kilometers: '))
    return km
#Function that converts KM to MI
def convert_miles(x):
    y=x*CV
    return y
#Function that Displays Miles
def display_miles(miles):
    print(format(miles, '.2f'),'mi')
#Calls main function and starts program
main()
