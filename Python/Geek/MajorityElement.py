class Solution:
    def majorityElement(self, A, N):
        Map = dict()
        
        for i in A:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i] += 1
        
        for key, value in Map.items():
            if value > N // 2:
                return key
        return -1
    
    #https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&status[]=solved&sortBy=submissions