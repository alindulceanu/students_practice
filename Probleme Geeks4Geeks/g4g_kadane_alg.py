'''Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.'''


class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sum = 0
        maxSum = -999999999999
        
        for i in range(len(arr)):
            sum += arr[i]
            
            if sum > maxSum:
                maxSum = sum
                
            if sum < 0:
                sum = 0
                
        return maxSum

