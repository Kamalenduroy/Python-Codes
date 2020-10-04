First_iteration = True

while(1):
    if First_iteration:
        health_cond = input('Please input health condition : Excellent or Good or Fair or Poor: ')
        First_iteration = False
    else:
        health_cond = input('Incorrect choice, Please reenter health condition: Excellent or Good or Fair or Poor: ')

    if(health_cond in ['Excellent','Good','Fair','Poor']):
        break

Age = int(input('Please enter Age '))

First_iteration = True

while(1):
    if First_iteration:
        Place = input('where does he/she lives: City or Village: ')
        First_iteration = False
    else:
        Place = input('Incorrect Value entered, please reenter : City or Village: ')

    if(Place in ['City','Village']):
        break

First_iteration = True

while(1):
    if First_iteration:
        Gender = input('Please enter Gender : Male or Female: ')
        First_iteration = False
    else:
        Gender = input('Incorrect Value entered, please reenter : Male or Female: ')

    if(Gender in ['Male','Female']):
        break

Policy_Amount = int(input('please enter policy Amount: '))

if health_cond == 'Excellent' and Age >= 25 and Age <= 35 and Place == 'City' and Gender == 'Male' and Policy_Amount <= 200000:
    Premium = (Policy_Amount/1000)*4
    print('Loop1: Person is insured and Premium = ',Premium)

elif health_cond == 'Excellent' and Age >= 25 and Age <= 35 and Place == 'City' and Gender == 'Female' and Policy_Amount <= 100000:
    Premium = (Policy_Amount / 1000) * 3
    print('Loop2: Person is insured and Premium = ',Premium)

elif health_cond == 'Poor' and Age >= 25 and Age <= 35 and Place == 'Village' and Gender == 'Male' and Policy_Amount <= 10000:
    Premium = (Policy_Amount / 1000) * 6
    print('Loop3: Person is insured and Premium = ',Premium)

else:
    print('Person is not insured ')






















