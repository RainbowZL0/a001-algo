from tqdm import tqdm


def max_heapify(lst: list, i):
    """
    对第i个元素为根的这个子树做max_heapify。假设左右子树已经是最大堆，对根节点做向下冒泡，使得整个树变成最大堆。
    这个版本交换元素时使用的是单纯的swap，你可以优化为连续覆盖。
    Args:
        lst: 一个用数组存储的堆。
        i: 对i元素为根的子树做操作。
    Returns:
        操作后的lst
    """
    if not lst:
        return lst

    current_i = i
    root_value = lst[i]

    # 在树上操作，可能很少写while(左孩子存在)，孩子是否存在应该在循环内部判断，while(True)可能是更常用的。
    # 因为左孩子存在时，右孩子不一定存在，在循环内部还是要判断右孩子是否存在。还不如左右孩子都放到循环内部判断。
    while True:
        left_i = get_left_i(current_i)
        right_i = get_right_i(current_i)

        largest_i = current_i
        largest_v = root_value
        if left_i < len(lst) and largest_v < lst[left_i]:
            largest_i = left_i
            largest_v = lst[left_i]
        if right_i < len(lst) and largest_v < lst[right_i]:
            largest_i = right_i
            largest_v = lst[right_i]

        # 通过largest_i是否改变了来判断是否有一个孩子比current_i的元素更大，而不是通过值不等于。因为索引是唯一的，且是整数
        # 如果写判断值不相等，可能遇到浮点数是否相等的问题。
        if largest_i != current_i:
            # lst[current_i], lst[largest_i] = lst[largest_i], lst[current_i]
            lst[current_i] = largest_v
            current_i = largest_i
        else:
            lst[current_i] = root_value
            break
    return lst


def build_max_heap_from_array(lst: list):
    last_inner_node_i = len(lst) // 2 - 1
    for i in range(last_inner_node_i, -1, -1):
        max_heapify(lst, i)


def heap_sort(lst: list):
    """
    假设传入的是一个最大堆，然后做heap_sort
    """
    result_lst = []
    for _ in range(len(lst)):
        last_i = len(lst) - 1
        lst[0], lst[last_i] = lst[last_i], lst[0]
        result_lst.append(lst.pop(last_i))
        max_heapify(lst, 0)
    return result_lst


def entire_heap_sort(lst: list):
    build_max_heap_from_array(lst)
    return heap_sort(lst)


def get_left_i(i: int):
    return 2 * i + 1


def get_right_i(i: int):
    return 2 * i + 2


def get_parent_i(i: int):
    return (i - 1) // 2


def test_max_heapify():
    lst = [1, 2, 3, 4, 5, 6, 7]
    max_heapify(lst, 0)
    print(lst)


def test_build_heap():
    lst = [1, 2, 3, 4, 5, 6, 7]
    build_max_heap_from_array(lst)
    print(lst)


def test_heap_sort():
    for _ in tqdm(range(1000)):
        lst = list(range(100000))
        entire_heap_sort(lst)


if __name__ == "__main__":
    test_heap_sort()
