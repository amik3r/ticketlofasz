import functools

def debug(func):
    def debug_wrapper(*args, **kwargs):
        print(f'executing: {func.__code__}')
        func(*args, **kwargs)
    return debug_wrapper