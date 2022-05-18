def merge_sort(arr):
    return merge_sort_sub(arr, 0, len(arr) - 1)


def merge_sort_sub(arr, p, r):
    if p == r:
        return [arr[p]]

    # overflow may occur
    # mid = (p + r) // 2

    mid = p + (r - p) // 2

    arr_a = merge_sort_sub(arr, p, mid)
    arr_b = merge_sort_sub(arr, mid + 1, r)

    return merge(arr_a, arr_b)


def merge(arr_a, arr_b):
    m = len(arr_a) + len(arr_b)
    arr = [None] * m
    i = j = k = 0

    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] < arr_b[j]:
            arr[k] = arr_a[i]
            i += 1
        else:
            arr[k] = arr_b[j]
            j += 1

        k += 1

    while i < len(arr_a):
        arr[k] = arr_a[i]
        k += 1
        i += 1

    while j < len(arr_b):
        arr[k] = arr_b[j]
        k += 1
        j += 1

    return arr


if __name__ == "__main__":
    arr = [5, 1, 8, 2, 0, 9, 3, 10, 4, 6, 7]
    arr_sorted = merge_sort(arr)
    print(arr_sorted)
