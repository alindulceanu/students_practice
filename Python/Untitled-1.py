def split_list(lst, n):
    """Split a list into sublists containing n elements."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3  # Number of elements per sublist

sublists = split_list(lst, n)

print(sublists)