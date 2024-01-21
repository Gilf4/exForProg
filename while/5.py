N = int(input())

a, b = 0, 1

while b < N:
    a, b = b, a + b

if b == N:
    print("TRUE")
else:
    print("FALSE")