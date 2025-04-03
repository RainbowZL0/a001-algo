import random


# 合并列表中两个连续的已排序子区间
# 参数说明：
#   lst：需要操作的列表
#   left_start：左侧子区间的起始索引
#   left_end：左侧子区间的结束索引
#   right_end：右侧子区间的结束索引（右子区间的起始索引为 left_end + 1）
def merge_two_parts_of_a_list(lst, left_start, left_end, right_end):
    # 用于暂存合并后的结果
    new_lst = []

    # 初始化左右两个子区间的指针
    i = left_start  # 指向左侧子区间的当前元素
    j = left_end + 1  # 指向右侧子区间的当前元素

    # 当左右两个子区间都有剩余元素时，进行比较取较小值添加到新列表中
    while i <= left_end and j <= right_end:
        if lst[i] <= lst[j]:
            new_lst.append(lst[i])
            i += 1
        else:
            new_lst.append(lst[j])
            j += 1

    # 如果左侧子区间还有剩余元素，全部添加到新列表中
    while i <= left_end:
        new_lst.append(lst[i])
        i += 1

    # 如果右侧子区间还有剩余元素，全部添加到新列表中
    while j <= right_end:
        new_lst.append(lst[j])
        j += 1

    # 将合并后的结果复制回原列表对应的位置
    k = left_start
    for elem in new_lst:
        lst[k] = elem
        k += 1


# 迭代方式实现归并排序
# 参数说明：
#   lst：需要排序的列表
def merge_sort_by_iter(lst):
    # 初始子区间长度为 1（即每个元素都被视作已排序的子列表）
    group_len = 1

    # 当子区间长度小于列表总长度时，继续进行合并操作
    while group_len < len(lst):
        # i 为当前待合并区间的左侧起始索引，j 为右侧子区间的起始索引
        i = 0
        j = group_len

        # 遍历整个列表，按当前子区间长度进行合并
        while j < len(lst):
            # 左侧子区间为 lst[i] 到 lst[j-1]
            left_start = i
            left_end = j - 1

            # 右侧子区间为 lst[j] 到 lst[min(len(lst)-1, j+group_len-1)]
            right_end = min(
                len(lst) - 1,
                j + group_len - 1
            )

            # 合并这两个子区间
            merge_two_parts_of_a_list(
                lst,
                left_start,
                left_end,
                right_end
            )

            # 更新指针，移动到下一个需要合并的区间
            i = j + group_len
            j = i + group_len

        # 每一轮合并后，子区间长度翻倍
        group_len *= 2


# 测试归并排序实现的函数，通过生成随机列表验证排序结果的正确性
def the_test_merge_sort_by_iter():
    # 进行 10000 次随机测试
    for i in range(10000):
        # 生成一个包含 10 个随机整数（范围 0 到 100）的列表
        random_list = [random.randint(0, 100) for _ in range(9)]
        # 使用 Python 内置的 sorted 函数作为正确排序结果的标准答案
        standard_answer = sorted(random_list)
        # 使用迭代归并排序对随机列表进行排序
        merge_sort_by_iter(random_list)
        # 断言排序后的列表与标准答案一致
        assert standard_answer == random_list


# 当脚本被直接运行时，执行测试函数
if __name__ == '__main__':
    the_test_merge_sort_by_iter()
