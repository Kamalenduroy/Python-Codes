age = int(input('Please enter your age '))

try:
    assert age >0 and age < 110, print('The enter age is not valid')
    print('The age is = ', age)

except AssertionError:
    print('The Age is not valid')