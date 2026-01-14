"""
输入苹果数量，看能否用容量8或6的若干个袋子组合，恰好装下。
若能恰好装下，返回最少解决的袋子数。否则返回-1。
"""

# 解法类：苹果装袋问题的递归解法
# 提供 entry 和 solve 两个方法。


class Solution:
    def __init__(self):
        pass  # 初始化方法，目前不需要任何初始化操作

    def entry(self, num):
        ans = self.solve(num)
        if ans == float("inf"):
            return -1
        return ans

    def solve(self, num):
        """
        使用递归方法计算装袋苹果的最少袋子数量
        每个袋子只能装6个或8个苹果
        Args:
            num: 需要装袋的苹果数量
        Returns:
            int/float: 最少需要的袋子数量，如果无法完全装袋则返回无穷大(float("inf"))
        """
        # 基本情况：如果苹果数量为0，不需要袋子
        if num == 0:
            return 0
        # 如果苹果数量小于6，无法装袋（因为最小的袋子是6个）
        if num < 6:
            return float("inf")
        # 递归情况：尝试用8个装的袋子和6个装的袋子
        # 计算使用8个袋子后剩余苹果需要的袋子数量，并加1（当前这个8个袋子）
        bag_8 = self.solve(num - 8) + 1
        # 计算使用6个袋子后剩余苹果需要的袋子数量，并加1（当前这个6个袋子）
        bag_6 = self.solve(num - 6) + 1
        # 返回两种选择中袋子数量较少的方案
        return min(bag_8, bag_6)


def tst_1():
    sol = Solution()
    for num in range(1, 100):
        print(f"{num} needs bags num: {sol.entry(num)}")


if __name__ == "__main__":
    tst_1()
