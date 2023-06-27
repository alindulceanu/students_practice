class Solution:
    

    def missingNumber(self,arr,n):
        arr.sort()
        positive = []
        for i in range(n):
            if arr[i] > 0:
                positive.append(arr[i])
            if len(positive) == 0:
                print(1)
        sol = 0
        for i in range(1,len(positive)+1):
            if i not in positive:
                sol = 1
                print(i)
                if sol == 0:
                    print(len(positive)+1)

#https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1?page=2&status[]=unsolved&sortBy=submissions