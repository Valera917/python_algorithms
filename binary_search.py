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


lst = [0, 12, 35, 89, 134, 205, 206, 345, 512, 1024]
print(binary_search(lst, 35))
