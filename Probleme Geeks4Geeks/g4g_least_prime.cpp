#include <iostream>
using namespace std;

class Solution {
public:
    int* leastPrimeFactor(int n) {
        int* primes = new int[n + 1];
        primes[0] = 0;
        primes[1] = 1;

        for (int i = 2; i <= n; i++)
                primes[i] = i;

        int p = 2;

        while (p * p <= n) {
            if (primes[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (primes[i] == i)
                        primes[i] = p;
                }
            }
            p += 1;
        }
        return primes;
    }
};


int main() {
    Solution ob;
    int N = 500;
    int* result = ob.leastPrimeFactor(N);
    for (int i = 1; i <= N; i++) 
        cout << result[i] << " ";
    
    delete[] result;
    return 0;
}
