# 定义二叉树节点类
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点值
        self.left = left  # 左子节点
        self.right = right  # 右子节点


# 计算从给定节点开始的最左路径深度
def left_depth(node):

    """
    计算二叉树节点的左子树深度
    参数:
        node: 二叉树的节点
    返回:
        int: 左子树的深度
    """
    depth = 1  # 初始化深度为1
    while node is not None:  # 当节点不为空时，继续循环
        depth += 1  # 每向下遍历一层，深度加1
        node = node.left  # 沿着左子节点向下遍历
    return depth - 1  # 返回深度值（因为初始深度为1，所以需要减1）。非常巧妙的写法。


class Solution:
    def __init__(self):
        self.whole_depth = 0  # 初始化整个树的深度

    def entry(self, node):
        # 获取整个树的深度
        self.whole_depth = left_depth(node)
        # 开始计算节点数量
        return self.solve(node, 1)

    def solve(self, node, node_depth):
        # 如果节点为空，返回0
        if node is None:
            return 0
        # 计算右子树的最左路径深度
        r_tree_depth = left_depth(node.right)

        # 若右树深度到底
        if node_depth + r_tree_depth == self.whole_depth:
            # 说明左子树是满的
            l_tree_num = 2 ** (self.whole_depth - node_depth) - 1
            return self.solve(node.right, node_depth + 1) + l_tree_num + 1
        # 若右树深度不到底
        # 说明右树是满的，只是不到底
        r_tree_num = 2 ** r_tree_depth - 1
        return self.solve(node.left, node_depth + 1) + r_tree_num + 1
