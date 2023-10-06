import time

def decorator(func):
  def function(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken to run the prime number logic is {execution_time:.3f} seconds.")
    return result

  function.time_taken = -1
  return function

@decorator
def find_primes(min, max):
  prime_numbers = []
  for i in range(min, max + 1):
    if is_prime(i):
      prime_numbers.append(i)
  return prime_numbers

def is_prime(n):
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

primes = find_primes(2, 100000)
print(f"The total prime numbers in the given range is {len(primes)} ")