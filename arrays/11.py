arr = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,10]
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] = arr[i]*3
print(arr)