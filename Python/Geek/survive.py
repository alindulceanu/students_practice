class Solution:
    def minimumDays(self, S, N, M):
        maxbuy = N
        days = 1
        if M > N:
            return -1
        elif N==M and S>=7:
            return -1
        elif ((N-M)*6)<M and S>=7:
            return -1
        else:
            while S > 0:
                for i in range(S):
                    if N < M:
                        N += maxbuy
                        days +=1
                    if N == 0:
                        N = N
                        days +=1
                    S -= 1
                    N -= M
        return days
    
#https://practice.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1?page=1&status[]=unsolved&category[]=Game%20Theory&category[]=Puzzles&sortBy=submissions