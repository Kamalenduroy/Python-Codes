'''Calculating digital root of a number '''

try:
    Number = int(input('Please enter an integer '))

except:
    print('Please enter a valid integer ')

def digital_root(number):
    sum = 0

    while (number > 9 ):

        while ( number != 0 ) :
            Reminder = number % 10
            number = int(number / 10)
            sum = sum + Reminder
            print('rem = ',Reminder)
            print('Quetient = ', number)

        number = sum
        sum = 0
        print('The intermidiate number is ', number)

    return(number)

print('The digital root of ', Number, ' is : ', digital_root(Number))

