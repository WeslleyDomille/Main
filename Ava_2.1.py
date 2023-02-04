#
# Avaliação - Prog.1
# Alunos: Weslley

import re

a = open('arquiv.txt', 'rt')
# n = a.readline()
lines = a.readlines()
line = ' '.join(lines).replace('\n', '').split()

x = 1
c = 0
while c <= len(line):
    listP = list()
    ltemp = list()
    while c <= len(line):
        if line[c-1] == '%':
            c += 1
        if c > len(line):
            break
        ltemp.append(line[c])
        if line[c+1] == '%':
            ltemp.append(int(line[c])+1)
        c += 1
        if line[c] == '%':
            c += 1
            break
    for i in range(0, len(ltemp)):
        if i+1 == len(ltemp):
            break
        if int(ltemp[i]) % 2 != 0 and int(ltemp[i+1]) % 2 != 0:
            x += 1
        elif int(ltemp[i]) % 2 == 0 and int(ltemp[i+1]) % 2 == 0:
            x += 1
        elif int(ltemp[i]) % 2 != 0 and int(ltemp[i+1]) % 2 == 0:
            listP.append(x)
            x = 1
        elif int(ltemp[i]) % 2 == 0 and int(ltemp[i+1]) % 2 != 0:
            listP.append(x)
            x = 1
    for i in listP:
        if i == len(listP):
            if i == listP[i-1]+1:
                break
            print(listP[-1], '\n%')
            break
        if i+1 != listP[i]:
            print('NAO\n%')
            break


a.close()
