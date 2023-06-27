'''Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".'''


class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []                                          #  Initializing a stack to hold the paranthesis in order

        par = {')' : '(', ']' : '[', '}' : '{'}             # A dicionary that pairs the paranthesis

        if len(x) % 2 != 0:                                 # It can't be balanced it the number of paranthesis is odd
            return 0

        for i in x:                                         # Iterates through x
            if i in par.values():                           # Paranthesis openers are stocked in the values of the dictionary
                stack.append(i)                             # So we add them in the stack
                continue

            if i in par.keys():                             
                val = par[i]                                # val is the value par[i] should have to make 'x' balanced

                try:                                        # Use try because if there are more paranthesis ends than openers you will get an iteration error
                    if stack[-1] == val:                    # Check if they are the same, if not = unbalanced
                        stack.pop()

                    else:
                        return 0
                    
                except:
                    return 0
                
            else:
                return 0
        
        return 1                                            # If everything was fine, 'x' is balanced

ob = Solution()

print(ob.ispar(['{', '(', '[', ']', ')', '}']))
        
