def merge_lists(arr_1: list, arr_2: list) -> list:
    """Function that merges two sorted lists"""
    res = []
    len_1 = len(arr_1)
    len_2 = len(arr_2)

    i = 0
    j = 0
    while i < len_1 and j < len_2:
        if arr_1[i] <= arr_2[j]:
            res.append(arr_1[i])
            i += 1
        else:
            res.append(arr_2[j])
            j += 1

    res += arr_1[i:] + arr_2[j:]
    return res


def split_and_merge(array: list) -> list:
    delimiter = len(array) // 2
    first_part = array[:delimiter]
    second_part = array[delimiter:]

    if len(first_part) > 1:
        first_part = split_and_merge(first_part)
    if len(second_part) > 1:
        second_part = split_and_merge(second_part)

    return merge_lists(first_part, second_part)


test = [9, 0, -5, 3, 1, 6]
print(split_and_merge(test))
