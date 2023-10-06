import time

def cached(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    wrapper.time_taken = -1
    return wrapper

@cached
@performance_monitor
def factorial(n):
    if n == 0:
        return 1
    else:
        ft=1
        while(n!=0):
            ft=ft*n
            n=n-1
        return ft
print(factorial(4))  
print(factorial(7))  
print(factorial(12))
print(factorial(4))