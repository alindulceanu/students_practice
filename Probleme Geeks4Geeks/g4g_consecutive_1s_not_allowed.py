'''Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer modulo 10^9 + 7.'''

class Solution:      #Merge pana la n = 43 lol
                     #Fibonacci

    def countStrings(self,n):
        last = 1
        current = 1

        for i in range(n):
            x = current
            current += last
            last = x

        return current
    
    def countString(self,n): #  
        pass

    
ob = Solution()
print(ob.countStrings(10))


