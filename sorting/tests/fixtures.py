import pytest


@pytest.fixture
def sorting_algorithm_test_cases():
    """
    Return test cases for sorting algorithm

    :return: list[tuple], list of test cases where test case is (array, sorted_array)
    """
    return [
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ([1, 1, 2, 2, 3, 3, 5, 5, 6, 6], [1, 1, 2, 2, 3, 3, 5, 5, 6, 6]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([9.9, 8, 7.8, 7.5, 1.5, 5, 6, 7], [1.5, 5, 6, 7, 7.5, 7.8, 8, 9.9]),
        ([], []),
        ([1], [1]),
        ([-1, 1, -2, 2, -3, 3, 5, -5, 6, -6], [-6, -5, -3, -2, -1, 1, 2, 3, 5, 6]),
    ]
