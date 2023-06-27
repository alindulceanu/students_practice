'''Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it
 is greater than or equal to all the elements to its right side. The rightmost element is always a leader. '''


class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        maxi = -1
        leaders = []
        for i in range(N - 1, -1 , -1):            #We count from the last element to the first one
            if A[i] >= maxi:                       #We compare the current value to the maximum value found yet, if it is bigger
                maxi = A[i]                        #we add that value to the leaders list and update the maximum value
                leaders.append(A[i])

        return leaders[::-1]

