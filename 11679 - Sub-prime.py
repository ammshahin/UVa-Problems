

while True:
    b,n = map(int, input().split())
    if b==0 and n==0:
        break
    reserve = list(map(int, input().split()))
    possible = True
    for i in range(n):
        d,c,v = map(int, input().split())
        reserve[d-1] -= v
        reserve[c-1] += v
    for i in reserve:
        if i<0:
            possible = False
    if possible == True:
        print('S')
    else:
        print('N')
