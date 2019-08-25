import numpy as np
import math


def get_parent_index(i):
    return math.floor((i - 1) / 2)


def get_left_child_index(i):
    return i * 2 + 1


def get_right_child_index(i):
    return i * 2 + 2


def sift_down(array, root_index):
    while get_left_child_index(root_index) < len(array):
        left_child_index = get_left_child_index(root_index)
        right_child_index = get_right_child_index(root_index)
        swap_index = root_index
        if array[left_child_index] > array[root_index]:
            swap_index = left_child_index
        if right_child_index < len(array) and array[right_child_index] > array[swap_index]:
            swap_index = right_child_index

        if swap_index != root_index:
            array[root_index], array[swap_index] = array[swap_index], array[root_index]
            root_index = swap_index
        else:
            return


def heapify(array):
    node_index = get_parent_index(len(array))
    while node_index >= 0:
        sift_down(array, node_index)
        node_index -= 1


def heapsort(array):
    heapify(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array[:i], 0)


def main():
    size = 100
    array = np.random.randint(1, 20, size)
    print(f"before: {array}")
    heapsort(array)
    print(f"after heapsort: {array}")


main()
