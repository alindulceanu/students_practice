class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        sol = []
        for i in range(N):
            flag = False
            for j in range(i + 1, N):
                if not A[i] >= A[j]:
                    flag = True
                    break
            if flag == True:
                continue
            else:
                sol.append(A[i])
                
        return sol


    
#https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&status[]=unsolved&sortBy=submissions