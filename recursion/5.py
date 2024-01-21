import sys
sys.setrecursionlimit(1000000)
def combine(n, k):
    if k == 0 or n == k:
        return 1
    elif n < k:
        return combine(n-1, k) + combine(n-1, k-1)
    else:
        return 'err'
print(combine(2, 5))
    