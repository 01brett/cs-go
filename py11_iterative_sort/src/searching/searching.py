def linear_search(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # floor division aka round down
        mid = (right + left) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            # toss out the left side of array including mid element
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found
