from functools import *
from sys import *
setrecursionlimit(100000)
@lru_cache(None)
def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(10000))