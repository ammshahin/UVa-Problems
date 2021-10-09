def cal(x,y):
    print((x//3) * (y//3))

if __name__ == '__main__':
    t = int(input())

    for x in range(t):
        x,y = map(int, input().split())

        cal(x,y)
