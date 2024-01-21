def maxElement(arr, n):
    if n == 1:
        return arr[0]
    maxInteger = maxElement(arr, n -1)
    if arr[n] > maxElement(arr, n-1):
        maxInteger = arr[n]
    else:
        maxInteger = maxElement(arr, n -1)
print(maxElement([1, 2, 3, 4, 5], 4))