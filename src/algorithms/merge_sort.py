from .utils import execution_time


@execution_time
def merge_sort(list_unsorted):
    if len(list_unsorted) > 1:
        middle = len(list_unsorted) // 2

        left = list_unsorted[:middle]
        right = list_unsorted[middle:]

        merge_sort(left)
        merge_sort(right)

        merge(list_unsorted, left, right)


def merge(list_unsorted, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list_unsorted[k] = left[i]
            i += 1
        else:
            list_unsorted[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements
    while i < len(left):
        list_unsorted[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        list_unsorted[k] = right[j]
        j += 1
        k += 1
