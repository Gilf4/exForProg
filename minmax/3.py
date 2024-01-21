N = int(input())
numbers = [int(input()) for i in range(N)]

max_count = 0
current_count = 0
for number in numbers:
    if number % 2 == 0:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0
print(max_count)