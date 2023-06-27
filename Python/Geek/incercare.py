N=6
K=2
tasks=["A","A","A","B","B","B"]
time = 0
temp = []
clock = 0
while len(temp) < N:
    for i in range(1, N+1):
        clock += i
        if tasks[i] == tasks[i+1]:
            continue
        else:
            temp.append(i)
            time += 1
print(time)