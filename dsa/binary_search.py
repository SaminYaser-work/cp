def binary_search(arr, target):
    if len(arr) == 0:
        return False
    m = len(arr) // 2
    if arr[m] == target:
        return True
    return binary_search(arr[m+1:len(arr)], target) if target > arr[m] else binary_search(arr[0:m], target)


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    print(binary_search(arr, -1))
