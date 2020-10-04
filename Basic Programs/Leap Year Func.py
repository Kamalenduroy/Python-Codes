'''This is Leap year Function, program will take a input from console and return Y or N
    '''

Year = int(input('Please enter a year'))

def leap_year(year):

    leap_year_ind = 'N'

    if year % 4 == 0:
        if year % 400 == 0:
            print('This year is devided by 400')
            leap_year_ind = 'Y'
        elif year % 100 == 0:
            print('This year is devided by 100')
            leap_year_ind = 'N'
        else:
            print('This year is devided by 4')
            leap_year_ind = "Y"

    return (leap_year_ind)

if leap_year(Year) == 'Y':
    print('This is a leap year')
else:
    print('This is not a leap year')



