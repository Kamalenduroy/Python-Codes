'''Diff_string will take two string as input and retrun the location where first diff occured'''

string1 = input('Please enter a name ')
string2 = input ('Please enter second name ')

def match_func(string1, string2):
    i = 0
    mismatch = 'N'
    while i < len(string1) and i < len(string2) :

        if string1[i] != string2[i]:
            mismatch = 'Y'
            break

        i = i + 1

    if mismatch == 'Y':
        return(i)
    else:
        if len(string1) == len(string2):
            return(-1)
        else:
            return(i)

Retrun_code = match_func(string1,string2)

if Retrun_code == -1 :
    print('Strings are same')
else:
    print('String are differ at position ', Retrun_code)


