#Test the negetive number in Python
cm = input('Please enter cm')
try:
    cm_float = float(cm)
    inch = cm_float / 2.54
    print('Inch = ', inch, " when cm = ", cm_float)

except ValueError:
    print('Enter cm value is not valid')
