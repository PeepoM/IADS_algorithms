def quick_sort(arr):
    quick_sort_sub(arr, 0, len(arr) - 1)


def quick_sort_sub(arr, p, r):
    if p < r:
        pivot = partition(arr, p, r)
        quick_sort_sub(arr, p, pivot - 1)
        quick_sort_sub(arr, pivot + 1, r)


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    arr = [5, 1, 8, 2, 0, 9, 3, 10, 4, 6, 7]
    quick_sort(arr)
    print(arr)
