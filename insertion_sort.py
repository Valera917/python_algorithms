def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


test = [9, 7, -2, 4, 0]
print(insertion_sort(test))
