n = 4
k = 10
a = [1, 2, 3, 4]
pair = []
sol = 0
temp = []
for i in a:
    if len(pair) == 0:
        pair.append(a[i])
    if len(pair) == 1:
        pair.append(a[i+1])
    if a[i] < k:
        temp.append(i)
        sol += 1
    if a[i] + n < k:

        sol += 1
print(sol)
