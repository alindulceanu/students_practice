N = int(input("Enter number of elements: "))
test_list = []
for i in range(N):
    test_list.append(int(input("Elements of the list: ")))
print(test_list)

def group_elements(lst):
    grouped_dict = {}
    for element in lst:
        if element in grouped_dict:
            grouped_dict[element].append(element)
        else:
            grouped_dict[element] = [element]
    return grouped_dict

result = group_elements(test_list)
print(result)