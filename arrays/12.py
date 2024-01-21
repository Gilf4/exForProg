arr = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12, 13]
k = 5
m = 2
arr = arr[:k] + [0] * m + arr[k:]
print(arr)
