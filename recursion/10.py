def digitSum(n):
    if n < 10:
        return n
    some = n // 10
    return n - some*10 + digitSum(some)
print(digitSum(254))