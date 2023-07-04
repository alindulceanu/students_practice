class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        ans=0
        r=0
        l=0
        p=1
        while r < n:
            p *= a[r]
            while p >=  k and l <= r:
                p /= a[l]
                l += 1
            if l <= r:
                len = r-l+1
                ans += len
            r += 1
        return ans
    
#AM FOLOSIT O METODA *DENUMITA* SLIDING WINDOW
#https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1