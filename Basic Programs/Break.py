#Illustrate break statement

for number in '123456789':
    if (number == '5'):
        continue
    print('Current Number is ', number)
else:
    print('else part of for, current iteration number is ', number)

print('outside of for loop')