t = int(input())
count = 1
for _ in range(t):
    a,b,c = map(int, input().split())
    if a==b==c:
        print("Case {}: {}".format(count,a))
        
    elif a>b and a>c :
        if b>c:
            print("Case {}: {}".format(count,b))
        else:
            print("Case {}: {}".format(count,c))
    
    elif b>a and b>c:
        if a>c:
            print("Case {}: {}".format(count,a))
            
        else:
            print("Case {}: {}".format(count,c))
            
    elif c>a and c>b:
        if a>b:
            print("Case {}: {}".format(count,a))
            
        else:
            print("Case {}: {}".format(count,b))
            
    
        
    count += 1
