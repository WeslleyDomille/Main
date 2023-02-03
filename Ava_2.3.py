# Avaliação - Prog.1
# Aluno: Weslley Domille


import re

read = open('entrada.txt', 'rt')

present = {1:'o', 2:'os', 3:'a', 4:'om', 5:'ons', 6:'am'}
past = {1:'ei', 2:'es', 3:'e', 4:'em', 5:'est', 6:'im'}
future = {1:'ai', 2:'ais', 3:'i', 4:'aem', 5:'aist', 6:'aim'}

for line in read.readlines():
    line = line.strip()

    match = re.search(r'([^bcdfghjklmnpqrstvwxz][a-z]{0,2}$)', line)
    sufx = str(match.group(1))
    suf_p = ''
    tempo = ''

    for k, i in present.items():
        if i == sufx:
            suf_p = sufx
            tempo = 'presente'
            Verbo = line.replace(sufx, 'en')
            print('{} - verbo {}, {}, {}º pessoa'.format(line, Verbo, tempo, k))
        
    for k, i in past.items():
        if i == sufx:
            suf_p = sufx
            tempo = 'pretérito'
            Verbo = line.replace(sufx, 'en')
            print('{} - verbo {}, {}, {}º pessoa'.format(line, Verbo, tempo, k))
        
    for k, i in future.items():
        if i == sufx:
            suf_p = sufx
            tempo = 'futuro'
            Verbo = line.replace(sufx, 'en')
            print('{} - verbo {}, {}, {}º pessoa'.format(line, Verbo, tempo, k))
        
    if suf_p == '':
        suf_p = 'não é um tempo verbal'
        print('{} - {}'.format(line, suf_p))
    

read.close()