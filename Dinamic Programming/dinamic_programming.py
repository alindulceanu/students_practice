import time
import sys

sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(99999999)

class dp:
    def fib(self, n, memo = {}):
        if n == 0 or n == 1:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
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
    
    def fib_iter(self, n):
        current = 1
        last = 0

        for i in range(n - 1):
            x = current
            current += last
            last = x

        return current

start = time.time()
ob = dp()
print(ob.fib_iter(100000), "\n")
print(str(time.time() - start) + "s")


#TIMETABLE

#fib(10000) - 0.008335113525390625s
#fibBottomUp(10000) - 0.006401538848876953s
#fib_iter(10000) - 0.004000186920166016s

#fib(100000) - 0.18917226791381836s
#fibBottomUp(100000) - 0.2032630443572998s
#fib_iter(100000) - 0.08015084266662598s

#fib_iter Best time