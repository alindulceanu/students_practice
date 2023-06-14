N = int(input("Enter the value of N: "))
arr = []
for _ in range(N):
    arr.append(int(input("Enter element: ")))
K = int(input("Enter the value of K: "))

def is_valid(arr, K, max_sum):
    subarray_count = 1
    current_sum = 0
    subarray_splits = []
    
    for num in arr:
        if current_sum + num > max_sum or K - subarray_count > len(arr) - arr.index(num):
            subarray_count += 1
            subarray_splits.append(current_sum)
            current_sum = num
        else:
            current_sum += num
    
    subarray_splits.append(current_sum)
    
    return subarray_count <= K, subarray_splits

def split_array(arr, K):
    start = max(arr)
    end = sum(arr)
    result = float('inf')
    split_result = []
    
    while start <= end:
        mid = (start + end) // 2
        
        valid, splits = is_valid(arr, K, mid)
        
        if valid:
            result = mid
            split_result = splits
            end = mid - 1
        else:
            start = mid + 1
    
    return result, split_result

minimum_max_subarray_sum, array_splits = split_array(arr, K)

print("The minimum possible maximum subarray sum is:", minimum_max_subarray_sum)
print("Array Split:")
for i in range(len(array_splits) - 1):
    print(array_splits[i+1] - array_splits[i], end=" ")
print()