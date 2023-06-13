while True:

    Selector = input("Choose case: Case1(simple) / Case2(complex) / q to quit: ")

    if Selector == "q":
        break

    if Selector == "Case1":

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

    if Selector == "Case2":

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

        split_lengths = [array_splits[i+1] - array_splits[i] for i in range(len(array_splits) - 1)]
        highest_number = max(arr)

        for length in split_lengths:
            if length > highest_number:
                print(highest_number, end=" ")
                length -= highest_number

            while length > 0:
                print(min(length, highest_number), end=" ")
                length -= highest_number

        print()
    print()