'''Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears more than N/2 times in the array.'''

class Solution:
    def majorityElement(self, A, N):
        index1 = {}                         # Dictionary to store the frequency of every element
        maxi = -1
        maxPos = -1 

        for i in range(N):
            if A[i] not in index1.keys():   # Adding values and frequencies of elements in A to the dictionary
                index1[A[i]] = 1

            else:
                index1[A[i]] += 1
                
                if index1[A[i]] > maxi:     # Storing the value with the highest frequency
                    maxi = index1[A[i]]
                    maxPos = i
                   
        if maxi > N/2:                      # Checking if the values with maximum frequency is a majority in the array
            return A[maxPos]
        
        else:
            return -1

ob = Solution

print(ob.majorityElement([3, 1, 3, 3, 2], 5))

