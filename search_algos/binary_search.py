def binary_search(arr, key):
    p = 0
    r = len(arr) - 1

    while p <= r:
        mid = p + (r - p) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        else:
            p = mid + 1

    return -1


def bin_search_rec(arr, key):
    return bin_search_sub(arr, key, 0, len(arr) - 1)


def bin_search_sub(arr, key, p, r):
    if p <= r:
        mid = p + (r - p) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return bin_search_sub(arr, key, p, mid - 1)
        else:
            return bin_search_sub(arr, key, mid + 1, r)

    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5]
    for key in range(-10, 10):
        index = bin_search_rec(arr, key)
        print(index)
