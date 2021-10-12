t = int(input())

for _ in range(t):
    n = int(input())
    walls = list(map(int, input().split()))
    h = 0
    l = 0
    for i in range(n):
        if i+1 == n:
            break
        else:
            if walls[i] < walls[i+1]:
                h += 1
            elif walls[i] > walls[i+1]:
                l += 1
    print('Case {}: {} {}'.format(_+1, h, l))
