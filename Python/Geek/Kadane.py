class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        summ = arr[0]
        current_sum = 0
    
        for num in arr:
            current_sum += num
    
            if current_sum > summ:
                summ = current_sum
            
            if current_sum < 0:
                current_sum = 0
    
        return summ
    
#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1?page=1&status[]=solved&sortBy=submissions