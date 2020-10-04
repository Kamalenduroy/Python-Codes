def ave():
    Marks_input  = input('Please enter Marks for 5 subjects separated by space ')
    Marks = Marks_input.split()
    sum = 0
    for i in range(0,5):
        sum = sum + int(Marks[i])
    Avg = sum /5
    Percentage = (sum /500)*100
    print('The sum of 5 subjects = ',sum,' The Average = ', Avg, ' The Percentage is = ', Percentage )

ave()
ave()
