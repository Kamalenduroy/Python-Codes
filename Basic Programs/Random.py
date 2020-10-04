# Generate a random number and user will be asked to guess that number
# Program will return if the enter number is correct or not
from random import randint

random_number = randint(0,10)

user_input = int(input('Please enter a number '))

if random_number == user_input:   # adksghdksahdkashdksagdksagdsagd
    print('You entered ', user_input, 'Random number generated ', random_number)
    print('Congrats you have guessed the number correctly')
else:
    print('You entered ', user_input, 'Random number generated ', random_number)
    print('You did not guessed the number correctly')

