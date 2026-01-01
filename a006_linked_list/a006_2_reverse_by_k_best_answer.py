class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0)
        dummy.next = head

        # group_prev: 指向“已处理好部分的尾巴”，等待接纳新的一组
        group_prev = dummy

        while True:
            # 1. 探测：寻找当前组的尾部 (kth node)
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # 如果剩余节点不足 k 个，直接结束，保留原样
                    return dummy.next

            # 2. 断链：记录下一组的头，并把当前组切下来
            group_next = kth.next
            kth.next = None  # 【关键】：物理切断，形成一个独立的短链表

            # 3. 翻转：此时 group_start 到 kth 是一个标准的独立链表
            group_start = group_prev.next
            new_start = self.reverse(group_start)

            # 4. 拼接：
            # (a) 把上一组的尾巴接到翻转后的新头
            group_prev.next = new_start

            # (b) 翻转前的头 (group_start) 变成了现在的尾，把它连到下一组
            group_start.next = group_next

            # 5. 推进：更新 group_prev 为当前组的尾巴 (即原来的 group_start)
            group_prev = group_start

        return dummy.next

    def reverse(self, head: ListNode) -> ListNode:
        """标准的最基础反转链表，无需任何改动"""
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
