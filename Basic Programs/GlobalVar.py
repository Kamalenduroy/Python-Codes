#Illustrate the global variable function

a = 10
b = 15

def function_a ():
    global a = 20
    global b = 25

    print('Inside function a = {} and b = {}'.format(a,b))

function_a()

print('Outside function a = {} and b = {} '.format(a,b))

