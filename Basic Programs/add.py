input1 = 10
input2 = 15
input3 = 20

def add(**a):
    sum = 0
    for key,value in a.items():
        sum = sum + value

    return sum

print('the sum of above two numbers are : ', add(a=input1,b=input2,c=input3))

