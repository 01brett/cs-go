"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # grab max_val from first window
    m = max(nums[:k])
    result = [m]

    for i in range(1, len(nums) + 1 - k):
        # if incoming num is bigger than max,
        # set it to the incoming num
        if nums[i + k - 1] > m:
            m = nums[i + k - 1]
        # if outgoing num `was` max,
        # compute a new max from the new window
        elif nums[i - 1] == m:
            m = max(nums[i : i + k])
        # add current max_val to result array
        result.append(m)

    return result


# def sliding_window_max(nums, k):
#     ans = []
#     for i in range(len(nums) + 1 - k):
#         window = nums[i : i + k]
#         ans.append(max(window))
#     return ans


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}"
    )  # [3,3,5,5,6,7]
