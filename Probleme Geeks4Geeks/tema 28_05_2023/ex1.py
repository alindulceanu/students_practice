queue = list()
queue2 = list()
queue3 = list()
N = int(input('N:'))

for i in range(N):
    queue.append(int(input('queue:')))

M = int(input('M:'))

for i in range(M):
    queue2.append(int(input('queue2:')))

while len(queue2) != 0:
    queue3.append(queue.count(queue2.pop(0)))

print(queue3)