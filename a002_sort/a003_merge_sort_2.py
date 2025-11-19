import random
from math import floor


def merge_with_sentinel(a: list, p: int, q: int, r: int):
    list_1 = [i for i in a[p : q + 1]]  # from p to q
    list_2 = [i for i in a[q + 1 : r + 1]]  # from q+1 to r

    list_1.append(float("inf"))
    list_2.append(float("inf"))

    i = 0
    j = 0
    for k in range(p, r + 1):
        if list_1[i] < list_2[j]:
            a[k] = list_1[i]
            i += 1
        else:
            a[k] = list_2[j]
            j += 1


def merge_with_copy(a: list, p: int, q: int, r: int):
    list_1 = [i for i in a[p : q + 1]]  # from p to q
    list_2 = [i for i in a[q + 1 : r + 1]]  # from q+1 to r

    i = 0
    j = 0
    for k in range(p, r + 1):
        if list_1[i] <= list_2[j]:
            a[k] = list_1[i]
            i += 1
        else:
            a[k] = list_2[j]
            j += 1

        if i >= len(list_1):
            # list_1到了末尾，然后copy list_2剩余的部分
            a[k + 1 : r + 1] = list_2[j:]
            break
        if j >= len(list_2):
            a[k + 1 : r + 1] = list_1[i:]
            break


def merge_sort(a: list, p: int, r: int):
    if p >= r:
        return
    q = floor((p + r) / 2)
    merge_sort(a, p, q)
    merge_sort(a, q + 1, r)
    merge_with_copy(a, p, q, r)


if __name__ == "__main__":
    array = [random.randint(a=0, b=100) for i in range(10)]
    merge_sort(array, 0, 9)
    print(array)
