class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[n-1]-arr[0]
        for i in range(1,n):
            ans = min(ans,max(arr[i-1]+k,arr[n-1]-k)-min(arr[0]+k,arr[i]-k))
        
        return ans 
    
#https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1