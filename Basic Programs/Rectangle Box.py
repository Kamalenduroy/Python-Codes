'''Program call a function that display output in rectangle box when length and breath are passed'''

try:
    length = int(input('Please enter length of the rectangle '))
    breath = int(input('Please eneter breath of the rectangle '))

except:
    print('Please enter a valid number')

def rectangle_star_print(length = 0, breath = 0):
    for i in range(0,length):
        print('')
        for j in range(0,breath):
            print('*',end='')

rectangle_star_print(length,breath)
