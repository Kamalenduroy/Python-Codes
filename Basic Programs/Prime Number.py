'''Function will accept a vlue from user and return true or false if the number is prime or not'''

#Input from User
try:
    Number = int(input("Please eneter a number"))

except:
    print('The enter number is not an integer ')

def prime(number):
    for i in range(2,number):
        if number % i == 0:
            print('Inside if block ', i)
            return(False)

    return(True)
    print("outside if block")

if prime(Number) == True:
    print('The number ', Number , ' is prime Number ')
else:
    print('The number ', Number, ' is not a prime number')


