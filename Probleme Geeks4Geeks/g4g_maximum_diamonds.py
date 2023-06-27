'''There are N bags with diamonds in them. The i'th of these bags contains A[i] diamonds. If you drop a bag with 
A[i] diamonds, it changes to A[i]/2 diamonds and you gain A[i] diamonds. Dropping a bag takes 1 minute.
 Find the maximum number of diamonds that you can take if you are given K minutes.'''
from sortedcontainers import SortedList

class Solution:
    def maxDiamonds(self, A, N, K):
        diamonds = 0
        for i in range(K):
            diamonds += max(A)                                      # We add the value of the biggest bag of diamonds in our collection
            A[A.index(max(A))] = int(A[A.index(max(A))] / 2)        # Then, we halve that bag

        return diamonds
    
ob = Solution()
print(ob.maxDiamonds([2,1,7,4,2], 5, 3))

class Solution2:                                #Same thing but we use the SortedList from sortedcontainers library which is faster
    def maxDiamonds(self, A, N, K):
        diamonds = 0

        A = SortedList(A)
        for i in range(K):
            d = A.pop()
            diamonds += d
            A.add(d // 2)
            
        return diamonds
    
ob2 = Solution2()
print(ob2.maxDiamonds([2,1,7,4,2], 5, 3))

            
                

