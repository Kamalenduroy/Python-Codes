days = int(input('Please enter number of days in the month '))
starting_day = int(input('Please enter starting day of this month '))

count = 0

#printing the starting spaces for that mont

for index in range(1,starting_day): #[1-6]
    print(end='   ')
    count = count + 1

for day in range(1,days+1):

    print('{:02d}'.format(day),end=' ')

    count = count + 1
    if count in [7,14,21,28,35]:
        print()


