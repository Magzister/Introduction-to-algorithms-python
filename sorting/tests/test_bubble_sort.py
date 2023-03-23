from sorting.bubble_sort import bubble_sort

from sorting.tests.fixtures import sorting_algorithm_test_cases


def test_bubble_sort(sorting_algorithm_test_cases):
    for array, sorted_array in sorting_algorithm_test_cases:
        bubble_sort(array)
        assert array == sorted_array
