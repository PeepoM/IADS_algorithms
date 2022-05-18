def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    arr = [5, 1, 8, 2, 0, 9, 3, 10, 4, 6, 7]
    insertion_sort(arr)
    print(arr)
