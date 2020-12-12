# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if len(arr) < 2:
        return arr
    # this loop essentially moves the boundary
    for i in range(0, len(arr) - 1):
        smallest_idx = i
        # find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j
        # Python's handy "swap" syntax
        arr[smallest_idx], arr[i] = arr[i], arr[smallest_idx]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        # we do len(arr) - 1 so that we stop just before the last ele
        # then when we do the compare, the last value is in range
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    if len(arr) < 1:
        return arr

    if maximum is None:
        maximum = max(arr)

    counter = [0 for _ in range(maximum + 1)]

    for val in arr:
        if val < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counter[val] += 1

    sorted_arr = []

    for idx, count in enumerate(counter):
        sorted_arr.extend([idx for _ in range(count)])

    return sorted_arr
