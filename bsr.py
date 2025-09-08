def binary_search_recursive(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, high, target)
        else:
            return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return -1

arr = [40, 20, 60, 40, 10]
arr.sort()
target = 30
print(arr)
print("Индекс элемента:", binary_search_recursive(arr, 0, len(arr) - 1, target))