#https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1?page=5&status[]=unsolved&sortBy=submissions

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        for i in range(len(A)):
            if A[i]==key:
                return i
        return -1