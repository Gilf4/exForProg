N = int(input())

K = 1
sum = 0
while sum < N:
    sum += K
    K += 1

print(f"Наименьшее целое положительное число K: {K}")
print(f"Сумма: {sum}")