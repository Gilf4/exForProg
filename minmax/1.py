N = int(input())
numbers = [int(input()) for i in range(N)]

# Найдите количество элементов, расположенных перед первым минимальным элементом
min_index = 0
for i in range(1, N):
    if numbers[i] < numbers[min_index]:
        min_index = i

print("Количество элементов:", min_index)

