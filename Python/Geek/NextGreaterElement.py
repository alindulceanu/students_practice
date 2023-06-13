class Solution:
    def nextLargerElement(self,arr,n):
        ans = [-1]
        result = []
        for i in arr[::-1]:
            if i < ans[-1]:
                result.append(ans[-1])
                ans.append(i)
            else :
                while ans[-1] != -1 and ans[-1] <= i :
                    ans.pop()
                result.append(ans[-1])
                ans.append(i)
        result.reverse()
        return result

#https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1?page=1&status[]=solved&sortBy=submissions