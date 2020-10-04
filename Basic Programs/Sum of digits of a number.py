'''This program takes a integer number as input and prints sum of digits of that number'''

Number_str = input('Please enter a numeric number ')

def sum_of_number(x):

    if x.isdigit():
        length_of_Number = len(x)
        sum = 0
        for i in range(0,length_of_Number):
            sum = sum + int(x[i])
        print('The sum of the',x, ' is: ', sum)
    else:
        print('The number is not a numeric Number')


sum_of_number(Number_str)
