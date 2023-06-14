class Solution:
    def count(self, coins, N, Sum):
        sol = [0]*(Sum+1)
        sol [0] = 1
        
        for i in range(len(coins)):
            for j in range(1, Sum+1):
                if (j >=coins[i]):
                    sol[j] = sol[j] + sol[j-coins[i]]
        return sol[Sum]  
    
ob = Solution()
print(ob.count([1,2,3],3, 4))