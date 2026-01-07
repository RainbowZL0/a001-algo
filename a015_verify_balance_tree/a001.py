# 验证是否为平衡二叉树
import unittest


class Node:
    def __init__(self, left=None, right=None):
        """
        二叉树节点类
        :param left: 左子节点
        :param right: 右子节点
        """
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        """初始化解决方案类"""

    def entry(self, node):
        """
        入口方法，用于开始验证平衡二叉树
        :param node: 二叉树的根节点
        :return: 调用solve方法的结果
        """
        return self.solve(node)

    def solve(self, node: Node):
        """返回高度，是否为平衡"""
        if node is None:
            return 0, True
        l_h, l_balance = self.solve(node.left)
        if l_balance:
            r_h, r_balance = self.solve(node.right)
            dif = l_h - r_h
            if abs(dif) <= 1 and r_balance:
                return max(l_h, r_h) + 1, True
        return -1, False


class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """测试空树"""
        height, is_balanced = self.solution.entry(None)
        assert height == 0
        assert is_balanced

    def test_single_node(self):
        """测试只有一个节点的树"""
        root = Node()
        height, is_balanced = self.solution.entry(root)
        assert height == 1
        assert is_balanced

    def test_balanced_tree(self):
        """测试平衡二叉树"""
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        node4 = Node()
        node5 = Node()
        node2 = Node(node4, node5)
        node3 = Node()
        root = Node(node2, node3)

        height, is_balanced = self.solution.entry(root)
        assert height == 3
        assert is_balanced

    def test_unbalanced_tree_left(self):
        """测试左子树不平衡"""
        #     1
        #    /
        #   2
        #  /
        # 3
        node3 = Node()
        node2 = Node(node3, None)
        root = Node(node2, None)

        height, is_balanced = self.solution.entry(root)
        assert height == -1
        assert not is_balanced

    def test_unbalanced_tree_right(self):
        """测试右子树不平衡"""
        #   1
        #    \
        #     2
        #      \
        #       3
        node3 = Node()
        node2 = Node(None, node3)
        root = Node(None, node2)

        height, is_balanced = self.solution.entry(root)
        assert height == -1
        assert not is_balanced

    def test_complex_balanced_tree(self):
        """测试复杂平衡二叉树"""
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  /
        # 7
        node7 = Node()
        node4 = Node(node7, None)
        node5 = Node()
        node2 = Node(node4, node5)
        node6 = Node()
        node3 = Node(None, node6)
        root = Node(node2, node3)

        height, is_balanced = self.solution.entry(root)
        assert height == 4
        assert is_balanced

    def test_complex_unbalanced_tree(self):
        """测试复杂不平衡二叉树"""
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  /
        # 7
        #    \
        #     8
        node8 = Node()
        node7 = Node(None, node8)
        node4 = Node(node7, None)
        node5 = Node()
        node2 = Node(node4, node5)
        node6 = Node()
        node3 = Node(None, node6)
        root = Node(node2, node3)

        height, is_balanced = self.solution.entry(root)
        assert height == -1
        assert not is_balanced


if __name__ == "__main__":
    unittest.main()
