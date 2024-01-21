maxValue = 0
value = 0
arr = list(map(str, [1, 2, 3, 4, 5 ,6 ,7 ,8, 8 ,9]))
set = set(arr)
for i in set:
    if arr.count(str(i)) > maxValue:
        maxValue = arr.count(str(i))
        value = i
print(value, maxValue)
