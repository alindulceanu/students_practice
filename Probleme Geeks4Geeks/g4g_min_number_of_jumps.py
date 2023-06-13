'''Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.'''

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
    

class Solution2:
    def minJumps(self, arr, n):
        front = 0
        back = 0
        while back != n - 1:
            front = back + arr[back] + 1
            for x in range(back + 1, front):
                if arr[x] + x > back:
                    back = arr[x] + x

            if back == front:
                return -1

                 

