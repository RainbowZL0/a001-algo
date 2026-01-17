"""
题目：实现一个基本计算器III

题目描述：
实现一个基本的计算器来计算简单的表达式字符串，支持加、减、乘、除和括号运算。
表达式可以包含整数、运算符(+, -, *, /)、括号和空格。

实现思路：
1. 使用递归下降解析方法处理表达式，通过递归调用解决嵌套括号问题
2. 使用栈结构处理运算优先级，遇到乘除时立即计算，加减则暂存结果
3. 采用一个索引指针遍历表达式，遇到左括号时递归处理子表达式
4. 遇到右括号时返回当前子表达式的计算结果
5. 使用辅助函数处理不同运算符对应的栈操作

时间复杂度：O(n)，其中n是字符串的长度
空间复杂度：O(n)，最坏情况下栈和递归调用深度与字符串长度成正比
"""


class Solution:
    def __init__(self):
        """
        初始化Solution类的实例变量
        i: 用于记录当前字符串处理的索引位置
        str: 存储输入的字符串表达式
        rst: 存储计算结果
        """
        self.i = 0
        self.str = ""
        self.rst = None

    def entry(self, string):
        """
        处理输入字符串的入口方法
        参数:
            string: 需要计算的数学表达式字符串
        """
        self.str = string
        self.rst = self.solve()

    def solve(self):
        """
        递归解析并计算数学表达式的主方法
        使用栈结构处理加减乘除和括号运算
        返回: 计算结果
        """
        stack = []
        last_sign = "+"  # 记录上一个运算符
        num = 0  # 当前正在构建的数字
        while self.i < len(self.str):
            cur = self.str[self.i]  # 获取当前字符
            self.i += 1

            # 处理运算符或右括号的情况
            if cur in "+-*/)":
                stack_operation(stack, last_sign, num)
                if cur in "+-*/":
                    num = 0  # 重置当前数字
                    last_sign = cur  # 更新运算符
                elif cur == ")":
                    return sum(stack)  # 遇到右括号，返回当前栈的和
            # 处理数字字符
            elif "0" <= cur <= "9":
                num = num * 10 + int(cur)  # 构建多位数
            # 处理左括号的情况
            elif cur == "(":
                num = self.solve()  # 递归处理括号内的表达式

        # 处理最后一个数字
        stack_operation(stack, last_sign, num)
        return sum(stack)


def stack_operation(stack, sign, num):
    """
    根据运算符对栈进行操作
    参数:
        stack: 数字栈
        sign: 运算符
        num: 当前数字
    """
    if sign == "+":
        stack.append(num)
    elif sign == "-":
        stack.append(-num)
    elif sign == "*":
        stack.append(stack.pop() * num)
    elif sign == "/":
        stack.append(int(stack.pop() / num))


def tst_1():
    """
    测试函数，用于验证Solution类的计算功能
    """
    sol = Solution()
    sol.entry("(((1+2)*(3+1)))")
    print(sol.rst)


if __name__ == "__main__":
    tst_1()
