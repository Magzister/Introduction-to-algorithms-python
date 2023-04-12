from decorators.decorators import timeit
from utilities.utilities import Utilities


@timeit
def insertion_sort(array: list[int]) -> None:
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


NUMBER_OF_ITERATION = 5
SIZE_OF_SEQUENCES = [
    1_000,
    10_000,
    100_000,
]


if __name__ == "__main__":
    for size in SIZE_OF_SEQUENCES:
        sequence = Utilities.generate_number_sequence(100_000)
        _, time = insertion_sort(sequence)
        print(time)
        total_time = 0
        for i in range(NUMBER_OF_ITERATION):
            sequence = Utilities.generate_number_sequence(size)
            _, time = insertion_sort(sequence)

            is_sorted = Utilities.check_sorted_sequence(sequence)
            if not is_sorted:
                print("Something went wrong. Array was not sorted =(")

            total_time += time
        print(f"Insertion sort took {total_time / NUMBER_OF_ITERATION} on average for {size} elements")
