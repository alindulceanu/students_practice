N = input ("Generate an array of N elements: ")
def display():
    x = [] * int(N)
    for i in range(int(N)+1):
        x.append(i)
        arr=[i for i in x if i!=0]
    return arr
print (display())
K = int(input ("Split array into K subarrays: "))
arr = display()
def split_list(arr, K):
    return [arr[i:i + K] for i in range(0, len(arr), K)]
subarray = split_list(arr, K)
print(subarray)