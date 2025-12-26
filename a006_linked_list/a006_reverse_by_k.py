from a006_linked_list.a001_crud import LinkedList

# 解题思路（反转链表的每 k 个节点）:
# 1) 以当前分组的起点 cur_start 出发，先走 k 步拿到分组终点 cur_finish；
#    若不足 k 个节点则不再处理，直接结束。
# 2) 在 cur_start 到 cur_finish.next 这一半开区间内原地反转指针。
# 3) 反转后把上一组的尾巴 last_tail 指向本组新的头 cur_finish，
#    再把本组原起点 cur_start（反转后变成尾巴）指向下一组起点 next_start，
#    同时更新 last_tail、cur_start 继续处理下一组。
# 4) 记录第一组反转后的头 rst_head，最后写回链表头。


def reverse_by_k(ll: LinkedList, k: int):
    cur_start = ll.head  # 本轮分组起点
    rst_head = None  # 反转后新的链表头
    last_tail = None  # 上一组反转后的尾部
    while cur_finish := get_finish(cur_start, k):  # 不足 k 个时直接退出
        next_start = cur_finish.next  # 下一组的起点
        reverse(cur_start, next_start)  # 原地反转当前分组
        cur_start.next = next_start  # 当前分组尾连向下一组起点
        if last_tail:
            last_tail.next = cur_finish  # 上一组尾连向当前新头
        else:
            rst_head = cur_finish  # 记录第一组的新头
        last_tail = cur_start  # 更新上一组尾
        cur_start = next_start  # 继续下一组
    if rst_head:
        ll.head = rst_head
    return ll


def get_finish(cur_head, k):
    # 返回从 cur_head 开始数第 k 个节点；不足 k 个则返回 None
    i = 0
    cur = cur_head
    while cur:
        i += 1
        if i == k:
            return cur
        cur = cur.next
    return None


def reverse(cur_start, next_start):
    # 反转 [cur_start, next_start) 半开区间
    if not cur_start:
        return
    cur = cur_start
    pre = None
    while cur != next_start:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt


def tst_reverse_by_k():
    ll = LinkedList()
    ll.build_list_from_py_list([1, 2, 3, 4, 5, 6, 7])
    print("Original list:")
    ll.print_list()

    k = 2
    reversed_ll = reverse_by_k(ll, k)
    print(f"Reversed by k={k}:")
    reversed_ll.print_list()


"""
标准解法
核心思路
Dummy Node：创建一个虚拟头指向链表头部，这样“第一组”和“后续组”的操作逻辑就完全一样了，不需要单独维护 rst_head。
三个指针：
pre：当前要翻转的 k 个节点的前一个节点（固定不动）。
start：当前要翻转的 k 个节点的第一个。
end：当前要翻转的 k 个节点的最后一个。

流程：
先让 end 走 k 步，如果不够 k 步直接返回。
记录 next_group = end.next。
断开链表（可选，或者传入范围反转）。
翻转 start 到 end。
拼接：pre.next 指向翻转后的头，start.next 指向 next_group。
重置：pre 移动到 start（现在的队尾），开启下一轮。
"""
# 假设这是 Node 定义
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def reverseKGroup(head: ListNode, k: int) -> ListNode:
#     dummy = ListNode(0)
#     dummy.next = head

#     # pre 永远指向"上一组"的结尾，对于第一组来说，上一组结尾就是 dummy
#     tail = dummy

#     while True:
#         # 1. 检查剩余节点是否有 k 个
#         end = tail
#         for _ in range(k):
#             end = end.next
#             if not end:
#                 return dummy.next  # 不足 k 个，保持原样，直接结束

#         # 2. 记录关键节点
#         start = tail.next
#         next_group_start = end.next

#         # 3. 翻转当前组 (这里展示切断链表法的标准写法)
#         end.next = None  # 先切断，方便复用标准的 reverse
#         reverse(start)  # 反转 start 到 end (此时 end.next 是 None)

#         # 4. 重新连接
#         tail.next = end  # 上一组结尾 -> 当前组新头 (原来的 end)
#         start.next = next_group_start  # 当前组新尾 -> 下一组开头

#         # 5. 指针后移，准备下一轮
#         tail = start  # 当前组的新尾 (start) 变成了下一组的 pre

#     return dummy.next


# def reverse(head):
#     pre = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = pre
#         pre = curr
#         curr = nxt
#     return pre


if __name__ == "__main__":
    tst_reverse_by_k()
