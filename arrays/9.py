arr = [1, 2, 3, 4, 4, 4, 1, 2, 5, 5]
arr = arr + [arr[-1] + 1]
result = []
f = 0
counter = 1
for i in range(len(arr) - 1):
    if arr[i] == arr[i+1]:
        f = 1
        counter += 1
    if arr[i] != arr[i+1] and f == 1:
        result.append([counter, arr[i]])
        counter = 1
        f = 0
print(result)
