'''This program accept positive and negetive numbers from console and terminates when user
enters zero, progrm returns number of positive and negetive number entered till zero is entered.'''

number = 1
positive = 0
negetive = 0
while (number != 0):
    number = int(input("please enter a number"))
    if number > 0 :
        positive = positive + 1
    elif number < 0 :
        negetive = negetive + 1
    else:
        print('Positive Number entered = ', positive)
        print('Negetive number entered = ', negetive)



