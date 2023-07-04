class Solution{
public:	
	// Function returns the second
	// largest elements
	int print2largest(int arr[], int n) {
	    sort(arr, arr + n);
	    int maxi = arr[n - 1];
	    int second = arr[n - 1];
	    int i = n - 1;
	    
	    while (second == maxi){
	        i--;
	        second = arr[i];
	        
	        if (i == 0 && second == maxi)
	            return -1;
	    }
	    return second;
	}
};

#https://practice.geeksforgeeks.org/problems/second-largest3735/1?page=1&difficulty[]=-2&sortBy=submissions