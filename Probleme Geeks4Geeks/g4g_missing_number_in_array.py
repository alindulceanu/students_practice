'''Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.'''


class Solution:
    def missingNumber(self,array,n):
        return list({i for i in range(1, n+1)}.difference(set(array)))[0]
    
ob = Solution()

print(ob.missingNumber([6,1,2,8,3,4,7,10,5], 10))