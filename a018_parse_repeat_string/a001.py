class Solution:
    def __init__(self, param_in):

        """
        初始化方法
        :param param_in: 输入的字符串参数
        """
        self.i = 0  # 当前处理的字符位置索引
        self.param_in = param_in  # 存储输入的字符串

    def entry(self):

        """
        入口方法，用于开始处理字符串
        :return: 处理后的结果字符串
        """
        rst = self.solve()  # 调用solve方法处理字符串
        self.i = 0  # 回到初始状态，便于下次调用
        return rst

    def solve(self):

        """
        递归处理字符串的核心方法
        处理包含数字和方括号的字符串，实现类似解码字符串的功能

        重点分析结算时机，什么时候往result里添加东西，
        1. 遇到单个字符，添加到result
        2. 遇到左括号时，等待递归返回结果，然后将结果重复num次，添加到result
        :return: 处理后的结果字符串
        """
        result = ""  # 用于存储当前处理的结果
        num = 0  # 用于存储当前数字

        while self.i < len(self.param_in):
            cur = self.param_in[self.i]  # 获取当前字符
            self.i += 1  # 移动到下一个字符
            if "0" <= cur <= "9":
                num = num * 10 + int(cur)  # 处理多位数
            elif cur == "[":
                save = self.solve()  # 递归处理括号内的内容
                result += num * save  # 将数字和括号内容相乘后添加到结果
                num = 0  # 重置数字
            elif cur == "]":
                return result  # 返回当前处理结果
            else:
                result += cur  # 直接添加非数字非括号的字符

        return result


def tst_1():
    sol = Solution("10[a]")
    result = sol.entry()
    print(result)
    assert result == "aaaaaaaaaa"


def tst_2():
    # 测试嵌套情况
    sol = Solution("2[ab3[c]]")
    print(sol.entry())
    assert sol.entry() == "abcccabccc"


def tst_3():
    # 测试多个字母
    sol = Solution("3[abc]")
    print(sol.entry())
    assert sol.entry() == "abcabcabc"


def tst_4():
    # 测试空字符串
    sol = Solution("")
    print(sol.entry())
    assert sol.entry() == ""


def tst_5():
    # 测试无重复模式
    sol = Solution("abc")
    print(sol.entry())
    assert sol.entry() == "abc"


def tst_6():
    # 测试复杂嵌套
    sol = Solution("2[a2[b]c]")
    print(sol.entry())
    assert sol.entry() == "abbcabbc"


def tst_7():
    # 测试多位数重复
    sol = Solution("12[ab]")
    print(sol.entry())
    assert sol.entry() == "ab" * 12


def run_all_tests():
    print("运行所有测试...")
    tst_1()
    print("测试1通过")
    tst_2()
    print("测试2通过")
    tst_3()
    print("测试3通过")
    tst_4()
    print("测试4通过")
    tst_5()
    print("测试5通过")
    tst_6()
    print("测试6通过")
    tst_7()
    print("测试7通过")
    print("所有测试通过!")


if __name__ == "__main__":
    run_all_tests()
