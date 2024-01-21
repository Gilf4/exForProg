import random
arr = [random.randint(1,25) for __ in range(int(input()))]
localMax = -100000
for i in range(1, len(arr)-1):
    if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
        localMax = max(localMax, arr[i])
print(arr, localMax)
