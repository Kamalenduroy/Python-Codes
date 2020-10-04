#This program illustrate how to throw error
import sys
try:
    number1 = int(input('Please enter a number '))
    number2 = int(input('Please enter another number '))

    result = number1/number2

    print('The result of number1 / number2 = ', result)

except ValueError:
    print('Enter value is not in correct format')

except ZeroDivisionError:
    print('Denominitor can not be zero')

except:
    print('Something is wrong, error code = ', sys.exc_info())


