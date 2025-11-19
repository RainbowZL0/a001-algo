"""
Created on 2024.03.02
"""

import random

N = 1000


def generate_list():
    """
    @return:
    """
    unsorted_list = [random.randint(1, 10000) for _ in range(N)]
    # unsorted_list = [1, 2, 3]
    return unsorted_list


def bubble_sort(int_list):
    """
    @param int_list:
    @return:
    """
    for i in range(len(int_list) - 1):
        # i实际取值从0到len-2, 一共做len-1次, 每次找一个最小的
        for j in range(len(int_list) - i - 1):
            # i=0时，j最大值为len-2
            # i=len-2时，j最大值为0
            if int_list[j] > int_list[j + 1]:
                temp = int_list[j]
                int_list[j] = int_list[j + 1]
                int_list[j + 1] = temp
    return int_list


def select_sort(int_list):
    """
    @param int_list:
    @return:
    """
    # 每次选一个最小的放到前面，一共执行len-1次
    for i in range(len(int_list) - 1):
        min_index = i
        for j in range(i + 1, len(int_list)):
            if int_list[j] < int_list[min_index]:
                min_index = j
        # 已经找到最小的，接下来交换
        temp = int_list[i]
        int_list[i] = int_list[min_index]
        int_list[min_index] = temp
    return int_list


def insert_sort(int_list):
    """
    插入有两种方法,
    1. 连续交换多次
    2. 记录待插值，然后连续比较多次并覆盖，找到目标位置后赋值一次。
    Args:
        int_list (_type_): _description_
    Returns:
        _type_: _description_
    """
    for j in range(1, len(int_list)):
        # i取值范围：[1, len-1]
        i = j - 1
        while i >= 0 and int_list[i + 1] < int_list[i]:
            temp = int_list[i]
            int_list[i] = int_list[i + 1]
            int_list[i + 1] = temp
            i -= 1
    return int_list


def insertion_sort_1(int_list):
    """
    Monotonically decreasing.
    @param int_list:
    @return:
    """
    for i in range(1, len(int_list)):
        key = int_list[i]
        j = i - 1
        while j >= 0 and int_list[j] < key:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key


def partition(int_list, left, right):
    """从小到大"""
    if not hasattr(partition, "count"):
        partition.count = 0
    partition.count += 1

    if left >= right:
        return
    standard = left  # 选最左元素为中位数。注意L的检查范围必须包含中位数，否则处理一个反例[1, 2]时将打乱顺序为[2, 1]。
    right_record = right
    while left < right:
        while int_list[right] > int_list[standard] and left < right:
            # j的寻找必须先于i，否则反例[1, 2, 3]会打乱顺序
            # j的接受范围（什么情况下循环继续，直至找到一个不接受的是需要交换的）：写>=或>的条件都可以。
            right -= 1
        while int_list[left] <= int_list[standard] and left < right:
            # i的循环继续查找条件：必须<=，不能<。否则反例[1, 2]会打乱顺序。
            left += 1
        int_list[right], int_list[left] = int_list[left], int_list[right]
    middle = left

    int_list[standard], int_list[middle] = int_list[middle], int_list[standard]
    if standard < middle - 1:
        partition(int_list, standard, middle - 1)  # 递归处理，不能再包含中位数，否则有反例[1, 2]，无限递归
    if middle + 1 < right_record:
        partition(int_list, middle + 1, right_record)  # 同样不能再包含中位数


def quick_sort(int_list):
    """
    @param int_list:
    @return:
    """
    partition(int_list, 0, len(int_list) - 1)
    return int_list


def try_sort(sort_func: callable):
    """
    args: sort_func 指定的一个排序function
    """
    int_list = generate_list()
    sorted_list = sort_func(int_list)
    print(sorted_list)


if __name__ == "__main__":
    try_sort(quick_sort)
    # noinspection PyUnresolvedReferences
    print(partition.count)

    # random_list = [random.randint(1, 100) for _ in range(100)]
    # random_list[0], random_list[47], random_list[90] = 10, 10, 10
    # partition(random_list, 0, 99)
