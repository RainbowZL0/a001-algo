import math
import random


def search(a: list, left: int, right: int, target: int):
    if left > right:
        return
    mid = math.floor((left + right) / 2)
    mid_elem = a[mid]
    if mid_elem == target:
        return mid
    elif mid_elem < target:
        return search(a=a, left=mid + 1, right=right, target=target)
    else:
        return search(a=a, left=left, right=mid - 1, target=target)


if __name__ == '__main__':
    array = [random.randint(a=0, b=100) for i in range(10)]
    array = sorted(array)
    index = search(a=array, left=0, right=9, target=2)
    print(index)
    print(array)
