class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[-1]-arr[0]
        for i in range(1,n):
            if arr[i] - k < 0:
                continue
            ans = min(ans,max(arr[i-1]+k,arr[n-1]-k)-min(arr[0]+k,arr[i]-k))
        
        return ans



    
#https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&status[]=unsolved&sortBy=submissions