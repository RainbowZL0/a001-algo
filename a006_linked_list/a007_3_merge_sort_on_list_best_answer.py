class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # 1. 获取长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = Node(0)
        dummy.next = head

        # 2. 外层循环：步长 step = 1, 2, 4, 8 ...
        step = 1
        while step < length:
            prev = dummy
            cur = dummy.next

            while cur:
                # 定义两组的头
                left = cur
                # 这里的 split 会把 left 的尾巴断开，并返回 right 的头
                right = self.split(left, step)
                # split 会把 right 的尾巴断开，并返回下一组的头
                cur = self.split(right, step)

                # 合并左右两组，并将结果接到 prev 后面
                prev = self.merge(left, right, prev)

            step *= 2

        return dummy.next

    def split(self, head, n):
        """
        断开链表：保留 head 开始的 n 个节点。
        返回剩余部分的头节点（如果是 None 则返回 None）。
        """
        # 细节：步数为 n-1 因为我们要停在第 n 个节点上做切断
        for _ in range(n - 1):
            if not head:
                break
            head = head.next

        if not head:
            return None

        second = head.next
        head.next = None  # 关键：物理断开
        return second

    def merge(self, l1, l2, prev):
        """
        合并 l1 和 l2，挂载到 prev.next 上。
        返回合并后的尾节点（作为下一次的 prev）。
        """
        cur = prev
        while l1 and l2:
            if l1.data < l2.data:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        # 这一步很关键：为了外层循环能接上，我们需要走到这一段的尽头
        while cur.next:
            cur = cur.next
        return cur
