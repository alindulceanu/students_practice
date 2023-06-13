N = int(input("Number of elements: "))

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
    sum(arr)