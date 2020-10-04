'''Enter a number , a pyramid will be displayed , for example if 3 is entered then displayed pyramid will be as below
   1
 212
32123'''

Number = int(input('Please enter a number '))
print('The pyramid of number ',Number, ' is:')

for i in range(1,Number+1):
    for j in range(Number, 0, -1):
        if (j <= i):
            print(j, end='')
        else:
            print(' ', end='')
    for j in range(2, Number+1):
        if(j <= i):
            print(j, end='')
        else:
            print(' ', end='')
    print('\n')



