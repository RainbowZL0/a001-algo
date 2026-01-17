# LeetCode 432. All O`one Data Structure (全 O(1) 的数据结构)


class Node:
    def __init__(self) -> None:
        self.freq = 0
        self.elems = set()
        self.pr = None
        self.nxt = None


class LL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_node_right(self, cur):
        """cur 不允许为空"""
        assert cur is not None

        # 记录原下一个点
        nxt = cur.nxt
        # 新建点，freq比当前点大1
        node = Node()
        node.freq = cur.freq + 1
        # 连接修改
        cur.nxt = node
        node.pr = cur
        node.nxt = nxt

        if nxt is not None:
            nxt.pr = node

        if cur is self.tail:
            self.tail = node

        # 返回新点
        return node

    def insert_node_left(self, cur):
        """cur 不允许为空，且cur.freq不为1"""
        assert cur is not None
        assert cur.freq != 1

        pr = cur.pr
        node = Node()
        node.freq = cur.freq - 1
        cur.pr = node
        node.nxt = cur
        node.pr = pr

        if pr is not None:
            pr.nxt = node

        # 若传入的cur是头，则头改为node，是新头
        if cur is self.head:
            self.head = node

        # 返回新点
        return node

    def remove_node(self, cur):
        """cur 不允许为空"""
        pr = cur.pr
        nxt = cur.nxt
        if pr is not None:
            pr.nxt = nxt
        if nxt is not None:
            nxt.pr = pr

        if cur is self.head:
            self.head = nxt
        if cur is self.tail:
            self.tail = pr

    def add_first_node(self):
        node = Node()
        node.freq = 1
        self.head = node
        self.tail = node
        return node


class Ans:
    def __init__(self) -> None:
        self.ll = LL()
        self.dic = {}

    def get_max_freq_elems(self):
        if self.ll.tail:
            return self.ll.tail.elems
        return None

    def get_min_freq_elems(self):
        if self.ll.head:
            return self.ll.head.elems
        return None

    def add_elem(self, k):
        if k in self.dic:
            cur = self.dic[k]
            if cur.nxt is None or (cur.nxt is not None and cur.nxt.freq != cur.freq + 1):
                self.ll.insert_node_right(cur)
            nw = cur.nxt
            # 转移位置
            cur.elems.remove(k)
            nw.elems.add(k)
            # dic维护
            self.dic[k] = nw

            # 若cur的elem已清空，删除链表结点
            if len(cur.elems) == 0:
                self.ll.remove_node(cur)
        # else 没添加过k
        else:
            # 若链表一个点都没有
            if self.ll.head is None:
                nw = self.ll.add_first_node()
                nw.elems.add(k)
                self.dic[k] = nw
            else:
                # 若链表不空，说明self.head不空
                # 若freq=1的点存在，等价于self.ll.head的freq是1
                if self.ll.head.freq == 1:
                    self.ll.head.elems.add(k)
                    self.dic[k] = self.ll.head
                # else freq=1的点不存在，说明self.ll.head.freq必大于1
                else:
                    # 需要在head左侧插入点
                    nw = self.ll.insert_node_left(self.ll.head)
                    assert nw.nxt is not None
                    nw.elems.add(k)
                    self.dic[k] = nw

    def dec_elem(self, k):
        # 若该元素存在
        if k in self.dic:
            cur: Node = self.dic[k]
            cur.elems.remove(k)
            if cur.freq == 1:
                self.dic.pop(k)
            else:
                if cur.pr is None or (cur.pr is not None and cur.pr.freq != cur.freq - 1):  # noqa: SIM108
                    nw = self.ll.insert_node_left(cur)
                else:
                    nw = cur.pr
                nw.elems.add(k)
                self.dic[k] = nw

            # 若cur的elem已清空，删除链表结点
            if len(cur.elems) == 0:
                self.ll.remove_node(cur)


if __name__ == "__main__":
    ans = Ans()
    ans.add_elem("a")
    ans.add_elem("b")
    ans.add_elem("a")
    ans.add_elem("a")
    ans.add_elem("c")
    ans.add_elem("b")

    ans.dec_elem("a")
