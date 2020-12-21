"""
This script can load a list of directories (containing photos) into a file. 
It can then search in this file by substring.
"""

import os

pth = 'x:\\foto'
i = [0]

def dir(pth):
    """
    Recursively writes the contents of the directory to a file.
    """
    for entr in os.listdir(pth):
        cesta = pth + '\\' + entr
        if os.path.isdir(cesta):
            with open("list.txt", "a+") as lst:
                lst.write(cesta+'\n')
            i[0] += 1    
            print('{} {}'.format(i, cesta))
            dir(cesta)

def inp():
    """
    Enter the name of the searched key + data initialization.
    """
    print()
    print('1 - init: ')
    print('enter parts of directory names separated by a space: ')
    la = input()
    if la == '1':
        try:
            os.remove('list.txt')
        except FileNotFoundError:
            pass
        dir(pth)
        return inp()
    else:    
        return la.lower()


la=inp()
last = ''
#i = 0
while la != '':
    if len(la) > 1:
        with open("list.txt", "r") as lst:
            re = lst.readlines()    
        for adr in re:
            pokr = True
            for ad in la.lower().split(' '):
                ind = adr.rstrip().lower().find(ad)
                if ind == -1:                        # if 1 of the separated space does not fit, then not found
                    pokr = False
            if pokr:
                """
                if (last == adr[:ind]): # or (i<5):
                    print('  '+adr[ind:].rstrip())
                    #i +=1
                else:
                """
                print(adr.rstrip())
                last = adr[:ind]
                #i = 0
    la=inp()
