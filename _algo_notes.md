# Problem you'll see in interviews

Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.

## Example outputs

```python
centered_average([1, 2, 3, 4, 100]) # -> 3
centered_average([1, 1, 5, 5, 10, 8, 7]) # -> 5
centered_average([-10, -4, 2, -4, -2, 0]) # -> -3
```

# Plan Your Approach

Assume at least 3 items in the array
if there are repeats, ignore only one

## Using examples to understand desired result

1, 5, 5, 8, 7
Double slash is called floor division (round down)

```python
26 // 5 = 5
```

## Most readable (best approach for 1st pass)

```python
def centered_average(arr):
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr) // len(arr)
```

## Most computationally efficient

```python
def centered_average(arr):
    # walk thru the arr and sum each value,
    # keeping track of low and high values
    total = 0
    low = float("inf")
    high = -float("inf")

    for n in arr:
        if n < low:
            low = n
        if n > high:
            high = n
        total += n

    # subtract low and high from sum and dived by length - 2
    return (total - low - high) // (len(arr) - 2)
```
