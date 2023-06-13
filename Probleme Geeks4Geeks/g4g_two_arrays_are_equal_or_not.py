'''Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.'''

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        self.__A = sorted(A)
        self.__B = sorted(B)
        
        if self.__A == self.__B:
            return True
            
        else:
            return False
        

