"""
2132. 用邮票贴满网格图
困难

给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

覆盖所有 空 格子。
不覆盖任何 被占据 的格子。
我们可以放入任意数目的邮票。
邮票可以相互有 重叠 部分。
邮票不允许 旋转 。
邮票必须完全在矩阵 内 。
如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
"""


def get(arr, i, j):
    """
    安全获取二维数组中指定位置的值
    
    Args:
        arr: 二维数组
        i: 行索引
        j: 列索引
    
    Returns:
        当索引越界时返回0，否则返回arr[i][j]
    
    Note:
        该函数用于处理前缀和计算中的边界情况，避免数组越界错误
    """
    if i < 0 or j < 0:
        return 0
    return arr[i][j]


def can_put(prefix, i, j, h, w):
    """
    判断是否可以在指定位置放置邮票
    
    Args:
        prefix: 前缀和数组，用于快速计算区域和
        i: 邮票左上角的行索引
        j: 邮票左上角的列索引
        h: 邮票的高度
        w: 邮票的宽度
    
    Returns:
        bool: 如果可以放置返回True，否则返回False
    
    判断条件：
    1. 邮票完全在网格内（右下角不越界）
    2. 该区域内没有被占据的格子（区域和为0）
    """
    # 计算邮票的右下角位置
    a = i + h - 1
    b = j + w - 1
    # 检查右下角是否越界
    if a >= len(prefix) or b >= len(prefix[0]):
        return False
    # 检查区域内是否全为0（即没有被占据的格子）
    return get_area(prefix, i, j, a, b) == 0


def get_area(prefix, i, j, a, b):
    """
    使用前缀和数组计算指定矩形区域的和
    
    Args:
        prefix: 前缀和二维数组
        i: 矩形左上角行索引
        j: 矩形左上角列索引
        a: 矩形右下角行索引
        b: 矩形右下角列索引
    
    Returns:
        int: 指定矩形区域内所有元素的和
    
    Note:
        使用二维前缀和公式：
        sum = prefix[a][b] - prefix[i-1][b] - prefix[a][j-1] + prefix[i-1][j-1]
        时间复杂度O(1)
    """
    return (get(prefix, a, b) -
            get(prefix, i - 1, b) -
            get(prefix, a, j - 1) +
            get(prefix, i - 1, j - 1)
            )


def put_stamp(flag, i, j, stampHeight, stampWidth):
    """
    使用差分数组标记邮票放置区域
    
    Args:
        flag: 差分数组，用于记录邮票的覆盖情况
        i: 邮票左上角的行索引
        j: 邮票左上角的列索引
        stampHeight: 邮票的高度
        stampWidth: 邮票的宽度
    
    Note:
        使用二维差分数组技术，可以在O(1)时间内标记一个矩形区域。
        标记方式：
        - 左上角(i,j)加1
        - 左下角(i+stampHeight,j)减1
        - 右上角(i,j+stampWidth)减1
        - 右下角(i+stampHeight,j+stampWidth)加1
        这样做的前缀和就能表示每个位置被多少个邮票覆盖
    """
    m = len(flag)
    n = len(flag[0])

    # 左上角标记+1
    flag[i][j] += 1
    # 左下角标记-1（如果未越界）
    if i + stampHeight < m:
        flag[i + stampHeight][j] -= 1
    # 右上角标记-1（如果未越界）
    if j + stampWidth < n:
        flag[i][j + stampWidth] -= 1
    # 右下角标记+1（如果未越界）
    if i + stampHeight < m and j + stampWidth < n:
        flag[i + stampHeight][j + stampWidth] += 1


def calcu_prefix(arr, prefix, i, j):
    """
    计算二维数组的前缀和
    
    Args:
        arr: 原始二维数组
        prefix: 前缀和数组（可以与arr是同一个数组）
        i: 当前行索引
        j: 当前列索引
    
    Returns:
        int: 位置(i,j)的前缀和值
    
    Note:
        前缀和公式：
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i][j]
        表示从(0,0)到(i,j)的矩形区域内所有元素的和
    """
    return (
        get(prefix, i - 1, j) +
        get(prefix, i, j - 1) -
        get(prefix, i - 1, j - 1) +
        get(arr, i, j)
    )


# noinspection PyPep8Naming
class Solution:
    @staticmethod
    def possibleToStamp(grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        """
        判断是否可以用邮票贴满网格图
        
        Args:
            grid: 二进制矩阵，0表示空格子，1表示被占据的格子
            stampHeight: 邮票的高度
            stampWidth: 邮票的宽度
        
        Returns:
            bool: 如果可以贴满返回True，否则返回False
        
        算法思路：
        1. 使用前缀和快速判断某个区域是否可以放置邮票
        2. 使用差分数组标记邮票的覆盖情况
        3. 遍历所有可能的位置，尝试放置邮票
        4. 最后检查是否所有空格子都被覆盖
        
        时间复杂度：O(m*n)
        空间复杂度：O(m*n)
        """
        # 初始化差分数组，用于标记邮票覆盖情况
        flag = [[0] * len(grid[0]) for _ in range(len(grid))]

        # 第一步：计算grid的前缀和，同时将被占据的格子标记到flag中
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 若原始位置就是1（被占据），在flag中标记
                # 这样后续计算前缀和后，被占据的位置值会大于0
                if grid[i][j] == 1:
                    put_stamp(flag, i, j, 1, 1)  # 只放一个位置，所以h和w都是1
                # 计算grid的前缀和，原地修改grid为前缀和数组
                grid[i][j] = calcu_prefix(grid, grid, i, j)

        # 第二步：遍历所有位置，尝试放置邮票
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果当前位置可以放置邮票（区域内没有被占据的格子且不越界）
                # 则在flag中标记这个邮票的覆盖区域
                if can_put(grid, i, j, stampHeight, stampWidth):
                    put_stamp(flag, i, j, stampHeight, stampWidth)

        # 第三步：计算flag的前缀和，检查是否所有位置都被覆盖
        for i in range(len(flag)):
            for j in range(len(flag[0])):
                # 计算flag的前缀和，得到每个位置被覆盖的次数
                flag[i][j] = calcu_prefix(flag, flag, i, j)
                # 如果某个位置没有被任何邮票覆盖（值为0），则返回False
                if flag[i][j] == 0:
                    return False

        # 所有位置都被覆盖，返回True
        return True


def tst_1():
    """
    测试函数，验证算法的正确性
    
    测试用例：
    1. 4x4网格，第一列全为1，邮票尺寸4x3
    2. 4x4网格，对角线全为1，邮票尺寸2x2
    3. 2x2网格，对角线全为1，邮票尺寸2x2
    """
    grid = [
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    sol = Solution()
    # 测试用例1：应该返回True
    print(sol.possibleToStamp(grid, 4, 3))
    # 测试用例2：应该返回False
    print(sol.possibleToStamp([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 2, 2))
    # 测试用例3：应该返回False
    print(sol.possibleToStamp([[1, 0], [0, 1]], 2, 2))


if __name__ == "__main__":
    tst_1()
