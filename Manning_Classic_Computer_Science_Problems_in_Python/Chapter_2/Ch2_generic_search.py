# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:44:30 2020

@author: jmiller
"""

from __future__ import annotations
from enum import IntEnum
from typing import (Tuple, List, TypeVar, Iterable, Sequence, Generic, List,
                    Callable, Set, Deque, Dict, Any, Optional)
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')
C = TypeVar('C', bound = 'Comparable')

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __lt__(self: C, other: C) -> bool:
        ...
    
    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    
    def __ge__(self: C, other: C) -> bool:
        return not self < other

# Linear search
def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

# Binary search
def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5))
print(binary_contains(['a', 'd', 'e', 'f', 'z'], 'f'))
print(binary_contains(['john', 'mark', 'ronald', 'sarah'], 'sheila'))