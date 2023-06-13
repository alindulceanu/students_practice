from queue import Queue as q




N = int(input('N:'))

qu = q(maxsize= N)




for i in range(N):

    qu.put(int(input('value:')))




K = int(input('K:'))




nums = []




for i in range(K):

    nums.append(int(input('value:')))




freq = [0 for i in range(K)]




while qu.full():

    k = qu.get()

    for i in range(K):

        if nums[i] == k:

            freq[i] =+ 1





print(freq)