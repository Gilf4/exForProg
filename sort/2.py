from random import *
arr = []
for i in range(10):
    arr.append(randint(1,100))
print(arr)
for i in range(len(arr)):
    min_el = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_el]:
            min_el = j
    arr[min_el], arr[i] = arr[i], arr[min_el]
print(arr)