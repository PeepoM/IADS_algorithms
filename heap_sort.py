import heapq


def heapsort(arr):
    new_arr = [None] * len(arr)
    i = 0

    # build heap from array
    heapq.heapify(arr)

    while arr:
        elem = heapq.heappop(arr)
        new_arr[i] = elem
        i += 1

    return new_arr


if __name__ == "__main__":
    arr = [5, 1, 8, 2, 0, 9, 3, 10, 4, 6, 7]
    arr_sorted = heapsort(arr)
    print(arr_sorted)
