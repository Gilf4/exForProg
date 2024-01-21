from random import *
import time
import resource

strart_time = time.time()
arr = []
for i in range(10000):
    arr.append(randint(1,100))
# strart_time = time.time()
for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
# end_time = time.time()
# print(end_time-strart_time)
import resource
import time

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
    ]:
    print(desc, name, getattr(usage, name))