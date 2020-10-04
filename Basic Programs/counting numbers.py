number = 1
pos_count = 0
neg_count = 0

while(number != 0):
    number = int(input('Please enter a number '))
    if (number > 0 ):
        pos_count = pos_count + 1
    elif(number <0):
        neg_count = neg_count + 1

print('Positive count = ', pos_count)
print("Negetive count = ", neg_count)