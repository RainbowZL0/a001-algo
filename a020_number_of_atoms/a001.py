"""
https://leetcode.cn/problems/number-of-atoms/description/
输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
"""
import operator
from collections import defaultdict


def collect(result, elem_str, elem_dic, num):
    """
    收集原子计数的辅助函数
    Args:
        result: 存储最终结果的字典
        elem_str: 当前处理的元素字符串
        elem_dic: 当前处理的元素字典
        num: 当前元素的计数
    Returns:
        更新后的结果字典
    """
    # num为0的含义是1
    if num == 0:
        num = 1
    if elem_str != "":
        result[elem_str] += num
    if len(elem_dic) > 0:
        for k, v in elem_dic.items():
            result[k] += v * num  # 别忘了这里要乘num
    return result


class Solution:
    def __init__(self, args):
        """
        初始化Solution实例
        Args:
            args: 要解析的化学式字符串
        """
        self.args = args
        self.i = 0  # 当前处理位置的索引

    def solve(self):

        """
        递归解析化学式并统计原子数量

        Returns:
            包含原子及其计数的字典
        """
        last_elem_str = ""  # 上一个元素名称
        last_elem_dic = {}  # 上一个元素字典（用于处理括号内的内容）
        result = defaultdict(lambda: 0)  # 结果字典，默认值为0
        num = 0  # 当前数字

        while self.i < len(self.args):
            cur = self.args[self.i]  # 获取当前字符
            self.i += 1

            # 若cur为大写字母，表示新元素开始
            if "A" <= cur <= "Z":
                # 结算上一个元素
                collect(result, last_elem_str, last_elem_dic, num)
                num = 0
                last_elem_str = cur
                last_elem_dic.clear()
            # 若cur为小写字母，是元素名称的一部分
            elif "a" <= cur <= "z":
                last_elem_str += cur
            # 若cur为数字，构建数字
            elif "0" <= cur <= "9":
                num = num * 10 + int(cur)
            # 若cur为左括号，开始新的子表达式
            elif cur == "(":
                # 先结算，但操作与大写字母不完全相同
                collect(result, last_elem_str, last_elem_dic, num)
                num = 0
                last_elem_str = ""  # 此处不同
                # 递归，返回的必为字典，不立即结算，等到下一个结算符号再做
                last_elem_dic = self.solve()
            # 若cur为右括号
            elif cur == ")":
                # 结算结果，返回
                collect(result, last_elem_str, last_elem_dic, num)
                # num = 0  # 这一步能省略，对之后无影响
                return result
        # 越界时再结算一次，最后一个（一组）元素
        collect(result, last_elem_str, last_elem_dic, num)
        return result


def tst_1():
    # 创建Solution类实例，传入化学式字符串"(O2H3)2Fe2A(CD)2"
    sol = Solution("(O2H3)2Fe2A(CD)2")
    # 调用solve方法解决化学式计数问题，并对结果按元素符号进行排序
    sorted_dict = dict(sorted(sol.solve().items(), key=operator.itemgetter(0)))
    # 打印排序后的字典，显示各元素的原子数量
    print(sorted_dict)  # {'A': 1, 'C': 2, 'D': 2, 'Fe': 2, 'H': 6, 'O': 4}

    # 初始化空字符串，用于构建化学式表示
    string = ""
    # 遍历排序后的字典，将元素符号和数量拼接成字符串
    for k, v in sorted_dict.items():
        string += k  # 添加元素符号
        if v > 1:    # 如果数量大于1，则添加数量
            string += str(v)
    # 打印最终的化学式字符串
    print(string)


if __name__ == "__main__":
    tst_1()
