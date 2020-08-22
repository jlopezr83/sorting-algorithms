from algorithms import bubble_sort


def test_it_sorts_a_list_of_numbers():
    list_unsorted = [9, 2, 1, 4, 8, 3, 5]
    bubble_sort(list_unsorted)

    assert list_unsorted == [1, 2, 3, 4, 5, 8, 9]


def test_it_sorts_a_inverse_sorted_list_of_numbers():
    list_unsorted = [7, 6, 5, 4, 3, 2, 1]
    bubble_sort(list_unsorted)

    assert list_unsorted == [1, 2, 3, 4, 5, 6, 7]


def test_it_sorts_a_list_of_numbers_with_duplicates():
    list_unsorted = [7, 7, 5, 4, 3, 3, 1]
    bubble_sort(list_unsorted)

    assert list_unsorted == [1, 3, 3, 4, 5, 7, 7]
