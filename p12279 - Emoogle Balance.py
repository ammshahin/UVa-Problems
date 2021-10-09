t = 1 
while True:
     
    n = int(input())
    if n ==0 or t>74:
        break
    
    count = 0
    for x in map(int, input().split()):
        if x == 0:
            count -= 1
        elif x >0  and x < 100:
            count += 1

    print("Case {}: {}".format(t,count))
    t+=1
        
