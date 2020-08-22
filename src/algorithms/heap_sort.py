from .utils import execution_time, swap


@execution_time
def heap_sort(list_unsorted):
    length = len(list_unsorted)

    for i in range(length // 2 - 1, -1, -1):
        heapify(list_unsorted, length, i)

    # Extract elements
    for i in range(length - 1, 0, -1):
        swap(list_unsorted, 0, i)
        heapify(list_unsorted, i, 0)


def heapify(list_unsorted, length, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Left child of root exists and is greater than root
    if left < length and list_unsorted[root] < list_unsorted[left]:
        largest = left

    # Right child of root exists and is greater than root
    if right < length and list_unsorted[largest] < list_unsorted[right]:
        largest = right

    # Change root, if needed
    if largest != root:
        swap(list_unsorted, root, largest)

        # Heapify the root
        heapify(list_unsorted, length, largest)
