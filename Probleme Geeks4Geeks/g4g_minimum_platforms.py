'''Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.'''

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        setA = set()                    # Defining the sets in which the values of a and b arrays will be added
        setB = set()
        
        for i in a:
            setA.add(i)
            
        for i in b:
            setB.add(i)
            
        return len(setA.union(setB))    # Using the set method "union" to find how many unique values do the arrays have in total

