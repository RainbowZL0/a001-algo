import random

from a006_linked_list.a001_crud import LinkedList


def get_tst_case():
    ll = LinkedList()
    ll.build_list_from_py_list([4, 2, 6, 3, 1, 5])
    return ll


def tst_merge():
    ll = get_tst_case()
    print("Original list:")
    ll.print_list()
    sorted_ll = merge_sort_on_list(ll)
    merge_sort_on_list(ll)
    print("Sorted list:")
    sorted_ll.print_list()


def merge_sort_on_list(ll: LinkedList):
    if not ll.head:
        return ll
    sub_g_size = 1
    length = ll.get_length()

    while sub_g_size < length:
        ll_head = None
        last_g_tail = None
        ls = ll.head

        while ls is not None:
            next_group_head = jump_next_n_node(ls, sub_g_size * 2)
            rs = jump_next_n_node(ls, sub_g_size)
            if rs is not None:
                cur_g_head, cur_g_tail = merge_two_sub_group(ls, rs, sub_g_size)
                if ll_head is None:
                    ll_head = cur_g_head
                if last_g_tail is not None:
                    last_g_tail.next = cur_g_head
                cur_g_tail.next = next_group_head
                ls = next_group_head
                last_g_tail = cur_g_tail
            else:
                break
        sub_g_size *= 2
        ll.head = ll_head

    return ll


def merge_two_sub_group(ls, rs, sub_g_size):
    """
    能调用到本函数，说明ls必不空，且右组有元素。
    返回合并后本组头和尾。
    """
    i = ls
    j = rs
    le = jump_next_n_node(ls, sub_g_size - 1, less_than_n_is_acceptable=False)
    re = jump_next_n_node(rs, sub_g_size - 1, less_than_n_is_acceptable=True)

    le_next = le.next
    re_next = re.next

    group_head = None
    cur_tail = None
    while i is not le_next and j is not re_next:
        if i.data <= j.data:
            if cur_tail is not None:
                cur_tail.next = i
                i = i.next
                cur_tail = cur_tail.next
            else:
                cur_tail = i
                i = i.next
        else:
            if cur_tail is not None:
                cur_tail.next = j
                j = j.next
                cur_tail = cur_tail.next
            else:
                cur_tail = j
                j = j.next
        if group_head is None:
            group_head = cur_tail
    while i is not le_next:
        cur_tail.next = i
        i = i.next
        cur_tail = cur_tail.next
    while j is not re_next:
        cur_tail.next = j
        j = j.next
        cur_tail = cur_tail.next

    return group_head, cur_tail


def jump_next_n_node(start, n, less_than_n_is_acceptable=False):
    if start is None:
        return None

    cur = start
    while n > 0 and cur.next is not None:
        cur = cur.next
        n -= 1
    if not less_than_n_is_acceptable:
        if n == 0:
            return cur
        return None
    return cur


# 假设你的 LinkedList 类和 merge_sort_on_list 函数已经在上面定义了
# 或者你需要 import 它们
# from your_module import LinkedList, merge_sort_on_list


def verify_sorted(ll):
    """辅助函数：将链表转换为列表以验证顺序"""
    result = []
    curr = ll.head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


def run_test_case(name, input_list):
    print(f"--- 测试: {name} ---")
    print(f"输入: {input_list}")

    # 1. 构建链表
    ll = LinkedList()
    ll.build_list_from_py_list(input_list)

    # 2. 运行排序
    try:
        # 为了防止死循环卡死程序，通常测试框架会有超时机制
        # 但在这里我们直接运行，如果卡住说明 Bug 还在
        merge_sort_on_list(ll)
    except Exception as e:
        print(f"❌ 运行时错误: {e}")
        return

    # 3. 验证结果
    actual_output = verify_sorted(ll)
    expected_output = sorted(input_list)

    if actual_output == expected_output:
        print(f"✅ 通过! 结果: {actual_output}")
    else:
        print(f"❌ 失败!")
        print(f"   期望: {expected_output}")
        print(f"   实际: {actual_output}")
    print("\n")


def run_all_tests():
    # 1. 基础测试
    run_test_case("常规乱序 (偶数长度)", [4, 2, 6, 3, 1, 5])

    # 2. 奇数长度 (关键测试点：之前死循环的高发区)
    # 当 sub_g_size=2 时，最后剩下一个 7，没有右组，之前的代码会在这里死循环
    run_test_case("常规乱序 (奇数长度)", [7, 2, 4, 3, 1])

    # 3. 边界条件：空链表
    run_test_case("空链表", [])

    # 4. 边界条件：单元素
    run_test_case("单元素", [1])

    # 5. 边界条件：双元素 (逆序)
    run_test_case("双元素逆序", [2, 1])

    # 6. 已排序
    run_test_case("已排序", [1, 2, 3, 4, 5])

    # 7. 完全逆序
    run_test_case("完全逆序", [5, 4, 3, 2, 1])

    # 8. 重复元素 (测试稳定性/正确性)
    run_test_case("包含重复元素", [4, 1, 2, 4, 3, 1])

    # 9. 大量数据测试 (性能与稳健性)
    large_list = [random.randint(0, 100) for _ in range(20)]
    run_test_case("随机长列表 (20个元素)", large_list)


if __name__ == "__main__":
    # 确保你的 merge_sort_on_list 已经应用了修复
    run_all_tests()
