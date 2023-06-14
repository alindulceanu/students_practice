class dp:
    def fib(self, n, memo = {}):
        if n == 0 or n == 1:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]

    def fibBottomUp(self, n):
        if n == 0 or n == 1:
            return n
        
        bottomUp = [None for i in range(n + 1)]

        bottomUp[0] = 0
        bottomUp[1] = 1

        for i in range(2, n + 1):
            bottomUp[i] = bottomUp[i - 1] + bottomUp[i - 2]

        return bottomUp[n]


ob = dp()
print(ob.fibBottomUp(9999))

