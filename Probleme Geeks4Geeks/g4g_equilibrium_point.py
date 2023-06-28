'''Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum 
of elements after it.

Note: Retun the index of Equilibrium point. (1-based index)'''

class Solution:
    def equilibriumPoint(self, A, N):
        if len(A) == 0:                                     # Empty arrays have no equilibrium points
            return -1
        
        elif len(A) == 1:                                   # Array with only 1 element have exactly 1 equilibrium point
            return 1
        
        left = 0                                            # Initializing 2 iterators, one starting from the first element and another one starting from the right
        right = N - 1
        sumLeft = A[left]                                   # Adding the elements into sums as we iterate through the array
        sumRight = A[right]                                  

        while left < right:                                 # Calculating until the iterators meet

            if sumLeft < sumRight:                          # If a sum is smaller than the other, we increment or decrement it depending on the case
                left += 1
                sumLeft += A[left]

            elif sumRight < sumLeft:
                right -= 1
                sumRight += A[right]

            elif sumRight == sumLeft and left != right:     # If the sums are equal but right and left don't meet we check for the next values of each iterator and we choose the smallest one
                if A[left + 1] < A[right - 1]:
                    left += 1
                    sumLeft += A[left]

                else:
                    right -= 1
                    sumRight += A[right]
                    
        
        if sumLeft == sumRight:                             # Iterators met but the sums are not equal = no equilibrium point
            return left + 1
            
        else: 
            return -1
    

ob = Solution()

print(ob.equilibriumPoint([20, 17, 42, 25, 32, 32, 30, 32, 37, 9, 2, 33, 31, 17, 14, 40, 9, 12, 36, 21, 8, 33, 6, 6, 10, 37, 12, 26, 21, 3], 30))

        
        
