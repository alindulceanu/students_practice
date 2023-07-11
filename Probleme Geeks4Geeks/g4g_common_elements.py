'''Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?'''


class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i = 0                                           # Iterators for every array
        j = 0
        k = 0
        commonElements = []                             # Storing the common elements within the arrays
        
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k] and A[i] not in commonElements:     # Checking if the elements at every iterator are equal
                commonElements.append(A[i])
                
            if A[i] < B[j]:                                             # Comparing the values, the lesser one gets it's iterator incremented
                i += 1
            
            elif C[k] < B[j]:
                k += 1
                
            else:
                j += 1
                
        return commonElements