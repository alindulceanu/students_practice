N = int(input("Enter number of N intigers: "))
q1 = []
for i in range(N):
    q1.append(int(input("Elements of the queue: ")))
print(q1)

M = int(input("Enter number of M intigers: "))
q2 = []
for i in range(M):
    q2.append(int(input("Elements of the queue: ")))
print(q2)

for element in q2:
    count = q1.count(element)
    if count > 0:
        print(f"{element}:{count}")
    else:
        print(f"{element}:-1")