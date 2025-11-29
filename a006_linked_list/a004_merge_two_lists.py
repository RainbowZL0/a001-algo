from a001_crud import LinkedList, Node


def merge_two_lists(l1, l2):
    """
    我自己的解法。

    思路：
    - 边界：任一链表为空就返回另一个。
    - 头结点：先选较小的头作为结果链表头，i 指向已排好部分的尾，j 指向另一链表当前节点。
    - 合并：遍历直到 i 到达自己链表末尾；若 i.next 更小则 i 前进，否则把 j 插到 i 后、交换指针继续。
    - 收尾：循环结束后，直接把另一链表剩余部分挂到 i 之后。
    - 复杂度：时间 O(m+n)，空间 O(1)。
    """
    # 边界处理：有一个链表为空时直接返回另一个
    if not l1.head:
        return l2
    if not l2.head:
        return l1
    
    # i、j 分别指向两个链表当前待比较的节点
    i = l1.head
    j = l2.head
    # 先确定结果链表的头指针
    if i.data <= j.data:
        rst = l1
    else:
        i, j = j, i
        rst = l2
    
    # i 永远是已经连好的部分的最后一个节点
    while i.next is not None:
        if i.next.data <= j.data:
            i = i.next
        else:
            i_next = i.next
            i.next = j
            i = j
            j = i_next
    # 退出循环时，i 是 l1 或 l2 的最后一个节点，这等价于 i.next 是 None
    # 另一个链表 l1 或 l2 可能还有剩余节点，直接连上即可
    if j is not None:
        i.next = j
    
    return rst


def merge_two_lists_optimized(l1, l2):
    """
    标准解法。
    """
    # 1. 边界检查（你写的这部分没问题，保留）
    if not l1.head:
        return l2
    if not l2.head:
        return l1

    # 2. 创建哨兵节点 (Dummy Node)
    # 它的作用是作为一个固定的“桩”，方便我们在后面通过 tail 指针挂载节点
    # tail 始终指向已经排序好的部分的最后一个节点。
    # 也可以不用创建dummy节点，那就先比较两个链表的头节点，选出较小的作为结果链表的头节点
    # dummy 节点的本质是，初始时的tail。额外创建它的原因是，tail始终指向已排序部分的最后一个节点，但初始时没有已排序部分
    dummy = Node(-1)
    tail = dummy

    # 获取两个链表的实际头节点
    p1 = l1.head
    p2 = l2.head

    # 3. 循环比较，谁小移谁
    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next  # 尾指针后移

    # 4. 处理剩余部分
    # 循环结束后，肯定有一个链表还没走完，直接把剩下的挂上去即可
    if p1:
        tail.next = p1
    elif p2:
        tail.next = p2

    # 5. 封装返回值
    # 因为你的函数签名要求返回一个 LinkedList 对象，我们把结果包装回去
    result_list = LinkedList()
    result_list.head = dummy.next
    return result_list


def build_ll_1():
    l1 = LinkedList()
    l1.append(3)
    l1.append(6)
    l1.append(9)
    l1.append(10)
    l1.print_list()
    
    l2 = LinkedList()
    l2.append(2)
    l2.append(5)
    l2.append(13)
    l2.append(17)
    l2.print_list()

    return l1, l2


def build_ll_2():
    l1 = LinkedList()
    l1.append(2)
    # l1.append(2)
    # l1.append(4)
    l1.print_list()
    
    l2 = LinkedList()
    l2.append(1)
    l2.append(3)
    l2.append(5)
    l2.print_list()

    return l1, l2


def tst_merge_two_lists():
    l1, l2 = build_ll_2()
    rst = merge_two_lists(l1, l2)
    rst.print_list()


def main():
    tst_merge_two_lists()


if __name__ == "__main__":
    main()
