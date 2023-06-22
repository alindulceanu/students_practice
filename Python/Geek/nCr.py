import math

class Solution:
    def nCr(self, n, r):
        mod = 10**9+7
        if n==r:
            return 1
        a = math.factorial(n)
        b = math.factorial(r)
        if n>r:
            c = math.factorial(n-r)    
            return (a//(b*c))%mod
        return 0
    
#https://practice.geeksforgeeks.org/problems/ncr1019/1?page=1&status[]=solved&sortBy=latest