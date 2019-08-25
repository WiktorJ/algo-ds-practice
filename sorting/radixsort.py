import numpy as np
import math


def msd_rec(array, exp):
    if exp == 0 or len(array) == 0:
        return
    bucekets = [0 for _ in range(11)]
    tmp = [0 for _ in range(len(array))]
    for el in array:
        bucekets[int(el // exp) % 10 + 1] += 1
    for i in range(10):
        bucekets[i + 1] += bucekets[i]
    for el in array:
        digit = int(el // exp) % 10
        tmp[bucekets[digit]] = el
        bucekets[digit] += 1
    for i in range(len(array)):
        array[i] = tmp[i]
    bucekets = [0] + bucekets
    for i in range(10):
        if bucekets[i + 1] - bucekets[i] > 0:
            msd_rec(array[bucekets[i]: bucekets[i + 1]], int(exp / 10))


def radix_msd(array):
    max_element = max(array)
    digits = int(math.log10(max_element)) + 1
    exp = 10 ** (digits - 1)
    return msd_rec(array, exp)


def main():
    size = 10
    array = np.random.randint(1, 9, size)
    print(f"before: {array}")
    radix_msd(array)
    print(f"after radix msd: {array}")


main()
