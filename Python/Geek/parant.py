class Solution:
    def maxLength(self, S):
        n = len(S)
        dp = [0]*(n+1)
        st = []
        for i in range(n):
            if S[i]=='(':
                st.append(i)
            else:
                if st:
                    b = st.pop()
                    dp[i] = i-b+1+dp[b-1]
                    
        return max(dp)    
    
#https://practice.geeksforgeeks.org/problems/longest-valid-parentheses5657/1?page=1&status[]=solved&sortBy=latest