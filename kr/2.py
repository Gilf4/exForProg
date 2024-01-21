arr = [1, 2, 4, 5]
flag = 0
errorValue = 0
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] != 1:
        flag = 1
        errorValue = arr[i+1]
if flag == 0:
    print('True')
else:
    print('False', errorValue)
