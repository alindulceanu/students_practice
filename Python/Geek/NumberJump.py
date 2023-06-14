class Solution:
	def minJumps(self, arr, n):
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

    
#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&status[]=solved&sortBy=submissions