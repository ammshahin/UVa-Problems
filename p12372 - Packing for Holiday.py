t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())

    if x<21 and y<21 and z <21:
        print('Case {}: good'.format(i+1))
    else:
        print('Case {}: bad'.format(i+1))
        
