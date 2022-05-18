def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    raise ValueError("Value not present in the list")


if __name__ == "__main__":
    arr = [5, 1, 0, 3, 2, 10, 9, 4]
    index = linear_search(arr, 0)
    print(index)
