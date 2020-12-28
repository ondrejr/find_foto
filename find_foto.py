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

vals = {}
vals['min_date'] = '1990-01-01'
vals['max_date'] = '2100-12-31'


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


def input_date(txt, vls):
    print('input {}date:'.format(txt))
    la = input()
    if len(la) > 3:
        vals[vls] = la + vals[vls][len(la):]
    else:
        print('invalid input')
    return la


def inp():
    """
    Enter the name of the searched key + data initialization.
    """

    print()
    print('1 - init / 2 - min date / 3 - max date: ')
    print('min date: {}'.format(vals['min_date']))
    print('max date: {}'.format(vals['max_date']))
    print('enter parts of directory names separated by a space: ')
    la = input()

    if (la == '1') or (la == '2') or (la == '3'):
        if la == '1':
            print('are you sure y/n ?')
            la = input()
            if la.lower() == 'a':
                try:
                    os.remove('list.txt')
                except FileNotFoundError:
                    pass
                dir(pth)
        if la == '2':
            la = input_date('min.', 'min_date')
        if la == '3':
            la = input_date('max.', 'max_date')
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
                mi = vals['max_date']
                ma = ''
                for i in lax:                       # zjistit maximální minimální hodnoty
                    val = i.split("'")[1]
                    if (val >= vals['min_date']) and (val <= vals['max_date']):
                        if val < mi:
                            mi = val
                        if val > ma:
                            ma = val
                        pr = True    
                    else:
                        pr = False
                if pr:                
                    if mi == ma:
                        print('{} {}'.format(adrs[0], mi))
                    else:    
                        print('{} {} {}'.format(adrs[0], mi, ma))
                    last = ad[0][:ind]
    la=inp()
