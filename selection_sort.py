def selection_sort(arr: list) -> list:
    for index, value in enumerate(arr):
        min_v = value
        min_idx = index
        for j in range(index + 1, len(arr)):
            if min_v > arr[j]:
                min_v = arr[j]
                min_idx = j

        if min_idx != index:
            arr[index], arr[min_idx] = arr[min_idx], arr[index]

    return arr


test = [-9, 5, 0, 1, -2]
print(selection_sort(test))
