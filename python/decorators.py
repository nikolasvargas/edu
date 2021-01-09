from typing import Callable
import functools


# function based decorators
def cached(func):
    cached_data = {}

    @functools.wraps(func)
    def cached_dec(*args):
        try:
            return cached_data[args]
        except KeyError:
            cached_data[args] = ret = func(*args)
            return ret
    return cached_dec


# class based decorators
class Cached:
    def __init__(self, func):
        self.cached_data = {}
        self.func = func

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return ret


@cached
def compute(x: int) -> int:
    print(f'calling w/ {x}')
    return x * x


@Cached
def compute_sum(x: int) -> int:
    print(f'calling w/ {x}')
    return x + x
