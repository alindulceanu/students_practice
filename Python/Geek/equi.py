class Solution:
    def equilibriumPoint(self,A, N):
        s = []
        s.append(A[0])
        for i in range(1, len(A)):
            s.append(s[-1] + A[i])
        for i in range(len(A)):
            if(i == 0):
                if(s[-1] - s[i] == 0):
                    return i + 1
            elif(i == len(A) - 1):
                if(s[i - 1] == 0):
                    return i + 1
            else:
                if(s[i - 1] == s[-1] - s[i]):
                    return i + 1
        return -1

#https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&status[]=unsolved&sortBy=submissions