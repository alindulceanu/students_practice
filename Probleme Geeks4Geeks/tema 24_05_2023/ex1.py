
N = int(input('N:'))
arr = []

for i in range(N):
    values = input('arr:')
    arr.append(int(values))

K = int(input('k:'))

split = []

for xD in range(N - K):
    sum = 99999999999
    for i in range(int(len(arr) / 2 )+ 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < sum:
                sum = arr[i] + arr[j]
                bestI = arr[i]
                bestJ = arr[j]
    
    split.append([bestI, bestJ])
    arr.remove(bestI)
    arr.remove(bestJ)

for i in arr:
    split.append([i])



