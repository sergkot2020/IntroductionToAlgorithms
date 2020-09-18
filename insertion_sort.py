from data.helpers import run, get_array


def insertion_sort(array):
    """ simple insertion sort """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

    return array


arr = get_array()
run(insertion_sort, arr)
