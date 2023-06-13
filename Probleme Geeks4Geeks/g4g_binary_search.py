'''Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.'''

class Solution:	
    def binarysearch(self, arr, n, k):
        bot = 0
        top = n - 1

        while top >= bot:
            mid = (bot + top) // 2

            if arr[mid] == k:
                return mid

            elif arr[mid] > k:
                top = mid - 1

            else:
                bot = mid + 1

        return -1
    

ob = Solution()
print(ob.binarysearch([1,7,4,2,6,3], 6, 4))