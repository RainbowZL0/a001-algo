from collections import deque


class TreeNode:
    def __init__(self, v):
        self.l = None
        self.r = None
        self.v = v


class Tree:
    def __init__(self):
        self.head = None
        self.size = 0

    def build_tree(self, lst):
        # sourcery skip: extract-duplicate-method, use-assigned-variable
        q = deque()
        self.head = TreeNode(lst[0])
        q.append(self.head)
        for i in range(len(lst)):
            node = q.popleft()
            if left_idx(i) < len(lst):
                l_child = TreeNode(lst[left_idx(i)])
                node.l = l_child
                self.size += 1
                q.append(l_child)
            if right_idx(i) < len(lst):
                r_child = TreeNode(lst[right_idx(i)])
                node.r = r_child
                self.size += 1
                q.append(r_child)


def left_idx(i):
    return 2 * i + 1


def right_idx(i):
    return 2 * i + 2


def tst_tree():
    t = Tree()
    t.build_tree([1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    tst_tree()
