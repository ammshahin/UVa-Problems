t = 1
while True:
    s = str(input())
    if s == '#':
        break
    elif s == 'HELLO':
        print('Case {}: ENGLISH'.format(t))
    elif s == 'HOLA':
        print('Case {}: SPANISH'.format(t))
    elif s == 'HALLO':
        print('Case {}: GERMAN'.format(t))
    elif s == 'BONJOUR':
        print('Case {}: FRENCH'.format(t))
    elif s == 'CIAO':
        print('Case {}: ITALIAN'.format(t))
    elif s == 'ZDRAVSTVUJTE':
        print('Case {}: RUSSIAN'.format(t))
    else:
        print('Case {}: UNKNOWN'.format(t))
    t+=1
