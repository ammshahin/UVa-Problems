n = int(input())

while n>=1 and n<=100:
    m = int(input())

    inp = list(map(int,input().split()))
    if m == len(inp):
        print((max(inp)-min(inp))*2)
        
    n-=1
