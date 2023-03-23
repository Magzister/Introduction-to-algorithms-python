import math
from typing import List

from sorting.decorators.decorators import timeit
from sorting.utilities.utilities import Utilities


def merge(array: List[int], p: int, q: int, r: int) -> None:
    n1: int = q - p + 1
    n2: int = r - q
    left: List[int] = [0] * (n1 + 1)
    right: List[int] = [0] * (n2 + 1)
    for i in range(1, n1 + 1):
        left[i - 1] = array[p + i - 1]
    for i in range(1, n2 + 1):
        right[i - 1] = array[q + i]
    left[n1] = right[n2] = math.inf
    i = j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1


def merge_sort(array: List[int], p: int = None, r: int = None):
    if p is None:
        p = 0
    if r is None:
        r = len(array) - 1

    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


@timeit
def merge_sort_wrapper(*args):
    merge_sort(*args)


if __name__ == "__main__":
    sequence = Utilities.generate_number_sequence(10_000)
    merge_sort_wrapper(sequence, 0, len(sequence) - 1)
    is_sorted = Utilities.check_sorted_sequence(sequence)
    if not is_sorted:
        print("Something went wrong. Array is not sorted =(")
