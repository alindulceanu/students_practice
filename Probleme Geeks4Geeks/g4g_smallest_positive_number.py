'''You are given an array arr[] of N integers. 
The task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1.'''


class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        arr=set(arr)                            # Turning the array into a set to eliminate duplicates 

        for i in range(1, max(arr)):            # Iterating from to to the max value in the set
            if i not in arr:
                return i                        # If i is not found in the set, it is the missing number
            
        return max(arr)+1 if max(arr)>0 else 1  # If all the values in the set are consecutive, the missing number should be the the incrementation of the max value
                                                # If all the values are negative, the smallest missing number is 1