"""
Merge sort
"""

import random


def generate_list(length):
    """
    Generate random with a given length
    @param length: len of the list
    @return: random list
    """
    return [random.randint(0, 999) for _ in range(length)]


def merge_sort(int_list: list, left, right):
    """
    Merge sort. [left, right] assign the two inclusive bounds to be sorted.
    @param int_list: list to sort
    @param left: left index
    @param right: right index
    @return:
    """
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(
        int_list, left, mid
    )  # 左半部分必须包含mid，否则只有2个元素时会进入无限递归
    merge_sort(int_list, mid + 1, right)
    merge(int_list, left, mid, right)


def merge(int_list: list, left, mid, right):
    """
    Merge two sorted lists
    @param int_list: list
    @param left: start index to copy into list
    @param mid: position where two sorted lists are split
    @param right: end index of list
    @return: none
    """
    left_part = int_list[left: mid + 1]  # 边界格外注意，左闭右开
    right_part = int_list[mid + 1: right + 1]

    i, j = 0, 0
    copy_to_list_index = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            int_list[copy_to_list_index] = left_part[i]
            i += 1
            copy_to_list_index += 1
        else:
            int_list[copy_to_list_index] = right_part[j]
            j += 1
            copy_to_list_index += 1

    # Copy the remainder to list. Only one of the following loop will be entered.
    while i < len(left_part):
        int_list[copy_to_list_index] = left_part[i]
        i += 1
        copy_to_list_index += 1
    while j < len(right_part):
        int_list[copy_to_list_index] = right_part[j]
        j += 1
        copy_to_list_index += 1


if __name__ == "__main__":
    list_A = generate_list(length=10000000)
    merge_sort(int_list=list_A, left=0, right=len(list_A) - 1)
    print(list_A)
