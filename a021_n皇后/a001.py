class Solution:
    def __init__(self, n):

        """
        初始化解决方案对象
        :param n: 棋盘大小，n x n的棋盘
        """
        self.n = n  # 棋盘大小
        self.result = []  # 存储结果的列表

    def solve(self, path, i):
        """
        使用回溯法解决N皇后问题
        :param path: 当前路径，表示已经放置的皇后位置
        :param i: 当前行号
        """
        if i == self.n:
            # 如果已经放置了n个皇后，将当前路径添加到结果中
            self.result.append(path.copy())

        # 在第i行上，j尝试摆放所有列
        for j in range(self.n):
            if can_use(path, i, j):
                path[i] = j  # 在第i行的第j列放置皇后
                self.solve(path, i + 1)  # 递归处理下一行


def can_use(path, i, j):
    """
    检查在第i行的第j列是否可以放置皇后
    :param path: 当前路径，表示已经放置的皇后位置
    :param i: 当前行号
    :param j: 当前列号
    :return: 是否可以放置皇后
    """
    for k in range(i):
        # 排除同列情况
        if path[k] == j:
            return False
        # 排除斜线，公式为 |x1-x2| == |y1-y2|
        if abs(k - i) == abs(path[k] - j):
            return False
    return True


def tst_1():
    for n in range(1, 51):
        sol = Solution(n)
        sol.solve(path=[0 for _ in range(n)], i=0)
        print(f"n={n}, {len(sol.result)}")


if __name__ == "__main__":
    tst_1()
