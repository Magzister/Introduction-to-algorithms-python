from typing import List

from sorting.decorators.decorators import timeit


def binary_search(array: List[int], value: int, left: int, right: int) -> int:
    while left <= right:
        middle = (right + left) // 2
        if array[middle] > value:
            right = middle - 1
        elif array[middle] < value:
            left = middle + 1
        else:
            return middle
    return left


@timeit
def binary_search_wrapper(*args):
    return binary_search(*args)
