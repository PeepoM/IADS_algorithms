def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [5, 1, 8, 2, 0, 9, 3, 10, 4, 6, 7]
    selection_sort(arr)
    print(arr)
