a=8
b=0

try:
    assert b!=0, print('ERROR : division by zero')
    print('value a = ', a)
    print('value b = ', b)
    print ('value a/b = ',a/b)

except AssertionError:
    print('The division was attepted by zero')



