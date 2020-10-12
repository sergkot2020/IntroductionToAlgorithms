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


def merge(left_arr, right_arr):
    i = 0
    j = 0
    len_left = len(left_arr)
    len_right = len(right_arr)
    result = []
    while i < len_left and j < len_right:
        left = left_arr[i]
        right = right_arr[j]
        if left_arr[i] < right:
            result.append(left)
            i += 1
        else:
            result.append(right)
            j += 1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result


def merge_insertion_sort(array):
    """
    O(log n)
    """
    e = len(array)
    s = 0
    if (e - s) > 1:
        medium = int((s + e) / 2)
        left_slice = array[s:medium]
        right_slice = array[medium:e]
        if e < 17:
            left_arr = insertion_sort(left_slice)
            right_arr = insertion_sort(right_slice)
        else:
            left_arr = merge_insertion_sort(left_slice)
            right_arr = merge_insertion_sort(right_slice)
        return merge(left_arr, right_arr)
    return array


if __name__ == '__main__':
    arr = get_array()
    run(merge_insertion_sort, arr)
