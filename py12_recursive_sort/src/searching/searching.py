# TO-DO: Implement a recursive binary search
def binary_search(arr, target, start, end):
    # base case if our array is []
    if end >= start:
        middle = (start + end) // 2  # floor division aka round down

        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            # shift start pointer to right of middle
            # effectively ignores left side of arr
            start = middle + 1
        else:
            # shift end pointer to left of middle
            # effectively ignores right side of arr
            end = middle - 1
        # recursive work
        return binary_search(arr, target, start, end)

    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    isAscending = arr[start] < arr[end]

    while start <= end:
        mid = (start + end) // 2  # floor division aka round down

        if target == arr[mid]:
            return mid

        if isAscending:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1  # not found
