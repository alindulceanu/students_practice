N = int(input("N terms: "))
q1=[]

for i in range(N):
    q1.append(int(input("Elements of the queue: ")))
print(q1)

print ([n for i, n in enumerate([len(q1)]) if i == n])