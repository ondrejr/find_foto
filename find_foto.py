"""
This script can load a list of directories (containing photos) into a file. 
It can then search in this file by substring.
"""

import os
import datetime

pth = 'x:\\foto'
#pth = 'c:\\Doc\\Foto'
pth='q:'
i = [0]

def dir(pth, pths = []):
    """
    Recursively writes the contents of the directory to a file.
    """
    for entr in os.listdir(pth):
        cesta = pth + '\\' + entr
        if os.path.isdir(cesta):
            i[0] += 1    
            print('{} {}'.format(i, cesta))
            dir(cesta, pths = [])
        else:
            dat = '{}'.format(datetime.datetime.fromtimestamp(os.path.getmtime(cesta)))[:10]
            if dat not in pths:
                pths.append(dat)
    if pths != []:
        with open("list.txt", "a+") as lst:
            lst.write('{};{}\n'.format(pth, set(pths)))


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
                #ad = adr.split(',')
                adrs = adr.rstrip().split(';')
                lax = adrs[1].rstrip().split(',')
                mi = '2100'
                ma = ''
                for i in lax:
                    val = i.split("'")[1]
                    if val < mi:
                        mi = val
                    if val > ma:
                        ma = val
                if mi == ma:
                    print('{} {}'.format(adrs[0], mi))
                else:    
                    print('{} {} {}'.format(adrs[0], mi, ma))
                #print('{} {}'.format(adrs[0], lax))
                last = ad[0][:ind]
                #i = 0
    la=inp()
