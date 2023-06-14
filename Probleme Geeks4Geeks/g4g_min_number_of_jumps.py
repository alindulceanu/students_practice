'''Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.'''
import time
import pytest

#User function Template for python3
class Solution:
    def __init__(self):
        self.count = 0
        
    def minJumps(self, arr, n, i = 0):        #Backtracking
        if i >=  n:
            return -1
        
        if arr[i] == 0:
            return -1
            
        if i == n - 1:
            return self.count
        
        jumpLimit = arr[i]
        for x in reversed(range(1, jumpLimit + 1)):

            self.count += 1
            if self.minJumps(arr, n, i + x) == self.count:
                return self.count
            
            self.count -= 1
            
        return -1
    
    def minJumps2(self, arr, n):
        front = 0
        back = 0
        count = 1
        while back <= n:
            front = back + arr[back] + 1
            if front > n:
                front = n
            for x in range(back + 1, front):
                if arr[x] + x > back:
                    back = arr[x] + x

            if back == front:
                return -1
            count += 1
            
        return count
    
    def minJumps3(self, arr, n): #gasita in comments
	    #code here
        jumps = 0 
        curr_idx = 0 
        
        while curr_idx != n-1:
            # got zero and haven't reached end
            if arr[curr_idx] == 0 and curr_idx != n-1:
                return -1 
            
            # this number will be able to take you to the end 
            if n-1 <= arr[curr_idx] + curr_idx:
                jumps += 1
                break; 
                
            range_start = curr_idx + 1
            range_end = min(n-1, range_start + arr[curr_idx])
            
            range_max = -1
            max_val = 0
            step = 0
            for idx in range(range_start, range_end):
                step_val = arr[idx] + step
                if step_val >= max_val:
                    range_max = idx
                    max_val = step_val
                step += 1 
                    
            jumps += 1
            curr_idx = range_max

        return jumps 
            
start = time.time()
ob = Solution()
print(ob.minJumps3([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))
end = time.time()

print(end - start)

                 

