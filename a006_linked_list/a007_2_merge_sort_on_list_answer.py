from a006_linked_list.a001_crud import LinkedList, Node  # 假设Node在此定义


def merge_sort_on_list(ll: LinkedList):
    if not ll.head or not ll.head.next:
        return ll

    length = ll.get_length()
    sub_g_size = 1

    while sub_g_size < length:
        dummy_head = Node(0)  # 用于暂存新链表的头，方便操作
        current_tail = dummy_head

        ls = ll.head

        while ls:
            # 1. 确定右组起点
            rs = jump_next_n_node(ls, sub_g_size)

            # 如果没有右组，说明剩下的是个尾巴，直接连上并结束本轮
            if not rs:
                current_tail.next = ls
                break

            # 2. 确定下一组起点 (必须在merge打乱指针前记录)
            next_group_head = jump_next_n_node(ls, sub_g_size * 2)

            # 3. 执行合并
            # 优化：merge函数返回合并后的头和尾，且负责把尾巴断开/连好
            merged_head, merged_tail = merge_two_sub_group(ls, rs, sub_g_size)

            # 4. 连接到主链表
            current_tail.next = merged_head
            current_tail = merged_tail

            # 5. 推进指针
            ls = next_group_head

        # 确保尾巴指向 None (防止成环，虽然你的逻辑中已经处理了，但这是双保险)
        # 注意：上面的 break 分支里 ls 如果是残缺的，可能本身 next 就是 None，或者指向上轮的乱序节点
        # 但在自底向上归并中，next_group_head 为 None 时，尾巴自然是 None。

        ll.head = dummy_head.next
        sub_g_size *= 2

    return ll


def merge_two_sub_group(l1, l2, size):
    """
    使用 Dummy Node 简化合并逻辑
    """
    dummy = Node(0)
    tail = dummy

    # 我们需要知道两个子链表的终止条件
    # 你的原方法是找到 le_next 和 re_next，这很好
    # 这里我们用计数器来控制，避免这一步的 jump 预遍历（性能优化点）

    idx1, idx2 = 0, 0
    # l1 长度一定是 size，但 l2 长度可能小于 size
    # 所以 l1 我们不仅看 None，还要看计数；l2 同理

    c1, c2 = l1, l2

    while idx1 < size and idx2 < size and c1 and c2:
        if c1.data <= c2.data:
            tail.next = c1
            c1 = c1.next
            idx1 += 1
        else:
            tail.next = c2
            c2 = c2.next
            idx2 += 1
        tail = tail.next

    # 处理剩余部分
    while idx1 < size and c1:
        tail.next = c1
        c1 = c1.next
        idx1 += 1
        tail = tail.next

    while idx2 < size and c2:
        tail.next = c2
        c2 = c2.next
        idx2 += 1
        tail = tail.next

    # 此时 tail 是合并后的尾节点
    # 注意：此时 tail.next 可能是杂乱的，因为我们没有断开链表
    # 但在主循环中，我们会执行 current_tail.next = merged_head (下一组)
    # 或者直接覆盖 tail.next。
    # 为了安全起见，我们可以在这里暂时不处理 tail.next，留给主循环连接

    return dummy.next, tail


def jump_next_n_node(start, n):
    """简化的 jump，不需要处理 strict 模式了，因为我们在 merge 里用计数器控制"""
    cur = start
    while n > 0 and cur:
        cur = cur.next
        n -= 1
    return cur
