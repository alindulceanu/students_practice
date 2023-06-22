'''Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.'''


class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[-1] - arr[0]
    
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            max_ = max(arr[i-1] + k, arr[-1] - k)
            min_ = min(arr[i] - k, arr[0] + k)
            ans = min(ans, max_ - min_)
        return ans


ob = Solution()
print(ob.getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5))