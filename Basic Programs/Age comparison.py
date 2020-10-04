John_age = int(input('Please enter the age of John '))
Kelvin_age = int(input('Please enter the age of Kelvin '))
Smith_age = int(input('Please enter the age of smith '))

if(John_age < Kelvin_age):
    if(John_age<Smith_age):
        print('John is youngest')
    elif(John_age == Smith_age):
        print('John and Smith are younger than Kelvin')
    else:
        print('Smith is the youngest')

elif (John_age == Kelvin_age):
    if (John_age == Smith_age):
        print('John, Kelvin and smith are same age')
    elif (John_age < Smith_age):
        print('John and Kelvin are youngest')
    else:
        print('Smith is the youngest')

else:
    if(Kelvin_age == Smith_age):
        print('Kelvin and Smith are youngest')
    elif(Kelvin_age < Smith_age):
        print('Kelvin is youngest')
    else:
        print('Smith is the youngest')



