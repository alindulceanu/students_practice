#include <iostream>
#include <climits>

using namespace std;



class Solution{
    public:

        long long maxSubarraySum(int arr[], int n){
            long long maxSum = INT_MIN;
            long long sum = 0;
            
            for(int i = 0; i < n; i++){
                sum += arr[i];
                
                if(sum > maxSum)
                    maxSum = sum;
                
                if(sum < 0)
                    sum = 0;
                    
                
            }
                
            return maxSum;
        
    }
};

int main(){

    int n = 5;
    int a[] = {1, 4, 1, 5, 6};

    Solution ob;

    cout << ob.maxSubarraySum(a,n);
        
    return 0;
}
