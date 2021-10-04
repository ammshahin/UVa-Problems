while (1):
    k = int(input())
    if k == 0:
        break
    n,m = map(int,input().split()) 
    while k>0 and k<10**3:        
        x,y = map(int,input().split())
        if x-n == 0 or y-m == 0:
            print('divisa')
        elif x-n > 0:
            if y-m > 0:
                print('NE')
            else:
                print('SE')
        elif x-n < 0:
            if y-m > 0:
                print('NO')
            else:
                print('SO')
        k-=1
       
