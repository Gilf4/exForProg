arr = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,0]
maxSum = 0
index = [0, 0]
for i in range(len(arr) - 1):
    if arr[i] + arr[i+1] > maxSum:
        maxSum = arr[i] + arr[i+1]
        index = [i, i+1]
print(index, maxSum)
