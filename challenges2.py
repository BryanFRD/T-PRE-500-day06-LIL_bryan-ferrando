import time

s = time.time_ns()

def t(a, b):
  return a if b == 1 else a * t(a, b-1)

print(t(2, 4))

print(f"{(time.time_ns() - s)/1000}ms")