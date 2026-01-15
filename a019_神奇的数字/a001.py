"""
输入n, a, b
神奇的数字是能被a或b整除的。
返回从1开始数的第n个神奇数。
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


def magic(k, a, b, lcm_a_b):
    """在[1, k]上的神奇数的个数"""
    return k // a + k // b - k // lcm_a_b


class Solution:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b

    def main(self):
        upper_bound = self.n * min(self.a, self.b)
        l = 1
        r = upper_bound
        lcm_a_b = lcm(self.a, self.b)

        while l < r:
            m = (l + r) // 2
            magic_cnt = magic(m, self.a, self.b, lcm_a_b)

            # 注意避免错误思路：若magic_cnt恰为n时返回，是错的。
            # 因为 < n 的神奇数的数量是阶梯状增长的，有平台，必须返回最左的那一个
            # 对应普通二分查找问题，如果目标值有相同的多个，必须返回最左的那一个
            if magic_cnt < self.n:
                # 范围内的神奇数不够，说明 m 太小了，肯定不是答案
                l = m + 1
            else:
                # 范围内的神奇数 >= n
                # m 可能是答案，但也可能 m 很大（例如上面例子里的 5）
                # 所以我们不能丢弃 m，让 r = m，尝试去左边找更小的
                r = m

        return l  # 循环结束时 l == r，即为答案


def tst_1():
    sol = Solution(5, 2, 3)
    print(sol.main())


if __name__ == "__main__":
    tst_1()
