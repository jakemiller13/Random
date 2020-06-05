# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:45:15 2020

@author: jmiller
"""

from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self._container: List[T] = []
        
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)

num_discs: int = 4
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int],
          temp: Stack[int], n: int) -> None:
    print('n = {}'.format(n))
    if n == 1:
        print('POP | a = {}, b = {}, c = {}'.format(tower_a, tower_b, tower_c))
        end.push(begin.pop())
    else:
        print('a = {}, b = {}, c = {}'.format(tower_a, tower_b, tower_c))
        hanoi(begin, temp, end, n - 1)
        print('a = {}, b = {}, c = {}'.format(tower_a, tower_b, tower_c))
        hanoi(begin, end, temp, 1)
        print('a = {}, b = {}, c = {}'.format(tower_a, tower_b, tower_c))
        hanoi(temp, end, begin, n - 1)
        print('DONE | a = {}, b = {}, c = {}'.format(tower_a, tower_b, tower_c))

hanoi(tower_a, tower_c, tower_b, num_discs)