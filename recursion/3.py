def PowerN(x, n):
    if n == 0:
        return 1
    else:
        if n < 0:
            return 1 / PowerN(x, -n)
        else:
            if n % 2 == 0:
                return (PowerN(x, n / 2))**(1/2)
            else:
                return x * PowerN(x, n - 1)
for i in range(5):
    PowerN(int(input()), int(input()))


