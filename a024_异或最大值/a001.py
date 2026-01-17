"""
最大异或值问题解决方案
使用前缀树(Trie)数据结构来高效地查找最大异或值
"""

from a011_prefix_tree.a002_标准实现 import Trie


class Solution:
    def __init__(self):
        # 初始化一个Trie树实例
        self.trie = Trie()

    def entry(self, lst):
        return self.solve(lst)

    def solve(self, lst):
        """
        解决最大异或值问题的主方法。
        Args:
            lst: 每个元素是0和1组成的字符串，8位
        Returns:
            最大异或值
        """
        if not lst:  # 【优化1】Pythonic 写法：直接用 if not 判断空列表
            return "00000000"

        # 原始代码：
        # if len(lst) == 0:
        #    return "00000000"

        ans = "00000000"

        for s in lst:
            self.trie.insert(s)

            # 【优化2】使用列表收集结果字符，最后再 join。
            # 虽然 s_ans += "1" 写法简单，但在长字符串处理中，列表 append 效率高于字符串拼接。
            s_ans_list = []

            # 原始代码：
            # s_ans = ""

            cur = self.trie.head

            for c in s:
                # 理想异或对象：如果是0想要1，如果是1想要0
                dream = "1" if c == "0" else "0"

                # 【优化3】大幅简化逻辑
                # 逻辑解析：
                # 1. 我们优先看 cur.children 里有没有 dream。
                # 2. 如果没有 dream，我们别无选择，只能走和当前字符 c 一样的路（因为 c 就是 dream 的反面）。
                #    比如：c是'0'，dream是'1'。如果没'1'可走，那树里肯定只有'0'（即 c）或者没路（但在完整前缀树里肯定有路）。
                #    所以，else 的情况就是 real = c。

                if dream in cur.children:
                    real = dream
                    s_ans_list.append("1")  # 异或成功：1
                else:
                    real = c
                    s_ans_list.append("0")  # 异或失败：0

                # 原始代码（过于复杂的嵌套三元表达式）：
                # real = dream if dream in cur.children else "0" if dream == "1" else "1"
                # s_ans += "1" if dream == real else "0"

                cur = cur.children[real]

            # 将列表转回字符串
            s_ans = "".join(s_ans_list)

            # 【优化4】直接使用 Python 内置比较
            # Python 字符串比较 "1100" > "1011" 本身就是按字典序（即数值大小）比较的。
            # 不需要自己写循环逐位对比。
            ans = max(ans, s_ans)

            # 原始代码：
            # if better(s_ans, ans):
            #     ans = s_ans

        return ans


# 【优化5】删除了 better 函数
# 理由：Python 字符串支持直接比较大小，s1 > s2 即为字典序比较。
# 自定义的循环比较不仅代码量大，而且效率不如底层 C 实现的内置比较符。

# def better(s_ans, ans):
#     """两个整数值、长度相同的字符串比较大小"""
#     for i in range(len(ans)):
#         c1 = s_ans[i]
#         c2 = ans[i]
#         if c1 > c2:
#             return True
#         if c1 == c2:
#             continue
#         return False
#     return False


def tst_1():
    lst = ["00001111", "11110000"]
    print(Solution().entry(lst))


if __name__ == "__main__":
    tst_1()
