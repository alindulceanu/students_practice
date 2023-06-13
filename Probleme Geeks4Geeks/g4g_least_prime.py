class Solution:
    def leastPrimeFactor (n):
        primes = [0 for i in range(n + 1)]
        primes[1] = 1
    
        p = 2
        while p ** 2 <= n:
            if primes[p] == 0:
                for i in range(p ** 2, n + 1, p):
                    if primes[i] == 0:
                        primes[i] = p
            p += 1
    
        for i in range(2, n+1):
            if primes[i] == 0:
                primes[i] = i
    
        return primes
    
ob = Solution
print(ob.leastPrimeFactor(100))

