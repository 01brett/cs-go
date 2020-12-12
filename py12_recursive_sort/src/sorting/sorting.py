# break down the arr into smaller chunks using a `pivot`
# helper function to partition the input array
def partition(arr):
    # pick a pivot (1st el in this case)
    pivot = arr[0]
    left = []
    right = []

    # partition the elements around the pivot
    for el in arr[1:]:
        if el <= pivot:
            left.append(el)
        else:
            right.append(el)

    # we have el partitioned in left, pivot, and right arrays
    return left, pivot, right


def quicksort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # call partition() to breakup our inputs
    left, pivot, right = partition(arr)  # Python destructuring

    # concatenates our arrays together
    # [pivot] just places our pivot val into an arr to allow arr concatenation
    return quicksort(left) + [pivot] + quicksort(right)


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # use AND b/c as soon as an arr is empty, then we just append the other /sorted/ arr to the list
    while len(arrA) >= 1 and len(arrB) >= 1:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    return merged_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case
    if len(arr) < 2:  # arr of 1 is sorted
        return arr

    mid = len(arr) // 2
    left = arr[:mid]  # excludes mid element
    right = arr[mid:]  # includes mid element

    return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, left, right):
    if left < right:  # arr of 1 is sorted
        # Same as (left + right) / 2, but avoids overflow for large left and right
        mid = left + (right - left) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, left, mid)
        merge_sort_in_place(arr, mid + 1, right)

        merge_in_place(arr, left, mid, right)
