# Program will randomly generate a multiplication question and ask user to solve it
# Program will also display if answer is correct or not

from random import randint

count = 0

for index in range(0,10):
    a = randint(0,10)
    b = randint(0,10)
    c = a * b
    print (a ,' X ', b , ' = ? ')
    d = int(input())
    if c == d:
        count = count + 1
        print('you are right')
    else:
        print('You are wrong')

    if index == 9:
        print ('Number of correct answers = ', count)
    else:
        print('Next question is')
