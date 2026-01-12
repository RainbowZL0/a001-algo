"""实现2"""


class Node:
    def __init__(self):
        # 子节点字典，用于存储当前节点的子节点
        self.children = {}
        # 记录经过当前节点的单词数量
        self.pass_ = 0
        # 记录以当前节点为结尾的单词数量
        self.end = 0


class Trie:
    def __init__(self):
        """
        初始化Trie树，创建头节点
        """
        self.head = Node()

    def insert(self, string):
        """
        向Trie树中插入一个字符串
        :param string: 要插入的字符串
        """
        cur = self.head
        cur.pass_ += 1  # 经过当前节点的字符串数量加1
        for e in string:
            # 如果当前字符的子节点不存在，则创建新节点
            if not cur.children.get(e):
                cur.children[e] = Node()
            cur = cur.children.get(e)
            cur.pass_ += 1  # 经过当前节点的字符串数量加1
        cur.end += 1  # 以当前节点结束的字符串数量加1

    def search_pass(self, string):
        """
        搜索经过某个字符串的路径的节点数
        :param string: 要搜索的字符串
        :return: 经过该字符串路径的节点数
        """
        cur = self.head
        for e in string:
            # 如果当前字符的子节点不存在，返回0
            if cur.children.get(e):
                cur = cur.children.get(e)
            else:
                return 0
        return cur.pass_

    def search_end(self, string):
        """
        搜索以某个字符串结尾的节点数
        :param string: 要搜索的字符串
        :return: 以该字符串结尾的节点数
        """
        cur = self.head
        for e in string:
            # 如果当前字符的子节点不存在，返回0
            if cur.children.get(e):
                cur = cur.children.get(e)
            else:
                return 0
        return cur.end

    def decrease(self, string):
        """
        从Trie树中删除一个字符串
        :param string: 要删除的字符串
        """
        # 如果要删除的字符串不存在，直接返回
        if self.search_end(string) == 0:
            return
        cur = self.head
        cur.pass_ -= 1  # 经过当前节点的字符串数量减1
        for e in string:
            # 当前节点的子节点的pass_减1
            cur.children.get(e).pass_ -= 1
            # 如果子节点的pass_为0，删除该子节点并返回
            if cur.children.get(e).pass_ == 0:
                cur.children.pop(e)
                return
            cur = cur.children.get(e)
        cur.end -= 1  # 以当前节点结束的字符串数量减1
        return
