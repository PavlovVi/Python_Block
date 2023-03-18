def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

# Пример
arr = [2, 5, 8, 3, 6, 1, 4, 7]
min_val = 3
max_val = 6
result = find_indexes(arr, min_val, max_val)
print(result) 
