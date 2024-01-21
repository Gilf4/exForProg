arr = [1, 2, 3, 4, 5 ,6 ,7, 8, 10]
k = 5
# arr.pop(k)
arr = arr[:k] + arr[k+1:]
print(arr)