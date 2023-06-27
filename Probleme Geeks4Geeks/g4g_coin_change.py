'''Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, 
find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. '''

class Solution:
    def count(self, coins, N, Sum):
        sums = [0 for i in range(Sum + 1)]
        sums[0] = 1
        
        for i in range(len(coins)):                         #Using Dynamic Programming to calculate all the possible sums 
            for j in range(1, Sum+1):                       #From 0 to Sum
                if j >=coins[i]:
                    sums[j] += sums[j-coins[i]]
        return sums[Sum]
    
ob = Solution()

assert ob.count([2,5,3], 3, 11) == 4
        