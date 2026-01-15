"""
906. 超级回文数
困难

如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为 超级回文数 。
现在，给你两个以字符串形式表示的正整数 left 和 right  ，统计并返回区间 [left, right] 中的 超级回文数 的数目。

示例 1：
输入：left = "4", right = "1000"
输出：4
解释：4、9、121 和 484 都是超级回文数。
注意 676 不是超级回文数：26 * 26 = 676 ，但是 26 不是回文数。

示例 2：
输入：left = "1", right = "2"
输出：1

提示：
1 <= left.length, right.length <= 18
left 和 right 仅由数字（0 - 9）组成。
left 和 right 不含前导零。
left 和 right 表示的整数在区间 [1, 1018 - 1] 内。
left 小于等于 right 。

----------------------------
最大right值: 18个9
最小left值：1个0

算法思路：
1. 超级回文数的定义：C = B²，且B和C都是回文数
2. 直接枚举C并检查是否是回文数的平方效率太低
3. 更高效的方法：枚举回文数B，计算C=B²，然后检查C是否是回文数
4. 通过生成回文数B来减少搜索空间：
   - B1：奇数长度回文数（如121）
   - B2：偶数长度回文数（如1221）
5. 使用种子a生成B1和B2，然后计算C1=B1²和C2=B2²
6. 检查C1和C2是否在[left, right]范围内且是回文数
"""


class Solution:
    def __init__(self):
        pass

    def entry(self, left, right):
        """
        入口函数，调用solve方法解决问题

        Args:
            left: 区间左边界（字符串形式）
            right: 区间右边界（字符串形式）

        Returns:
            int: 超级回文数的个数
        """
        return self.solve(left, right)

    @staticmethod
    def solve(left, right):
        """
        解决超级回文数计数问题的核心方法

        算法步骤：
        1. 将字符串形式的边界转换为整数
        2. 枚举种子a，生成奇数长度和偶数长度的回文数B1、B2
        3. 计算C1=B1²和C2=B2²
        4. 检查C1和C2是否在范围内且是回文数
        5. 统计符合条件的超级回文数数量

        Args:
            left: 区间左边界（字符串形式）
            right: 区间右边界（字符串形式）

        Returns:
            int: 超级回文数的个数
        """
        left = int(left)
        right = int(right)

        ans = 0
        # 生成A种子，用于构造回文数B
        a = 0
        while True:
            a += 1
            # 生成B1（奇数长度回文）和B2（偶数长度回文）种子
            # 例如：a=12时，B1=121（奇数长度），B2=1221（偶数长度）
            b1 = get_b1_seed_odd(a)
            b2 = get_b2_seed_even(a)

            # 计算C1=B1²和C2=B2²
            # C1会比C2小，因为B1<B2
            c1 = b1**2
            c2 = b2**2

            # 优化：若较小的C1都大于上界范围了，那说明没必要继续枚举了
            if c1 > right:
                break

            # 若较大的C2还没超过下界left，说明还无需收集结果
            if c2 < left:
                continue

            # 检查C1是否是回文数且在范围内
            if is_reverse_number(c1) and left <= c1 <= right:
                ans += 1
                print(c1)

            # 检查C2是否是回文数且在范围内
            if is_reverse_number(c2) and left <= c2 <= right:
                ans += 1
                print(c2)

        return ans


def get_b1_seed_odd(a):
    """
    生成奇数长度的回文数
    例如：
    - a=1 -> 1
    - a=12 -> 121
    - a=123 -> 12321

    原理：
    - 取a的前n-1位数字，逆序后追加到a的末尾
    - 例如a=12，取前1位(1)，逆序后追加到末尾得到121

    Args:
        a: 输入的种子数字

    Returns:
        int: 生成的奇数长度回文数
    """
    tmp = a // 10  # 获取a除最后一位外的所有数字
    while tmp != 0:
        a = a * 10 + tmp % 10  # 将tmp的最低位追加到a的末尾
        tmp //= 10  # 去掉tmp的最低位
    return a


def get_b2_seed_even(a):
    """
    生成偶数长度的回文数
    例如：
    - a=1 -> 11
    - a=12 -> 1221
    - a=123 -> 123321

    原理：
    - 取a的所有数字，逆序后追加到a的末尾
    - 例如a=12，逆序后得到21，追加到末尾得到1221

    Args:
        a: 输入的种子数字

    Returns:
        int: 生成的偶数长度回文数
    """
    tmp = a  # 保存a的原始值
    while tmp != 0:
        a = a * 10 + tmp % 10  # 将tmp的最低位追加到a的末尾
        tmp //= 10  # 去掉tmp的最低位
    return a


def is_reverse_number(num):
    """
    判断输入数字是否是回文数

    方法：
    - 比较数字的最高位和最低位
    - 如果相同，则去掉最高位和最低位，继续比较
    - 如果不同，则不是回文数
    - 直到数字变为0或只剩一位

    示例：
    - num=12321
    - 比较最高位1和最低位1，相同，去掉后得到232
    - 比较最高位2和最低位2，相同，去掉后得到3
    - 只剩一位3，是回文数

    Args:
        num: 要判断的数字

    Returns:
        bool: 如果是回文数返回True，否则返回False
    """
    # 计算num的最高位的单位值
    # 例如num=12321，high_tmp=10000
    copy_num = num
    high_tmp = 1
    while copy_num >= 10:
        high_tmp *= 10
        copy_num //= 10

    while num != 0:
        # 取出 num 的最高位和最低位，判断是否一样
        # num =  12321
        # high = 1   1 = low
        high = num // high_tmp
        low = num % 10
        if high != low:
            return False

        # 去掉最高位和最低位
        # num = 2321
        num %= high_tmp
        # num = 232
        num //= 10
        # high_tmp = 100
        high_tmp //= 100

    return True  # 若num已经变为0，退出循环了，都还没return False，说明是回文数


def tst_1():
    """
    测试函数，用于验证Solution类的正确性
    测试用例：
    1. left=4, right=1000，预期输出4
    2. left=1002000, right=1002002，预期输出1
    3. left=100020000, right=100020002，预期输出1
    4. left=1, right=1000000000000000000，预期输出70
    """
    sol = Solution()
    print("------")
    print(f"ans = {sol.entry('4', '1000')}")
    print("------")
    print(f"ans = {sol.entry('1002000', '1002002')}")
    print("------")
    print(f"ans = {sol.entry('100020000', '100020002')}")
    print("------")
    print(f"ans = {sol.entry('1', '1000000000000000000')}")
    print("------")


if __name__ == "__main__":
    tst_1()
