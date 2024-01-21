import random
arr = [random.randint(1,25) for __ in range(int(input()))]
print(arr)
counter = 0
f = 0
for i in range(len(arr)):
    if arr[i] < arr[i-1]:
        f = 1
    if arr[i] > arr[i-1] and f == 1:
        counter += 1
        f = 0
print(counter)
        

    