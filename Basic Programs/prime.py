#print the list of prime numbers

count = 0
print('The prime numbers are : ')
for number in range(1,300):
    divisable_ind = False

    for i in range(2,number-1):
        if(number % i == 0):
            divisable_ind = True
            break

    if(divisable_ind == False):
        count = count + 1
        print('{3}'.format(number),end =' ')
        if(count == 10):
            print('\n')
            count=0





