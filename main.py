import math
import time
import os
import psutil

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

timerStart = time.perf_counter()
print(fib(30))
timeEnd = time.perf_counter()

# Runtime
print(f"Runtime: {math.floor((timeEnd - timerStart) * 100000)/100} ms")
print(f"Memory Usage: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} MB")