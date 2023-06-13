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

def get_array_input2():
    arr2 = []
    print("Enter the elements of the array:")
    for _ in range(N):
        element2 = int(input())
        arr2.append(element2)
    return arr2

def display():
    arr2 = get_array_input2()
    return arr2

arr = display()
arr2 = display()

arr.sort()
arr2.sort()

print(arr)
print(arr2)

if arr == arr2:
    print ("Equal")
else:
    print ("Not equal")