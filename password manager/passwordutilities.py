import secrets
import string
import subprocess

characters = string.ascii_letters
numbers = ['0','1','2','3','4','5','6','7','8','9','0']
symbols = ['!','"','£','$','%','^','&','(',')','#',';',':','~']

usinglist = []

def genlist(UsingLetters, UsingNumbers, UsingSymbols):

    returnlist = []
    
    if UsingLetters == 1:
        returnlist = [*returnlist, *characters]

    if UsingNumbers == 1:
        returnlist = [*returnlist, *numbers]

    if UsingSymbols == 1:
        returnlist = [*returnlist, *symbols]

    return returnlist

def genpassword(length, UsingLetters, UsingNumbers, UsingSymbols, CopyList):
    
    usinglist = genlist(UsingLetters, UsingNumbers, UsingSymbols)

    if len(usinglist) == 0:
        return 'Select some types to use'
    
    passgen = ''
    
    for i in range(0,length):   
        letter = secrets.choice(usinglist)
        passgen = passgen + letter

    if CopyList == 1:
        subprocess.run("clip", universal_newlines=True, input=passgen)
    
    return passgen

