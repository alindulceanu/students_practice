'''Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, 
compute how much water can be trapped between the blocks during the rainy season. '''


'''
class Solution:
    def __init__(self):
        self.water = 0
        self.hypotheticWater = {}

    def trappingWater(self, arr,n):
        save1 = -1
        save2 = -1

        for i in range(n):
            if arr[i] != 0 and save1 == -1:
                save1 = i
            elif arr[i] != 0 and save2 == -1:
                save2 = i

            if save1 != -1 and save2 != -1:
                self.waterArea(save1, save2, arr)
                save1 = save2
                save2 = -1

        return self.water

    def waterArea(self, x, y, array):
        maxi = max(array[x], array[y])

        area = maxi * abs(y - x + 1)

        area = area - array[x] - array[y] - (abs(array[x] - array[y]) * abs(y - x))

        self.water += area

        hyphotheticArea = (abs(array[x] - array[y]) * (y - x))

        self.hypotheticWater[x] = 



ob = Solution()

print(ob.trappingWater([1, 0, 3, 0, 3, 0, 2], 7))
'''

'''
class Solution:
    def trappingWater(self, arr, n):
        lMax = arr[0]
        rMax = arr[n - 1]

        lValues = []
        rValues = []
        water = 0

        for i in range(n):
            if arr[i] > lMax:
                lMax = arr[i]
            lValues.append(lMax - arr[i])

            if arr[n - i - 1] > rMax:
                rMax = arr[n - i - 1]
            rValues.app(rMax - arr[n - i - 1])

        for i in range(n):
            water += min(lValues[i], rValues[-i])

        return water
    
ob = Solution()

print(ob.trappingWater([8, 8, 2, 4, 5, 5, 1], 7))
            '''

class Solution:
    def trappingWater(self, height, n):
        left = 0                                                # We start 2 iterators, one from the left and one from the right
        right = n - 1
        maxLeft = maxRight = waterTrapped = 0                   # We store the max values each iterator meets in its path
    
        while left <= right:                                    # Do this until the left and right iterators meet
            if height[left] <= height[right]:                   
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    waterTrapped += maxLeft - height[left]      # The trapped water will be the difference between the maxheighht found by this iterator - the current height
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    waterTrapped += maxRight - height[right]
                right -= 1
    
        return waterTrapped
    

ob = Solution()
print(ob.trappingWater([8, 8, 2, 4, 5, 5, 1], 7))

        

