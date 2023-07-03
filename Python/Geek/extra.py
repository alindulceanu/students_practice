

class Solution:
    
    def merge(self,arr1,arr2,n,m):
        i=n-1
        j=0
        while i>=0 and j<m:
            if arr1[i]>arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
                i-=1
                j+=1
            else:
                break
        arr1.sort()
        arr2.sort()
        return(arr1,arr2)
    
#https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1?page=3&status[]=solved&sortBy=difficulty