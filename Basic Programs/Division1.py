#This program is to determine grade of a student
Numbers = input("please enter five numbers one after another separated by space ")
l1 = Numbers.split()

for index in [0,1,2,3,4]:
    l1[index] = int(l1[index])

else:
    print('End of the for loop')
    print('The index value is : ', index)


avg = (l1[0] + l1[1] + l1[2] + l1[3] + l1[4]) / 5

if avg >= 60 :
    print('First Division')
elif avg >= 50:
    print('Second Division')
else:
    print('Third Division, average mark is ',avg)
