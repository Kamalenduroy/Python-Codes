a = 10
b = 15



print('a = ',a)
print('b = ',b)

def fun():
    global a,b

    a = 20
    b = 25

    print('inside function a = ',a)
    print('inside function b = ',b)

fun()

print('a = ',a)
print('b = ',b)

