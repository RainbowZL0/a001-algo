class Solution:
    def __init__(self):
        """"""

    def entry(self):
        """"""

    @staticmethod
    def solve(arr):
        """"""
        prefix_sum = [[0] * len(arr[0]) for _ in range(len(arr))]
        a_ans = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # C B
                # A ?
                # ? = B + A - C + ?数值
                # ? 坐标 = (i, j)
                # B 坐标 = (i-1, j)
                # A 坐标 = (i, j-1)
                # C 坐标 = (i-1, j-1)
                prefix_sum[i][j] = (
                    subscribe(prefix_sum, i - 1, j)
                    + subscribe(prefix_sum, i, j - 1)
                    - subscribe(prefix_sum, i - 1, j - 1)
                    + arr[i][j]
                )

                if arr[i][j] == 1:
                    a_ans = max(a_ans, 1)
                a = 1
                while i - a >= 0 and j - a >= 0:
                    # (i-a, j-a)
                    #           (i-a+1, j-a+1)
                    #                           (i-1, j-1)
                    #                                       (i, j)
                    diff_area = (
                        area(
                            arr,
                            prefix_sum,
                            i - a, j - a,
                            i, j
                        )
                        - area(
                            arr,
                            prefix_sum,
                            i - a + 1, j - a + 1,
                            i - 1, j - 1
                        )
                    )
                    if diff_area == 4 * a:
                        a_ans = max(a_ans, a + 1)  # a=边长减1，边长=a+1
                    a += 1
        return a_ans


def subscribe(arr, i, j):
    if i < 0 or j < 0:
        return 0
    return arr[i][j]


def area(arr, prefix_sum, top_left_r, top_left_c, bottom_right_r, bottom_right_c):
    """
    传入A, B坐标，即左上和右下，返回围成的区域里，数值的总和。传入前缀和数组，不是原始数组。
    D   C
      A
    E   B

    A: (r1, c1)
    B: (r2, c2)
    C: (r1 - 1, c2)
    D: (r1 - 1, c1 - 1)
    E: (r2, c1 - 1)

    面积等于 B - E - C + D

    Args:
        arr:
        prefix_sum:
        top_left_r:
        top_left_c:
        bottom_right_r:
        bottom_right_c:

    Returns:

    """
    r1, c1, r2, c2 = top_left_r, top_left_c, bottom_right_r, bottom_right_c
    # 若范围内只有一个数，返回它自己
    if r1 == r2 and c1 == c2:
        return arr[r1][c1]
    # 若范围里没有任何数，返回0
    if r1 > r2 and c1 > c2:
        return 0
    # 否则返回范围里的数的总和，用二维前缀树组加速计算
    return (subscribe(prefix_sum, r2, c2)
            - subscribe(prefix_sum, r2, c1 - 1)
            - subscribe(prefix_sum, r1 - 1, c2)
            + subscribe(prefix_sum, r1 - 1, c1 - 1))


def tst():
    sol = Solution()

    test_cases = [
        # Case 1: 单个 0
        {
            "arr": [[0]],
            "expected": 0,
            "desc": "Single 0"
        },
        # Case 2: 单个 1
        {
            "arr": [[1]],
            "expected": 1,
            "desc": "Single 1"
        },
        # Case 3: 2x2 全 1 正方形
        {
            "arr": [
                [1, 1],
                [1, 1]
            ],
            "expected": 2,
            "desc": "2x2 Solid Square"
        },
        # Case 4: 3x3 只有边界是 1 (中间是 0)
        # 这种题通常考察的是"边界全为1的最大正方形"
        {
            "arr": [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            "expected": 3,
            "desc": "3x3 Hollow Square"
        },
        # Case 5: 3x3 全 1
        {
            "arr": [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            "expected": 3,
            "desc": "3x3 Solid Square"
        },
        # Case 6: 无法构成正方形的情况 (L型)
        {
            "arr": [
                [1, 1],
                [1, 0]
            ],
            "expected": 1,
            "desc": "L-Shape (No 2x2)"
        },
        # Case 7: 矩形中的正方形
        {
            "arr": [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            "expected": 2,
            "desc": "Square inside Rectangle"
        },
        # Case 8: 稍微大一点的空心测试
        {
            "arr": [
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 1]
            ],
            "expected": 4,
            "desc": "4x4 Hollow Square"
        }
    ]

    print(f"{'Description':<25} | {'Expected':<10} | {'Actual':<10} | {'Result'}")
    print("-" * 60)

    for case in test_cases:
        arr = case["arr"]
        expected = case["expected"]
        desc = case["desc"]

        # 为了防止 debug 过程中可能的死循环卡死，这里只是简单调用
        # 如果你发现程序卡住不动，请检查你的 while 循环逻辑
        try:
            actual = sol.solve(arr)
            status = "PASS" if actual == expected else "FAIL"
        except Exception as e:
            actual = "Error"
            status = f"ERR: {e}"

        print(f"{desc:<25} | {expected:<10} | {actual:<10} | {status}")


if __name__ == "__main__":
    tst()
