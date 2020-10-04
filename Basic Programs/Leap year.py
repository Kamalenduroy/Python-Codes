#Eneter a year and program will return if that year is a leap year or not

def leap_year(year):
    if(year%4 == 0):
        if(year%400 == 0):
            print('{} is a leap year'.format(year))
        elif(year % 100 == 0):
            print('{} is not a leap year'.format(year))
        else:
            print('{} is a leap year'.format(year))
    else:
        print('{} Number is not a Leap year'.format(year))

leap_year(2000)

leap_year(1996)

leap_year(1900)

leap_year(2005)
