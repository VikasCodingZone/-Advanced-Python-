# 9 Print all elements of a nested list

def print_list(lst):
    for item in lst:
        if isinstance(item, list):
            print_list(item)
        else:
            print(item)

print_list([1, [2, 3, [4, 5]], 6])


# Logic:

# Agar element list hai → andar ghus jao (recursive call)
# warna print karo.
# Ye real life me folder ke andar folder traverse jaisa hai.
