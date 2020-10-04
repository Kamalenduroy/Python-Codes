Number = input('Please enter a number')
if Number.isdigit():
    sum  = 0
    for index in range(len(Number)):
        sum = sum + int(Number[index])
    print('The sum is ', sum)
else:
    print('This is not a numeric number')
