from .utils import execution_time, swap


@execution_time
def bubble_sort(list_unsorted):
    for i in range(len(list_unsorted)):
        for j in range(len(list_unsorted)-i-1):
            if list_unsorted[j] > list_unsorted[j+1]:
                swap(list_unsorted, j, j+1)
