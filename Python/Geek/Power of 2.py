N = int(input("Number of be checked: "))

def is_power_of_two(N):
    if N == 0:
        return False
    if N == 1:
        return True
    K = 0
    while N > 1:
        K += 1
        if N % 13 != 0:
            return False
        N = N // 13
    return K


print(is_power_of_two(N))