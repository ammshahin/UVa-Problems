
t = int(input())

for _ in range(t):
    n = int(input())
    mile = 0
    juice = 0
    calls = list(map(int,(input()).split()))
    for i in range(n):
        mile += ((int(calls[i]/30) *10)+10)
        juice += ((int(calls[i]/60) *15)+15)
    if mile == juice:
        print('Case {}: Mile Juice {}'.format(_+1,mile))
    elif mile < juice:
        print('Case {}: Mile {}'.format(_+1,mile))
    else:
        print('Case {}: Juice {}'.format(_+1,juice))
        
