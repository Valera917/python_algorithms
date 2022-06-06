def bubble_sort(arr: list):
    list_length = len(arr)
    for i in range(0, list_length):
        for j in range(0, list_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test = [9, 7, -2, 4, 0]
print(bubble_sort(test))
