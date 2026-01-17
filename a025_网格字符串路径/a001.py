"""
问题描述：
输入二维数组（网格），每个元素是一个字符。再输入一组字符串（字典）。
请问从网格任意位置出发，沿上下左右移动（不可重复经过同一格），能否拼出字典中的字符串？
返回所有能被拼出的字符串。

核心问题：
node.pass -= ans数量，这步为什么必须在子问题递归之后做？
为什么从前缀树head点到当前点cur的这些点，pass减少的逻辑不用再写一遍？
"""


# 为了代码自包含，这里补充一个适配本题逻辑的 Trie 节点定义
class Node:
    def __init__(self):
        self.children: dict[str, Node] = {}
        self.pass_ = 0  # 经过这个节点的单词总数（用于剪枝）
        self.end = 0  # 以这个节点结尾的单词数量


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        node = self.head
        node.pass_ += 1
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.pass_ += 1
        node.end += 1


class Solution:
    def __init__(self):
        # 初始化放在 entry 中更安全，防止多次调用实例导致状态污染
        self.string_lst = None
        self.trie = None
        self.mesh_r = 0
        self.mesh_c = 0
        self.mesh = None
        self.path = []  # 用于记录当前路径字符，还原单词。若单词存放到树的结点上，那就无需path变量。
        self.ans_lst = []  # 结果列表

    def entry(self, mesh: list[list[str]], string_lst: list[str]) -> tuple[int, list[str]]:
        """
        程序入口
        """
        # 1. 初始化与状态重置
        self.mesh = mesh
        self.mesh_r, self.mesh_c = len(mesh), len(mesh[0])
        self.string_lst = string_lst
        self.path = []
        self.ans_lst = []

        # 重置前缀树（关键：每次新任务都需要全新的树）
        self.trie = Trie()
        for s in string_lst:
            self.trie.insert(s)

        # 2. 遍历网格所有位置作为起点
        # total_found 用于统计总共找到了多少个单词
        total_found = 0

        for i in range(self.mesh_r):
            for j in range(self.mesh_c):
                # 优化：如果整棵树的单词都已经被找到了（pass_归零），提前结束整个搜索
                if self.trie.head.pass_ == 0:
                    return total_found, self.ans_lst

                # 从 (i, j) 出发进行 DFS
                total_found += self.solve(i, j, self.trie.head)

        return total_found, self.ans_lst

    def solve(self, i: int, j: int, cur: Node) -> int:
        """
        DFS 核心递归函数。
        Args:
            i: 当前网格坐标
            j: 当前网格坐标
            cur: 当前对应的前缀树父节点（尚未进入 (i,j) 对应的字符节点）
        Returns:
            int: 这一轮递归中找到的新单词数量
        """
        # --- 1. 边界检查与基础剪枝 ---

        # 越界检查
        if not (0 <= i < self.mesh_r and 0 <= j < self.mesh_c):
            return 0

        # 获取当前网格字符
        char = self.mesh[i][j]

        # 如果字符是 0，说明当前路径通过该格子，不能重复访问
        if char == 0:
            return 0

        # Trie 剪枝：如果当前字符不在父节点的子节点中，说明此路不通
        if char not in cur.children:
            return 0

        # --- 2. 尝试进入当前节点 ---

        nxt: Node = cur.children[char]

        # 高级剪枝：pass_ 为 0 表示该分支下的所有单词之前都已经找到过了
        if nxt.pass_ == 0:
            return 0

        # --- 3. 标记与处理 ---

        # 标记当前格子已访问（用 0 占位）
        self.mesh[i][j] = 0
        # 记录路径，用于拼出单词
        self.path.append(char)

        # 局部统计：本次 DFS 调用找到的单词数
        found_count = 0

        # 检查：是否找到了一个完整的单词
        if nxt.end > 0:
            # 这是一个新发现的单词
            self.ans_lst.append("".join(self.path))
            # 标记该单词已处理，防止重复添加
            nxt.end -= 1
            found_count += 1

        # --- 4. 向四个方向递归 (上下左右) ---
        # 累加四个方向找到的单词总数
        found_count += self.solve(i - 1, j, nxt)
        found_count += self.solve(i + 1, j, nxt)
        found_count += self.solve(i, j - 1, nxt)
        found_count += self.solve(i, j + 1, nxt)

        # --- 5. 回溯与状态恢复 ---

        # 核心逻辑：从 Trie 的 pass_ 中减去本次搜索找到的单词数。
        # 意义：如果 found_count > 0，说明这个节点底下的某些单词被消耗掉了。
        # 当 pass_ 减为 0 时，下次再遇到这个节点就可以直接跳过（见步骤2）。
        nxt.pass_ -= found_count

        # 恢复网格字符，以便其他路径可以再次经过这里
        self.mesh[i][j] = char
        # 恢复路径记录
        self.path.pop()

        return found_count


# --- 测试代码 ---
def tst_1():
    print("--- Test Case 1 ---")
    mesh = [["a", "b"], ["c", "d"]]
    # "ac" 无法连续走通, "abdc" 可以(右下左), "dca" 可以(上右), "bdc" 可以
    string_lst = ["ac", "abdc", "dca", "bdc"]

    sol = Solution()
    count, words = sol.entry(mesh, string_lst)
    print(f"Total words found: {count}")
    print(f"Words list: {words}")


def tst_2():
    print("\n--- Test Case 2 (Overlapping) ---")
    mesh = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    string_lst = ["oath", "pea", "eat", "rain"]
    # oath: (0,0)->...->(1,2)
    # eat: (1,0)->(1,1)->(1,2)

    sol = Solution()
    count, words = sol.entry(mesh, string_lst)
    print(f"Total words found: {count}")
    print(f"Words list: {words}")


if __name__ == "__main__":
    tst_1()
    tst_2()
