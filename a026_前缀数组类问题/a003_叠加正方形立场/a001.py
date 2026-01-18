"""
LCP 74. 最强祝福力场
策略一：坐标变换（消除小数）为了避免处理浮点数，我们可以将所有坐标和长度扩大 2 倍。
原范围：$[x - side/2, x + side/2]$新范围：$[2x - side, 2x + side]$这样所有的边界坐标都变成了整数。

策略二：坐标离散化（Coordinate Compression）虽然坐标值很大，但正方形的数量很少（$N \\le 100$）。
这意味着最多只有 $2N$ 个 X 轴边界和 $2N$ 个 Y 轴边界。整个平面被这些边界切割成了最多 $(2N)^2$ 个网格区域。
我们可以收集所有用到的 X 坐标和 Y 坐标，排序并去重。将原始的大坐标映射为它们在排序数组中的下标（Rank）。
这样，原本巨大的平面就被压缩成了一个大约 $200 \\times 200$ 的小网格。

策略三：二维差分（2D Difference Array）在离散化后的网格上，我们需要将每个正方形覆盖的区域 $+1$。
暴力做法：对每个正方形，遍历它覆盖的离散化网格区域并加 1。复杂度 $O(N \\cdot (2N)^2) = O(N^3)$。
对于 $N=100$，运算量约 $10^6$，完全可以通过。
优化做法：使用二维差分数组，单次修改 $O(1)$，最后求前缀和还原。复杂度 $O(N^2)$。
"""


# noinspection PyPep8Naming
class Solution:
    @staticmethod
    def fieldOfGreatestBlessing(forceField: list[list[int]]) -> int:
        xs = set()
        ys = set()

        # 1. 坐标变换与收集
        for x, y, side in forceField:
            xs.add(2 * x - side)
            xs.add(2 * x + side)
            ys.add(2 * y - side)
            ys.add(2 * y + side)

        # 2. 排序去重，建立映射
        sorted_xs = sorted(xs)
        sorted_ys = sorted(ys)

        x_map = {val: i for i, val in enumerate(sorted_xs)}
        y_map = {val: i for i, val in enumerate(sorted_ys)}

        n, m = len(sorted_xs), len(sorted_ys)
        diff = [[0] * (m + 2) for _ in range(n + 2)]

        # 3. 填充差分数组
        for x, y, side in forceField:
            x1 = x_map[2 * x - side]
            x2 = x_map[2 * x + side]
            y1 = y_map[2 * y - side]
            y2 = y_map[2 * y + side]

            # 差分操作 (下标平移+1以防越界)
            diff[x1 + 1][y1 + 1] += 1
            diff[x2 + 2][y1 + 1] -= 1
            diff[x1 + 1][y2 + 2] -= 1
            diff[x2 + 2][y2 + 2] += 1

        # 4. 前缀和计算最大值
        ans = 0
        grid = [[0] * (m + 2) for _ in range(n + 2)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1] + diff[i][j]
                ans = max(ans, grid[i][j])

        return ans
