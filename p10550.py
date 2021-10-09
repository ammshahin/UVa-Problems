while True:
    a,b,c,d = map(int, input().split())

    if a==b==c==d==0:
        break
    else:
        print(1080+(((a-b+40)%40)+((c-b+40)%40)+((c-d+40)%40))*9)
