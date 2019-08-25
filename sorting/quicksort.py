import numpy as np


def partition(array):
    pivot = array[len(array)-1]
    i = 0
    j = len(array) - 1
    while i < j:
        while array[i] <= pivot and i < len(array)-1:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return array[:i], array[i:]
        array[i], array[j] = array[j], array[i]


def quicksort(array):
    if len(array) > 1:
        low, high = partition(array)
        quicksort(low)
        quicksort(high)


def main():
    size = 25
    array = np.random.randint(1, 10, size)
    print(f"before: {array}")
    quicksort(array)
    print(f"after quicksort: {array}")


main()
