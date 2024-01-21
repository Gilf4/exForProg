A = int(input())
B = int(input())

length = A
while length >= B:
    length -= B

print(f"Длина незанятой части {length}")