# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:13:00 2020

@author: jmiller
"""

from typing import Dict, Generator
from functools import lru_cache

# NOTE: Infinite recursion
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

memo: Dict[int, int] = {0: 0, 1: 1}
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

@lru_cache(maxsize = None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)

def fib5(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next