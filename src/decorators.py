import time
from functools import wraps

def time_measure(func):
    @wraps(func)  # mantem o nome e docstring da função
    def wrapper(*args, **kwargs):           #para receber qualquer tipo de arg
        start_time = time.perf_counter()   
        result = func(*args, **kwargs)     # executa a função original
        end_time = time.perf_counter()     # final time
        elapsed = end_time - start_time    # dif (dt)

        print(f"Execution time '{func.__name__}': {elapsed:.6f} sec")
        return result
    return wrapper

def retry_handler(retries=3, delay=1):
    """
    retries: # of tries
    delay: time (seconds) between atempts
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= retries:
                try:
                    print(f"Try {attempt}/{retries} for '{func.__name__}'...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Fail at attempt {attempt}: {e}")
                    if attempt == retries:
                        print("Max number of tries. Aborting.")
                        raise e
                    time.sleep(delay)
                    attempt += 1
        return wrapper
    return decorator