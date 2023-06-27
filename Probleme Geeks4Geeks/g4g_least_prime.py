'''Given a number N, find the least prime factors for all numbers from 1 to N.  \
The least prime factor of an integer X is the smallest prime number that divides it.
Note :
1 needs to be printed for 1.
You need to return an array/vector/list of size N+1 and need to use 1-based indexing to store the answer for each number.'''

class Solution:
    def leastPrimeFactor (n):
        primes = [0 for i in range(n + 1)]                  #Making a list of zeroes for every value from 0 to n
        primes[1] = 1                                       
        p = 2                                               #P will be our count for prime numbers

        while p ** 2 <= n:                                 
            if primes[p] == 0:                              #Checking if the current slot for p in the primes list is empty
                for i in range(p ** 2, n + 1, p):           #Adding p to itself until we reach the latest value
                    if primes[i] == 0:                      #If the current index is empty, we replace it with p
                        primes[i] = p
            p += 1                                          #Incrementing p for every while loop
    
        for i in range(2, n+1):                             #After the while loop, the prime numbers will have an empty index
            if primes[i] == 0:                              #So we will fill them with themselves
                primes[i] = i
    
        return primes
    
ob = Solution
print(ob.leastPrimeFactor(100))

