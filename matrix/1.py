M = int(input())
N = int(input())

matrix = [[10 * i for j in range(N)] for i in range(1, M+1)]

for row in matrix:
    print(row)