# Algorithm workbench number 4
# 18 JUNE 2017
# CTI-110 M3T2 - Debugging
# Nigel Gonzaga
# This program gets test scores and gives them a letter grade
# Numbers to represent the grade
A_score = 90
B_score = 80
C_score = 70
D_score = 60
# Now get a test score
score = int(input(' Enter your test score:'))
# Determine the grade
if score >= A_score:
    print(' Your grade is A.')
else:
    if score >= B_score:
        print(' Your grade is B.')
    else:
        if score >= C_score:
            print(' Your grade is c.')
        else:
            if score >= D_score:
                print(' Your grade is D.')
            else:
                print(' Your grade is F.') 
        
