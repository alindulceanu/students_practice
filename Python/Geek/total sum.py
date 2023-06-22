n=4
k=6
arr = [1,5,7,1]


second = sorted(arr, reverse = True)
sol = 0
prob = 0
for i in second:
    if i > k:
        continue
    if i == k:
        sol += 1
    if i <= k:
        prob += i
        if prob == k:
            sol +=1
            prob = 0
        if prob > k:
            break
        if prob <= k:
            continue
print(sol)