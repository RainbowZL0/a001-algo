def merge_sort(nums):
    n = len(nums)
    width = 1

    # 外层循环：控制合并的步长 1, 2, 4, 8...
    while width < n:
        # 内层循环：在当前步长下，两两合并
        # range(start, stop, step)
        for i in range(0, n, width * 2):
            left = i
            mid = i + width
            right = min(i + 2 * width, n)

            # 边界检查：如果没有右半部分（mid >= n），或者右半部分长度为0，无需合并
            if mid >= n:
                break

            # 优化点：如果左边最大值 <= 右边最小值，则无需合并（已有序）
            # 注意：mid 是右半边的起始索引，mid-1 是左半边的结束索引
            if nums[mid - 1] <= nums[mid]:
                continue

            merge(nums, left, mid, right)

        width *= 2


def merge(nums, left, mid, right):
    # 使用切片取出左右两部分，代码更可读
    # 注意：这里会产生临时内存开销 O(n)
    left_part = nums[left:mid]
    right_part = nums[mid:right]

    i = 0
    j = 0
    k = left  # k 指向原数组 nums 写入的位置

    # 标准的双指针合并
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1
        k += 1

    # 处理剩余元素
    # 这里的技巧是：因为我们在原数组上修改，
    # 如果 right_part 剩下了，它们本身就在原数组靠后的位置，不用动。
    # 只有 left_part 剩下了，才需要覆盖过去。
    while i < len(left_part):
        nums[k] = left_part[i]
        i += 1
        k += 1


# 测试
if __name__ == "__main__":
    lst = [3, 38, 27, 43, 3, 9, 82, 10]
    merge_sort(lst)
    print(lst)
