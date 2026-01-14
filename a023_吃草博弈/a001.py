class Solution:
    def __init__(self):
        pass

    def entry(self, num, first, second):
        # 入口方法，调用solve方法解决吃草游戏问题
        return self.solve(num, first, second)

    def solve(self, num, first, second):
        """
        每轮只能选择4的幂次方的草数量进行吃草
        这是一个递归解法，通过模拟所有可能的吃草情况来判断谁会获胜
        Args:
            num: 剩余草数量
            first: 本次谁先手
            second: 本次谁后手

        Returns:
            谁获胜
        """
        # 递归终止条件
        #      0   1
        # 先手    赢
        # 后手 赢
        if num == 0:  # 当没有草时，后手玩家获胜
            return second
        if num == 1:  # 当只剩1根草时，先手玩家获胜
            return first
        eat = 1  # 初始可以吃的草数量为1（4的0次方）
        while eat <= num:
            # 递归调用，交换先手和后手，模拟对手的回合
            win = self.solve(num - eat, second, first)
            # 如果当前玩家能找到一种吃法让对手输，则当前玩家获胜
            if win == first:
                return first
            eat *= 4  # 尝试下一个4的幂次方（1, 4, 16, 64...）
        # 如果所有可能的吃法都无法让对手输，则对手获胜
        return second


def tst_1():
    # 创建Solution类的实例
    sol = Solution()
    # 注释掉的行：调用entry方法，参数为3, "A", "B"
    # sol.entry(3, "A", "B")
    # 循环1到99
    for i in range(1, 100):
        # 打印当前数字和调用entry方法的结果
        print(f"{i}: {sol.entry(i, "A", "B")}")


if __name__ == "__main__":
    tst_1()
