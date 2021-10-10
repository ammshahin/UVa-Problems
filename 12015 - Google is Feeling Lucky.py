
t = int(input())

for _ in range(t):
    sites = []
    max = 0
    
    for i in range(10):
        n,r = input().split()        
        sites.append((n,int(r)))
        if int(r) > max:
            max = int(r)
        
    print('Case #{}:'.format(_+1))
    for a,b in sites:
        if b == max:
            print(a)
    


