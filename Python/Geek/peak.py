class Solution:   
    def peakElement(self,arr, n):
        min = 0
        max = n - 1
        while min <= max:
            mid = (min + max) // 2
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                max = mid - 1
            else:
                min = mid + 1
        return 0
    
#https://practice.geeksforgeeks.org/problems/peak-element/1?page=1&status[]=unsolved&sortBy=submissions