import pytest

from search.binary_search import binary_search


@pytest.fixture
def binary_search_test_cases():
    """
    Return test cases for binary search algorithm

    :return: list[tuple], list of test cases where test case is (array, value, expected_result)
    """
    return [
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2, 10),
        ([1, 1, 2, 2, 3, 3, 5, 5, 6, 6], 4, 6),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 0),
        ([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 6, 5),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 4),
    ]


def test_binary_search(binary_search_test_cases):
    for array, value, expected_result in binary_search_test_cases:
        result = binary_search(array, value, 0, len(array) - 1)
        assert result == expected_result
