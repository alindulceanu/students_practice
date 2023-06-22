#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        count= 0
        for i in range(n):
            for j in range(i+1, n):
                if ((arr[i]-arr[j])%k)==0:
                    count=count+1

        return count

#https://practice.geeksforgeeks.org/problems/e0059183c88ab680b2f73f7d809fb8056fe9dc43/1?page=1&status[]=unsolved&sortBy=submissions