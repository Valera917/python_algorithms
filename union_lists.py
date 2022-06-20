def union_sort(arr_1, arr_2):
    result = []
    len_1, len_2 = len(arr_1), len(arr_2)
    i = j = 0

    while i < len_1 and j < len_2:
        if arr_1[i] <= arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1

    result += arr_1[i:] + arr_2[j:]
    return result


first = [1, 4, 10, 11]
second = [2, 3, 3, 4, 8]
print(union_sort(first, second))
