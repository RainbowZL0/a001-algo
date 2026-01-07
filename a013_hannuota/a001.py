def f(num, src, to, other):

    """
    汉诺塔问题的递归解决方案函数

    参数:
        num: 要移动的盘子数量
        src: 源柱子
        to: 目标柱子
        other: 辅助柱子

    该函数通过递归的方式解决汉诺塔问题，将num个盘子从src柱子移动到to柱子
    """
    if num == 1:  # 基本情况：当只有一个盘子时，直接移动
        print(f"move 1 from {src} to {to}")
    else:  # 递归情况：当有多个盘子时
        f(num - 1, src, other, to)  # 将n-1个盘子从源柱移动到辅助柱
        print(f"move {num} from {src} to {to}")  # 将最大的盘子从源柱移动到目标柱
        f(num - 1, other, to, src)  # 将n-1个盘子从辅助柱移动到目标柱


def tst():
    """
    测试函数 tst
    该函数调用 f 函数并传递参数
    """
    # 调用 f 函数，传入一个整数和三个字符串参数
    f(5, "A", "B", "C")


if __name__ == "__main__":
    tst()
