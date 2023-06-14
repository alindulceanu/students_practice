#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        for ch in x:
            if ch in ('(', '{', '['):
                stack.append(ch)
            else:
                if stack and ((stack[-1] == '(' and ch == ')') or
                              (stack[-1] == '{' and ch == '}') or
                              (stack[-1] == '[' and ch == ']')):
                    stack.pop()
                else:
                    return False
        return not stack
    
#https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&status[]=unsolved&sortBy=submissions