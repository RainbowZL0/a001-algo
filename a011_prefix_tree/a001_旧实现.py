"""前缀树"""


class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.pass_cnt = 0
        self.end_cnt = 0


def delete_child_of_node(node: PrefixTreeNode, child_key):
    node.children.pop(child_key)


class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word):
        # 结果正确但逻辑奇怪的版本。
        # 在每一轮对字母c的循环里，逻辑最清晰的做法是处理c对应的那个节点，而不是处理c对应节点的父节点
        # 有助于人类理解，循环不变量更清楚。

        # node = self.root
        # for c in word:
        #     node.pass_cnt += 1
        #     if c not in node.children:
        #         node.children[c] = PrefixTreeNode()
        #     node = node.children[c]
        # node.pass_cnt += 1
        # node.end_cnt += 1

        node = self.root
        node.pass_cnt += 1

        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTreeNode()
            child = node.children[c]
            child.pass_cnt += 1
            node = child
        node.end_cnt += 1

    def search_end_cnt(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.end_cnt

    def search_prefix_cnt(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.pass_cnt

    def delete(self, word):
        if self.search_end_cnt(word) == 0:
            return

        node = self.root
        node.pass_cnt -= 1
        # 循环不变量，c初始化为word的
        for c in word:
            child = node.children[c]
            child.pass_cnt -= 1
            # 如果pass_cnt，则删除该节点
            if child.pass_cnt == 0:
                delete_child_of_node(node=node, child_key=c)
                return
            # 否则node指针向child移动
            node = child
        # 退出循环时，node指向word的最后一个字符对应的节点，让它end_cnt减1
        node.end_cnt -= 1
        return


def tst1():
    t = PrefixTree()
    t.insert("abc")
    t.insert("abd")
    t.insert("abc")

    t.delete("abc")
    t.delete("abc")


if __name__ == "__main__":
    tst1()
