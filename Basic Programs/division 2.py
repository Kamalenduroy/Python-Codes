number1 = int(input('Please enter mark for subject 1 '))
number2 = int(input('Please enter mark for subject 2 '))
number3 = int(input('Please enter mark for subject 3 '))
number4 = int(input('Please enter mark for subject 4 '))
number5 = int(input('Please enter mark for subject 5 '))

avg = (number1+number2+number3+number4+number5)/5
print('avg = ', avg)

if(avg >= 60):
    print('First Div')
elif(avg>=50):
    print('second div')
else:
    print('Third Div')








