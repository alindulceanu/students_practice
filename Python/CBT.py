while True:

    Selector = input("Run: (r) / Quit: (q) ")

    if Selector != "q" and Selector != "r":
        print("Invalid operation!")

    if Selector == "q":
        break

    if Selector == "r":

        def find_minimum_string(N, K):

            numbers = []
            for i in range(K**N):
                number = base_K(i, K, N)
                numbers.append(number)

            sorted_numbers = sorted(numbers)

            final_string = "".join(sorted_numbers)

            return final_string

        def base_K(num, base, length):
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            digits.extend(['0'] * (length - len(digits)))
            return ''.join(digits[::-1])

        N = int(input("Enter the value of N: "))
        K = int(input("Enter the value of K: "))

        result = find_minimum_string(N, K)
        print(result)