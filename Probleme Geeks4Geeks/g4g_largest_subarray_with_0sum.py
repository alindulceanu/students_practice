'''Given an array having both positive and negative integers. 
The task is to compute the length of the largest subarray with sum 0.'''

class Solution:
    def maxLen(self, n, arr):
        i = -1
        sum = 0
        maxLeng = 0
        sumMap = {}                             # Initializing a hashmap

        sumMap[sum] = i                         # Use the value of sum as key and the index as value

        while i < n - 1:
            i += 1  
            sum += arr[i]   

            if sum not in sumMap.keys():        # If a specific sum ever repeats, it means that the values between those sums equals to 0
                sumMap[sum] = i                 # Adding the sum in the hashmap if it's not already there

            else:
                leng = i - sumMap[sum]          # Calculating the length of elements in the sum
                                                
                if leng > maxLeng:              # Checking if it's the greatest length
                    maxLeng = leng

        return maxLeng
        
    
n = 84
arr = list(map(int, '-776 794 387 -648 363 691 764 -539 -171 -210 -566 783 -861 68 930 -21 -68 394 -10 -228 422 785 199 -314 -412 -90 -955 863 -995 306 85 337 847 314 125 583 815 435 -42 -86 -275 -787 -402 755 933 -675 -738 -225 -93 796 -433 -466 98 -316 -651 -300 -285 866 445 441 32 98 482 710 568 -496 587 307 220 -527 733 504 271 -707 341 797 619 847 922 380 -763 -840 -192 -33'.strip().split()))
ob = Solution()

print(ob.maxLen(n, arr))
