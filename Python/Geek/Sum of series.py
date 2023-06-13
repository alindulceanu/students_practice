N = int(input("N terms: "))
total = 0
global arr
global result

def display():
    x = [] * int(N)
    for i in range(int(N) + 1):
        x.append(i)
    arr = [i for i in x if i != 0]
    return arr

def result():
    for element in range(0, len(arr)):
        result = total + arr[element]
    return result

print("Sum of all elements is: ", result())