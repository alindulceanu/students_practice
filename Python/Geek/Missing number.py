class Solution:
    def missingNumber(self,array,n):
        totalSum = sum(range(n+1))
        arraySum = sum(array)
        
        if totalSum != arraySum:
            return totalSum-arraySum

#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&status[]=solved&sortBy=submissions