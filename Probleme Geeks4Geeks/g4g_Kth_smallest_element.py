'''Given an array arr[] and an integer K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.'''

class Solution:
    def kthSmallest(self,arr, l, r, k):         #Self explanatory
        arr.sort()
        
        return arr[k - 1]