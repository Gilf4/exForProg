N = int(input())
numbers = [int(input()) for i in range(N)]

max_element = max(numbers)
first_max_index = numbers.index(max_element)
last_max_index = len(numbers) - 1 - numbers[::-1].index(max_element)

if first_max_index == last_max_index:
    print(0)
else:
    count = abs(last_max_index - first_max_index) - 1
    print(count)