Number = input('Please enter your a number')
if Number.isdigit():
    print('The reverse order of ', Number, ' is = ')
    for index in range(len(Number)):
        print((Number[((len(Number)-1)-index)]),end = '')
else:
    print('This is not a numeric number')