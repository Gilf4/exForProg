arr1 = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
arr2 = []
for i in range(len(arr1)):
    arr2.append(sum([arr1[int(i)] for i in range(0, i+1)]))
print(arr2)