"""
算法导论4th, 2.1-5
两个二进制数加法，用循环实现。
"""


def binary_add(a: list, b: list):
    """
    @param a:
    @param b:
    @return:
    """
    temp = 0
    r = [0 for _ in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):  # 用i倒序遍历a和b，但是结果存放到r[i+1]
        native_result = a[i] + b[i] + temp
        if native_result == 0:
            temp = 0
            r[i + 1] = 0
        elif native_result == 1:
            temp = 0
            r[i + 1] = 1
        elif native_result == 2:
            temp = 1
            r[i + 1] = 0
        else:
            temp = 1
            r[i + 1] = 1
    r[0] = temp
    return r


if __name__ == "__main__":
    a = [0, 1, 1]
    b = [1, 1, 1]
    print(binary_add(a, b))
