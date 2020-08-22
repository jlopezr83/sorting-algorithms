from .utils import execution_time


@execution_time
def insertion_sort(list_unsorted):
    for i in range(1, len(list_unsorted)):
        current_element = list_unsorted[i]
        j = i-1

        while j >= 0 and current_element < list_unsorted[j]:
            j -= 1

        del list_unsorted[i]
        list_unsorted.insert(j+1, current_element)

