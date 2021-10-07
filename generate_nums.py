import random


def get_random_nums(length: int) -> list:
    """
    Return a list of random numbers from 0 to length-1.
    """
    return [random.randint(0, length - 1) for _ in range(length)]


def get_sorted_ascending_nums(length: int) -> list:
    """
    Return a list of numbers from 0 to length-1 sorted in ascending order.
    """
    return [num for num in range(length)]


def get_sorted_descending_nums(length: int) -> list:
    """
    Return a list of numbers from 0 to length-1 sorted in descending order.
    """
    return [num for num in range(length - 1, -1, -1)]


def get_123_nums(length: int) -> list:
    """
    Return a list of numbers formed from {1, 2, 3} set.
    """
    return [random.choice((1, 2, 3)) for _ in range(length)]
