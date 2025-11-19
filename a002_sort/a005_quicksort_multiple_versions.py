def bucket_sort(strings):
    if not strings:
        return []

    # 为26个字母创建26个桶
    buckets = {chr(i + ord("a")): [] for i in range(26)}
    # 对于空字符串特殊处理，创建一个单独的桶
    buckets[""] = []

    # 分配字符串到桶
    for string in strings:
        if string == "":
            buckets[""].append(string)
        else:
            buckets[string[0]].append(string[1:])

    sorted_strings = []

    # 递归排序每个桶中的字符串
    for key in sorted(buckets.keys()):
        # 如果桶不为空，则排序桶中的字符串
        if buckets[key]:
            # 对桶中的字符串进行递归排序
            sorted_substrings = bucket_sort(buckets[key])
            # 对递归排序结果进行拼接
            if key != "":
                sorted_strings.extend(key + substring for substring in sorted_substrings)
            else:
                # 空字符串直接加到结果中
                sorted_strings.extend(sorted_substrings)
        # 如果桶是空字符串桶，则直接添加
        elif key == "":
            sorted_strings.extend(buckets[key])

    return sorted_strings


def test_bucket_sort():
    # 示例字符串数组
    original_strings = ["bat", "apple", "bark", "batman", "atom", "app", "a"]
    # 调用排序函数
    sorted_strings = bucket_sort(original_strings)
    print(sorted_strings)


def partition_to_three_parts(lst, p, r):
    pivot = lst[r]  # 选择最后一个元素作为主元
    i = p - 1  # 追踪小于主元的部分
    j = p - 1  # 追踪小于或等于主元的部分

    for k in range(p, r):
        if lst[k] < pivot:
            i += 1
            j += 1
            temp = lst[k]
            lst[k] = lst[j]
            lst[j] = lst[i]
            lst[i] = temp
        elif lst[k] == pivot:
            j += 1
            lst[j], lst[k] = lst[k], lst[j]

    # 将主元放到正确的位置
    lst[j + 1], lst[r] = lst[r], lst[j + 1]

    return i, j + 1


def test_partition_to_three_parts():
    # 示例测试
    lst = [3, 2, 1, 5, 6, 3]
    p = 0
    r = len(lst) - 1
    i, j = partition_to_three_parts(lst, p, r)
    print(lst)  # 输出划分后的数组
    print(i, j)  # 输出小于部分的最后一个元素的位置和等于部分的最后一个元素的位置


if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    a, b, c = c, a, b
    print(a, b, c)
