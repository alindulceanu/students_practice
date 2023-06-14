N = int(input("Enter the value of N: "))
K = int(input("Enter the value of K: "))

def is_valid(N, K, max_sum):
    subarray_count = 1
    current_sum = 0
    subarray_splits = []
    
    for num in range(1, N+1):
        if current_sum + num > max_sum or K - subarray_count > N - num:
            subarray_count += 1
            subarray_splits.append(current_sum)
            current_sum = num
        else:
            current_sum += num
    
    subarray_splits.append(current_sum)
    
    return subarray_count <= K, subarray_splits

def split_array(N, K):
    start = 1
    end = N * (N + 1) // 2
    result = float('inf')
    split_result = []
    
    while start <= end:
        mid = (start + end) // 2
        
        valid, splits = is_valid(N, K, mid)
        
        if valid:
            result = mid
            split_result = splits
            end = mid - 1
        else:
            start = mid + 1
    
    return result, split_result

minimum_max_subarray_sum, array_splits = split_array(N, K)

print("The minimum possible maximum subarray sum is:", minimum_max_subarray_sum)
print("Array Split:")
for i in range(len(array_splits) - 1):
    print(array_splits[i+1] - array_splits[i], end=" ")
print()






