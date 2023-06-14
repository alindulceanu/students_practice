N = input("Generate an array of N elements: ")

def display():
    x = [] * int(N)
    for i in range(int(N) + 1):
        x.append(i)
    arr = [i for i in x if i != 0]
    return arr

print(display())

K = int(input("Split array into K subarrays: "))
arr = display()

def split_list(arr, K):
    max_num = max(arr)
    total_sum = sum(arr) 
    
    subarray_sum = total_sum // K
    
    if subarray_sum >= max_num:
        subarray_sum = max_num - 1 
    
    subarray = []
    temp = []
    current_sum = 0
    
    for num in arr:
        if current_sum + num <= subarray_sum:
            temp.append(num)
            current_sum += num
        else:
            subarray.append(temp)
            temp = [num]
            current_sum = num
    
    subarray.append(temp)
    
    return subarray

subarray = split_list(arr, K)
print(subarray)