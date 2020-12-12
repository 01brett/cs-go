"""
Input: a List of integers
Returns: a List of integers
"""


# def moving_zeroes(arr):
#     if len(arr) < 2:
#         return arr
#     zeros = []
#     nums = []
#     for n in arr:
#         if n == 0:
#             zeros.append(n)
#         else:
#             nums.append(n)

#     return nums + zeros


def moving_zeroes(arr):
    if len(arr) < 2:
        return arr

    i = 0
    end = len(arr)

    while i < end:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            end -= 1
        else:
            i += 1

    return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation

    print(f"The resulting of moving_zeroes is: {moving_zeroes([0, 3, 1, 0, -2])}")
    print(f"The resulting of moving_zeroes is: {moving_zeroes([0, 0, 0, 0, 3, 2, 1])}")
