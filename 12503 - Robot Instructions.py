t = int(input())

for _ in range(t):
    n = int(input())
    inst = []
    for i in range(n):
        command  = list(input().split())
        if len(command) == 1:
            if command[0] == 'LEFT':
                inst.append(-1)
            elif command[0] == 'RIGHT':
                inst.append(1)                           
        else:
            inst.append(inst[(int(command[-1])-1)])
            
    output = 0
    for j in inst:
        output += j
    print(output)
