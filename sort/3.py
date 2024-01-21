from random import *
arr = []
for i in range(10):
    arr.append(randint(1,100))
print(arr)
for i in range(1, len(arr)):
    buffer = arr[i]
    j = i - 1
    while j >= 0 and buffer < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = buffer
print(arr)
