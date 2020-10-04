'''Program accepts a group of numbers as input , then find out the occurence of max number'''

input = input('Please enter few numbers ending with zero')
l = input.split(' ')

max = l[0]
freq = 1

for i in range(1,len(l)):
    if l[i] > max:
        max = l[i]
        freq = 1
    elif l[i] == max :
        freq = freq + 1

print('Max number is ', max, ' freq = ', freq)


