n = int(input())
count = 0
if n>=1 and n<=100:
    while n>0:
        st = str(input()).split()
        if st[0] == 'donate':
            num = int(st[1])
            if num >= 100 and num <= 100000:
                count+= num
        elif st[0] == 'report':
            print(count)
        n-=1
        
