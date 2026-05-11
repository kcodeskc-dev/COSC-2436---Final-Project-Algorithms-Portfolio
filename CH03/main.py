"""
Lab 03: Recursion
Implement recursive functions from Chapter 3.

Every recursive function has two cases:
1. Base case - when the function doesn't call itself
2. Recursive case - when the function calls itself
"""
from typing import List


def countdown(i: int) -> None:
    if i <= 0:
        print(0)
        return
    print(i)
    countdown(i - 1)
    
def fact(x: int) -> int:
    if x <= 1:
        return 1
    return x * fact(x - 1)


def recursive_sum(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr: List) -> int:
    if len(arr) == 0:
        return 0
    return 1 + recursive_count(arr[1:])


def recursive_max(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    max_of_rest = recursive_max(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest
