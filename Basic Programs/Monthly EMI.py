Loan_Amount=int(int(input('Please enter Loan Amount')))
Interest = float(input('Please enter Interest rate'))
Year = int(input('Please enter Loan tenure'))
EMI= (Loan_Amount*Interest)/(1-(1/(1+Interest)**(Year*12)))
print('EMI = ', EMI)