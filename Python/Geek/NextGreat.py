#https://practice.geeksforgeeks.org/problems/214734e358208c1c6811d9b237b518f6b3c3c094/1?page=1&status[]=solved&sortBy=submissions

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