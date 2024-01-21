arr = [1 ,2 ,3, 5 ,6 ,7, 8, 9]
arr = sorted(arr)
counter = 1
failedElement = 0
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] == 1:
        counter += 1
    else:
        failedElemnt = i
        print(f'err in {failedElement} element')
        break
if counter == len(arr):
    print('All good')
