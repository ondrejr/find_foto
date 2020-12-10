"""
This script can load a list of directories (containing photos) into a file. 
It can then search in this file by substring.
"""
import os

def dir(pth, i):
    """
    Recursively writes the contents of the directory to a file.
    ""
    for entr in os.listdir(pth):
        cesta = pth + '\\' + entr
        if os.path.isdir(cesta):
            with open("list.txt", "a+") as lst:
                lst.write(cesta+'\n')
            i += 1    
            print('{} {}'.format(i, cesta))
            dir(cesta, i)

def inp():
    """
    Enter the name of the searched key + data initialization.
    """
    print('1 - init: ')
    print()
    print('zadej jméno adresáře na 3: ')
    la = input()
    if la == '1':
        try:
            os.remove('list.txt')
        except FileNotFoundError:
            pass
        dir('d:\\foto', 0)
        imp()
    else:    
        return la.lower()


la=inp()
last = ''
#i = 0
while la != '':
    if len(la) >= 3:
        with open("list.txt", "r") as lst:
            re = lst.readlines()    
        for adr in re:
            ind = adr.rstrip().lower().find(la)
            if ind > -1:
                if (last == adr[:ind]): # or (i<5):
                    print('  '+adr[ind:].rstrip())
                    #i +=1
                else:
                    print(adr.rstrip())
                    last = adr[:ind]
                    #i = 0
    la=inp()
