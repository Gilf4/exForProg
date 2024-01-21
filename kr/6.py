arr1 = [1, 3 ,5 ,7, 9]
arr2 = [2, 4, 6, 8, 10]
result = []
for i in range(5):
    if arr1[i] == arr2[i]:
        result.append(arr1[i])
    if arr1[i] < arr2[i]:
        result.append(arr1[i])
        result.append(arr2[i])
    else:
        result.append(arr2[i])
        result.append(arr1[i])
print(result)