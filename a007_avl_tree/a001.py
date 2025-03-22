class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # 初始高度为1


class AVLTree:
    # 获取节点的高度
    def get_height(self, node):
        return node.height if node else 0

    # 计算平衡因子
    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 更新节点高度
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # 左旋转
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # 执行旋转
        y.left = z
        z.right = T2

        # 更新高度
        self.update_height(z)
        self.update_height(y)

        return y  # 返回新的根节点

    # 右旋转
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # 执行旋转
        y.right = z
        z.left = T3

        # 更新高度
        self.update_height(z)
        self.update_height(y)

        return y  # 返回新的根节点

    # 插入操作
    def insert(self, root, key):
        # 1. 标准的 BST 插入
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # 不允许重复的键值

        # 2. 更新当前节点的高度
        self.update_height(root)

        # 3. 计算平衡因子，检查是否需要旋转
        balance = self.get_balance_factor(root)

        # LL（左-左）不平衡 -> 右旋转
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR（右-右）不平衡 -> 左旋转
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR（左-右）不平衡 -> 左旋转 + 右旋转
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL（右-左）不平衡 -> 右旋转 + 左旋转
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # 返回根节点（无变化）
        return root

    # 中序遍历（用于验证树结构）
    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print(f"{root.key} (Height: {root.height})", end=" -> ")
        self.inorder_traversal(root.right)
