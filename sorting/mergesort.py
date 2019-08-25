import numpy as np


def mergesort(array):
    mid = int(len(array) / 2)
    if len(array) > 2:
        mergesort(array[:mid])
        mergesort(array[mid:])

    i = 0
    j = mid
    tmp = [0] * len(array)

    for k in range(len(array)):
        if i < mid and (j > len(array) - 1 or array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    for i in range(len(array)):
        array[i] = tmp[i]


def main():
    size = 90
    array = np.random.randint(1, 20, size)
    print(f"before: {array}")
    mergesort(array)
    print(f"after quicksort: {array}")


main()
