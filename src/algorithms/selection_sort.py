from .utils import execution_time, swap


@execution_time
def selection_sort(list_unsorted):
    for i in range(len(list_unsorted)):
        min_index = i

        for j in range(i+1, len(list_unsorted)):
            if list_unsorted[j] < list_unsorted[min_index]:
                min_index = j

        swap(list_unsorted, min_index, i)
