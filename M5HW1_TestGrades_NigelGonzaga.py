# Test grade averager.
# 9 July 17
# CTI-110 M5HW1 - Test Average and Grade
# Nigel Gonzaga

#Define Main Function
def main():
    avg=calc_average()
    determine_grade(avg)
#Function that calculates the average of a user's input.
def calc_average():
    List=[]
    print('''This Program will ask for 5 test scores in a row.''')
    print('''Enter "-1" at any time to quit.''')
    for x in range(5):
        test=float(input('Enter test score:  '))
        if test == -1:
            break
        List.append(test)
        print(List)
    if x == 4:
        avg=(sum(List)/5)
        return avg
        print(avg)
    else:
        return -1
#Function that determines average grade.
def determine_grade(x):
    if x >=90:
        print('Congratulations!  You recieved an A with an average of %s.'% x)
    elif x >= 80 and x < 90:
        print('Good Job.  You recieved a B with an average of %s.' %x)
    elif x >= 70 and x < 80:
        print('You recieved a C with an average of %s, push yourself harder next time.' % x)
    elif x >= 60 and x < 70:
        print("You recieved a D with an average of %s, think about what you're doing with your life." % x)
    elif x >= 0 and x < 60:
        print('You recieved a F with an average of %s, why are you even here?' % x)
    else:
        print('Quitting Program')
main()
    
