'''Given a sorted array of size N and an integer K, 
find the position(0-based indexing) at which K is present in the array using binary search.'''

class Solution:	
    def binarysearch(self, arr, n, k):
        bot = 0
        top = n - 1

        while top >= bot:
            mid = (bot + top) // 2          # Mid is the value between top and bot and is recalculated every iteration

            if arr[mid] == k:               # If mid reaches the value K, we return mid
                return mid

            elif arr[mid] > k:              # If mid is greater than K, we move top to mid - 1
                top = mid - 1               # the reason being that K will not be found from mid to top in this case

            else:
                bot = mid + 1               # Same thing if mid is lesser than K, we move bot to mid + 1 

        return -1                           
    

ob = Solution()
print(ob.binarysearch([1,7,4,2,6,3], 6, 4))