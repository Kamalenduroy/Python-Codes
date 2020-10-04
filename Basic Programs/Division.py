#This program is to determine grade of a student
number1 = int(input('please enter Number 1 '))
number2 = int(input('please enter Number 2 '))
number3 = int(input('please enter Number 3 '))

avg = (number1 + number2 + number3) / 3

if avg >= 60 :
    print('First Division')
elif avg >= 50:
    print('Second Division')
else:
    print('Third Division')
