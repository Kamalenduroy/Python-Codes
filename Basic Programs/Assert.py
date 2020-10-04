Age = int(input('Please enter your age'))

try:
    assert Age > 0 and Age < 100, print('Entered Age is not valid X1')

except AssertionError:
    print('Entered Age is not valid')