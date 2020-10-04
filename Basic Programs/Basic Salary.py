Basic_Salary = input('Please enter your basic salary')
try:
    if '.' in Basic_Salary:
        B_S = float(Basic_Salary)
    else:
        B_S = int(Basic_Salary)

    DA = B_S * 0.40
    HRA = B_S * 0.20
    Gross_Salary = B_S + DA + HRA
    print('Gross Salary is ', Gross_Salary)
except ValueError:
    print('The entered salary is not a number')