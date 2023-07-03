
class Solution:

	def maxIndexDiff(self,arr,n):
		i = 0
		j=n-1
		ans=0;
        while i <= j:
            if arr[i]<=arr[j]:
                ans  = max(ans,j-i)
                i += 1
                j = n-1
            else:
                j -= 1
        return ans

#https://practice.geeksforgeeks.org/problems/maximum-index3307/1