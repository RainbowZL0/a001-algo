# 用栈，输出中左右顺序
from a012_binary_tree_iter.a001_tree_class import TreeNode


def first_order_by_iter(head):
    """
    The function `first_order_by_iter` performs a depth-first traversal of a binary tree using an
    iterative approach.

    Args:
      head: The `head` parameter in the `first_order_by_iter` function is the starting node of a binary
    tree. The function performs a depth-first traversal of the binary tree in a first-order (pre-order)
    manner using an iterative approach.
    """
    stack = [head]
    while stack:
        node = stack.pop()
        print(node.v)
        if node.r:
            stack.append(node.r)
        if node.l:
            stack.append(node.l)


# 测试first_order_by_iter()
def tst_first_order_by_iter():
    head = TreeNode(1)
    head.l = TreeNode(2)
    head.r = TreeNode(3)
    head.l.l = TreeNode(4)
    head.l.r = TreeNode(5)
    head.r.l = TreeNode(6)
    head.r.r = TreeNode(7)
    first_order_by_iter(head)


if __name__ == "__main__":
    tst_first_order_by_iter()
