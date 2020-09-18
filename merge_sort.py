from data.helpers import run, get_array


def merge(left_arr, right_arr):
    i = 0
    j = 0
    result = []
    while i < len(left_arr) and j < len(right_arr):
        left = left_arr[i]
        right = right_arr[j]
        if left < right:
            result.append(left)
            i += 1
        else:
            result.append(right)
            j += 1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result


def merge_sort(array):
    e = len(array)
    s = 0
    if (e - s) > 1:
        medium = int((s + e) / 2)
        left_arr = merge_sort(array[s:medium])
        right_arr = merge_sort(array[medium:e])
        return merge(left_arr, right_arr)
    return array


if __name__ == '__main__':
    arr = get_array()
    run(merge_sort, arr)
