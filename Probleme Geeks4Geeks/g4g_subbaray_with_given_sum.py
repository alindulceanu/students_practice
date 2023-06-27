'''Given an unsorted array A of size N that contains only positive integers, 
find a continuous sub-array that adds to a given number S and return the 
left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.'''



class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0:
            return [-1]                     # No subarray found
        start = 0
        end = 0
        sum = arr[start]
        
        while end < n:                      
            if sum == s:                    # If sum = s we return the margins of the subarray that adds up to s
                return start+1, end+1
            
            if sum < s:                     # Everytime our sum is less than s, we increment the end
                end += 1
                if end < n:                 # And we add the new value to the sum after we check that it is in the array
                    sum += arr[end]
            else:
                sum -= arr[start]           # If sum becomes bigger than s, we increment the start and we remove the last first value from the subarray
                start += 1
        
        return [-1]                         # No subarray found
    
ob = Solution()
print(ob.subArraySum([1,2,3,7,5], 5, 12))