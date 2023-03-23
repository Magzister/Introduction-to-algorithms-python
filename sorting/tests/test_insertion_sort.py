from sorting.insertion_sort import insertion_sort
from sorting.insertion_sort import binary_insertion_sort

from sorting.tests.fixtures import sorting_algorithm_test_cases


def test_insertion_sort(sorting_algorithm_test_cases):
    for array, sorted_array in sorting_algorithm_test_cases:
        insertion_sort(array)
        assert array == sorted_array


def test_binary_insertion_sort(sorting_algorithm_test_cases):
    for array, sorted_array in sorting_algorithm_test_cases:
        binary_insertion_sort(array)
        assert array == sorted_array
