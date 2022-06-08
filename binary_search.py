def binary_search(arr: list, item: int, low=None, high=None) -> int | None:
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_value = arr[middle]

        if middle_value == item:
            return middle

        if middle_value > item:
            return binary_search(arr, item, low, middle - 1)

        else:
            return binary_search(arr, item, middle + 1, high)

    return None


lst = [331, 893, 656, 176, 172, 104, 938, 202, 580, 620]
print(binary_search(lst, 580))
