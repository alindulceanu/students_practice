from queue import Queue

N = int(input("Enter number of N intigers: "))
q1 = Queue(maxsize = N)
for i in range(N):
    q1.put(int(input("Elements of the queue: ")))
for i in range(N):
    print(q1.get())

M = int(input("Enter number of M intigers: "))
q2 = Queue(maxsize = N)
for i in range(N):
    q2.put(int(input("Elements of the queue: ")))
for i in range(N):
    print(q2.get())

q3 = sum(len(q1)+len(q2))
#while q3.empty(False):
