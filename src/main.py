from random import randint
from copy import deepcopy


from algorithms import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort


MIN_VALUE = 1
MAX_VALUE = 1000
THRESHOLD_ELEMENTS_SLOW_ALGORITHMS = 10000


def generate_list(elements, min, max):
    """
    Generates list with random numbers
    :param elements: number of elements in the list
    :param min: Min value in the list
    :param max: Max value in the list
    :return: List with random numbers
    """
    return [randint(min, max) for _ in range(elements)]


if __name__ == '__main__':
    test_elements = [10, 100, 1000, 10000, 100000, 300000]

    print(f'\nComparing algorithms for {len(test_elements)} lists with different lengths:\n')

    for elements in test_elements:
        list_unsorted = generate_list(elements, MIN_VALUE, MAX_VALUE)

        print(f'List with {elements} elements:')

        if elements < THRESHOLD_ELEMENTS_SLOW_ALGORITHMS:
            bubble_sort(deepcopy(list_unsorted))
            print(f'Bubble sort: \t\t{bubble_sort.execution_time}')

            selection_sort(deepcopy(list_unsorted))
            print(f'Selection sort: \t{selection_sort.execution_time}')

            insertion_sort(deepcopy(list_unsorted))
            print(f'Insertion sort: \t{insertion_sort.execution_time}')
        else:
            print('Bubble sort: \t\tSkipping algorithm because it takes a long time')
            print('Selection sort: \tSkipping algorithm because it takes a long time')
            print('Insertion sort: \tSkipping algorithm because it takes a long time')

        quick_sort(deepcopy(list_unsorted), 0, len(list_unsorted)-1)
        print(f'Quick sort: \t\t{quick_sort.execution_time}')

        merge_sort(deepcopy(list_unsorted))
        print(f'Merge sort: \t\t{merge_sort.execution_time}')

        heap_sort(deepcopy(list_unsorted))
        print(f'Heap sort: \t\t{heap_sort.execution_time}\n')




