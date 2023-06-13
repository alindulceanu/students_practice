'''Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the 
left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.'''



class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0:
            return [-1]
        start = 0
        end = 0
        sum = arr[start]
        
        while end < n:
            if sum == s:
                return start+1, end+1
            
            if sum < s:
                end += 1
                if end < n:
                    sum += arr[end]
            else:
                sum -= arr[start]
                start += 1
        
        return [-1]
    
ob = Solution()
print(ob.subArraySum([1,2,3,7,5], 5, 12))