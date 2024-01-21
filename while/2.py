N = int(input())

while N > 1:
    if N % 3 != 0:
        print("FALSE")
        break
    N /= 3
else:
    print("TRUE")