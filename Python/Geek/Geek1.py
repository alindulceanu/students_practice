N = int(input("Enter the size of the array: "))

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

arr.sort()

print(arr)
print("Largest number is: ", arr[-1])
print("Second largest number is: ", arr[-2])