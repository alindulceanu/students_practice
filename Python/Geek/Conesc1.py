class Solution:

	def countStrings(self,n):
        mod = 10**9+7
        arr = [0 for i in range(n+1)]
        arr[0] = 1
        arr[1] = 2
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[-1]%mod

 #https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1?page=1&status[]=solved&sortBy=submissions       