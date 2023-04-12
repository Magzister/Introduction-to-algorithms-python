import random


class Utilities:
    @staticmethod
    def generate_number_sequence(amount: int = 1_000_000) -> list[int]:
        sequence = [random.randint(0, amount) for _ in range(amount)]
        random.shuffle(sequence)
        return sequence

    @staticmethod
    def check_sorted_sequence(sequence: list[int], increase: bool = True) -> bool:
        if increase:
            di = 1
            range_ = range(len(sequence) - 1)
        else:
            di = -1
            range_ = range(1, len(sequence))
        for i in range_:
            if sequence[i] > sequence[i + di]:
                return False
        return True

    @staticmethod
    def check_search_algorythm(sequence: list[int], index: int, value: int) -> bool:
        if sequence[index] <= value:
            if index + 1 == len(sequence):
                return True
            elif value <= sequence[index + 1]:
                return True
        return False
