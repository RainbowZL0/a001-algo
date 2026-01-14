"""
最大异或值问题解决方案
使用前缀树(Trie)数据结构来高效地查找最大异或值
"""
from a011_prefix_tree.a002_标准实现 import Trie


class Solution:
    def __init__(self):
        # 初始化一个Trie树实例，用于存储二进制字符串
        self.trie = Trie()

    def entry(self, lst):
        # 调用solve方法处理输入列表
        return self.solve(lst)

    def solve(self, lst):
        """

        解决最大异或值问题的主方法。
        对lst中的每个数，都到树上扫描一遍最大异或结果是多少，与累计已知最大结果比较
        Args:
            lst: 每个元素是0和1组成的字符串，8位，形如01010101

        Returns:
            最大异或值
        """
        # 如果输入列表为空，返回全0的字符串
        if len(lst) == 0:
            return "00000000"
        # 遍历lst，每个元素先放到Trie里，然后在Trie里找它参与异或能算出的最大值
        # 初始化答案ans为全0字符串
        ans = "00000000"
        for s in lst:
            # 加入Trie
            self.trie.insert(s)
            # 找s参与计算能算出的最大异或值 s_ans
            s_ans = ""
            cur = self.trie.head
            for c in s:
                # 对s里的每个字符c，理想异或对象在该位应该是 dream = not c
                dream = "1" if c == "0" else "0"
                # 如果dream能实现，real就等于dream，否则real只能取为dream的相反值
                real = dream if dream in cur.children else "0" if dream == "1" else "1"
                # 在树上走到real节点，且添加该位的异或结果到 s_ans
                cur = cur.children[real]
                s_ans += "1" if dream == real else "0"
            # s已经找到它参与的最大异或结果s_ans，与目前最大解ans比较，如果s_ans更好，替代之
            if better(s_ans, ans):
                ans = s_ans
        return ans


def better(s_ans, ans):
    for i in range(len(ans)):
        c1 = s_ans[i]
        c2 = ans[i]
        if c1 > c2:
            return True
        if c1 == c2:
            continue
        return False
    return False


def tst_1():
    # 定义一个函数 tst_1，用于测试 Solution 类的 entry 方法
    # 创建一个列表 lst，包含两个字符串元素
    lst = [
        "00001111",
        "11110000"
    ]
    # 调用 Solution 类的 entry 方法，并将列表 lst 作为参数传入，打印结果
    print(Solution().entry(lst))


if __name__ == "__main__":
    tst_1()
