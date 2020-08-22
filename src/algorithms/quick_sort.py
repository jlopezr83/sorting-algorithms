from .utils import execution_time, swap


@execution_time
def quick_sort(list_unsorted, left, right):
    if left < right:
        position = partition(list_unsorted, left, right)
        quick_sort(list_unsorted, left, position-1)
        quick_sort(list_unsorted, position+1, right)


def partition(list_unsorted, left, right):
    pivot = list_unsorted[right]
    index_smaller = left - 1

    for index in range(left, right):
        if list_unsorted[index] < pivot:
            index_smaller += 1
            swap(list_unsorted, index_smaller, index)

    swap(list_unsorted, index_smaller + 1, right)

    return index_smaller + 1

