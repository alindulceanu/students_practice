class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        sol = []
        temp = sorted(arr)
        if arr == temp:
            return 0
        elif all(i == arr[0] for i in arr):
            return 0
        else:
            for i in range(n):
                for j in range(i,n):
                    if arr[i] > arr[j]:
                        sol.append((arr[i],arr[j]))
            return len(sol)

#https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&status[]=unsolved&sortBy=submissions