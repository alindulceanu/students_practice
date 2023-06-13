while True:

    Selector = input("Choose case: Case1(simple) / Case2(complex) / q to quit: ")

    if Selector != "q" and Selector != "Case1" and Selector != "Case2":
        print("Invalid choice!")

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

        N = int(input("Enter the number of elements in the array: "))

        def get_array_input():
            arr = []
            print("Enter the elements of the array:")
            for _ in range(N):
                element = int(input())
                arr.append(element)
            return arr

        def display():
            arr = get_array_input()
            return arr

        arr = display()

        K = int(input("Enter the number of subarrays to split the array into: "))

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
            
            if temp:
                subarray.append(temp)
            
            if sum(subarray[-1]) > subarray_sum:
                last_subarray = subarray.pop()
                for num in last_subarray:
                    subarray.append([num])
            
            return subarray

        subarray = split_list(arr, K)
        print("Split Subarrays:")
        for i, sub in enumerate(subarray):
            print("Subarray", i + 1, ":", sub)
        print()