from datetime import datetime
from functools import wraps


def execution_time(func):
    """
    Decorator to count the execution time of a function
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper_execution_time(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()

        wrapper_execution_time.execution_time = end_time - start_time

        return result

    return wrapper_execution_time


def swap(list_swap, pos1, pos2):
    """
    Swap 2 elements in a list
    :param list_swap:
    :param pos1: Position of the first element
    :param pos2: Position of the second element
    """
    list_swap[pos1], list_swap[pos2] = list_swap[pos2], list_swap[pos1]
