M = int(input())
N = int(input())
numbers = [int(input()) for i in range(N)]

matrix = [[0 for j in range(N)] for i in range(M)]

for i in range(M):
    for j in range(N):
        matrix[i][j] = numbers[i]

for row in matrix:
    print(row)
