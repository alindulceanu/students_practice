'''Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.'''
#Using Kadane's algorithm

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sum = 0
        maxSum = -999999999999
        
        for i in range(len(arr)):
            sum += arr[i]               #Adding the current value to the sum, 
                                        #without looking for the negative integers
            if sum > maxSum:            #Updateing the maxsum if sum is greater
                maxSum = sum
                
            if sum < 0:                 #Reseting the sum if it's gone negative
                sum = 0
                
        return maxSum
    

    
ob = Solution()

print(ob.maxSubArraySum([1,2,-5,3,2,-1], 6))

