from sorting.merge_sort import merge_sort

from sorting.tests.fixtures import sorting_algorithm_test_cases


def test_merge_sort(sorting_algorithm_test_cases):
    for array, sorted_array in sorting_algorithm_test_cases:
        merge_sort(array)
        assert array == sorted_array
