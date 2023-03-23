from typing import List

from sorting.decorators.decorators import timeit
from sorting.utilities.utilities import Utilities


@timeit
def bubble_sort(array: List[int]):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


if __name__ == "__main__":
    sequence = Utilities.generate_number_sequence(10_000)
    bubble_sort(sequence)
    is_sorted = Utilities.check_sorted_sequence(sequence)
    if not is_sorted:
        print("Something went wrong. Array is not sorted =(")
