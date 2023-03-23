from typing import List

from sorting.decorators.decorators import timeit
from sorting.utilities.utilities import Utilities

from search.binary_search import binary_search


@timeit
def insertion_sort(array: List[int]) -> None:
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


@timeit
def binary_insertion_sort(array: List[int]) -> None:
    for j in range(1, len(array)):
        key = array[j]
        index = binary_search(array, key, 0, j - 1)
        while j > index:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key


if __name__ == "__main__":
    sequence = Utilities.generate_number_sequence(10_000)
    insertion_sort(sequence)
    is_sorted = Utilities.check_sorted_sequence(sequence, increase=False)
    if not is_sorted:
        print("Something went wrong. Array was not sorted =(")
    else:
        print("Everything is OK =)")

    sequence = Utilities.generate_number_sequence(10_000)
    binary_insertion_sort(sequence)
    is_sorted = Utilities.check_sorted_sequence(sequence)
    if not is_sorted:
        print("Something went wrong. Array was not sorted =(")
    else:
        print("Everything is OK =)")