from functools import *
from sys import *
setrecursionlimit(100000)
@lru_cache(None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(1000))