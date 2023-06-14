

k=5
arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
sol = []
middle = int(len(arr)/2)
for i in arr[0:middle]:
        if i <= arr[middle]:
            sol.append(i+k)
        else:
            sol.append(i-k)
for j in arr[middle:]:
        if j >= arr[middle]:
            sol.append(j-k)
        else:
            sol.append(j+k)
sol.sort()
sum = sol[-1] - sol[0]
print(sum)


