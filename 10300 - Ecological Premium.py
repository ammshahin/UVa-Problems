t = int(input())

for _ in range(t):
    f = int(input())
    total = 0
    for i in range(f):
        a,b,c = map(int, input().split())
        total += ((a/b)*c)*b
    print(round(total))
