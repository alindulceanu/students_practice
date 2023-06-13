N = int(input("N:"))
A = []
x = str(input())

A = x.split(' ')

for i in range(N):
A[i] = int(A[i])


def largButMinFreq(arr,n):
    freq = {}
    arr = []
    for i in A:
        if i in freq:
            freq[i] += 1

        else:
            freq[i] = 1

    mini = min(freq.values())
    for i in freq:
        if freq[i] == mini:
            arr.append(i)
    return max(arr)


print(largButMinFreq(A, N))

