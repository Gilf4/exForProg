matrix = [[5, 2, 3], [4, 10, 6], [3, 4, 9]]
K = 3

row = matrix[K-1]
sum = 0
proz = 1
for element in row:
    sum += element
    proz *= element
print(sum, proz)