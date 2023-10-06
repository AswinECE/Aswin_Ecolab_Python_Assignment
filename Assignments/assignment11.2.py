import time
from contextlib import contextmanager

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time

def find_primes(min, max):
  primes = []
  for i in range(min, max + 1):
    if is_prime(i):
      primes.append(i)
  return primes

def is_prime(n):
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

with Timer() as t:
    primes = find_primes(2, 100000)
    print('Total prime numbers in the given range: ', len(primes))

print(f"Time taken: {t.time_taken} seconds" )