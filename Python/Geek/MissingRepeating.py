#https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?page=1&status[]=solved&sortBy=submissions

class Solution:
    def findTwoElement( self,arr, n): 
        repeat=sum(arr)-sum(set(arr))
        a=list(set(arr))
        a.sort()
        if ((a[-1] * (a[-1] + 1)) // 2)-(sum(a))==0:
            missing = a[-1]+1
        else:
            missing=((a[-1] * (a[-1] + 1)) // 2)-(sum(a))
        return [repeat, missing]