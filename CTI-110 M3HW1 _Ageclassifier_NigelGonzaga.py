# Programming exercise 3 Age classifier
# 18 JUNE 2017
# CTI-110 M3HW1 - Age Classifier
# Nigel Gonzaga
# Get the variables for the age
adult = 20
teenager = 13
child = 2
infant = 1
# Get the persons age
age = int(input(' Enter your age: '))
# Determine the age
if age >= adult:
    print(' Your an adult.')
else:
    if age >= teenager:
        print(' Your a teenager ')
    else:
        if age >= child:
            print(' Your a child ')
        else:
            print(' Your a infant ')
            
