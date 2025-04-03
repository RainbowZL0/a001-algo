"""
给定一个全为数字的字符串，解释1为a, 2为b, 直到26为z。求所有可能转化的数量。
例如"111"可转为aaa, ak, ka
"""


def go(i: int, arr: list, ans: int):
    # 两种直接返回的base case
    if i >= len(arr):
        return 1
    if i == len(arr) - 1:
        if arr[i] == "0":
            return 0
        # else:
        #     return 1

    # 到这里就至少有两个剩余的长度
    if arr[i] == "0":  # 如果首个为0，直接返回0
        return 0
    # 单个元素转换
    ans_1 = go(i + 1, arr, ans)
    # 连续两个元素一起转换，如果满足条件
    ans_2 = 0
    if has_more_than_2_elem(i, arr) and next_2_elem_could_convert(i, arr):
        ans_2 = go(i + 2, arr, ans)
    # 返回两种转换的总数的和
    return ans_1 + ans_2


def has_more_than_2_elem(i: int, arr: list):
    """
    检查当前位置后长度是否大于等于2
    Args:
        i: 从哪里开始检查
        arr: 数组

    Returns:

    """
    if len(arr) - i >= 2:
        return True
    else:
        return False


def next_2_elem_could_convert(i: int, arr: list):
    """
    接下来的连续两个数小于等于26时，可以转换为一个字母
    Args:
        i: 从哪里开始选两个连续数
        arr: 数组

    Returns:

    """
    sub_str = arr[i:i + 2]
    sub_str = "".join(sub_str)
    if int(sub_str) <= 26:
        return True
    else:
        return False


def test_go():
    string = list("110")
    print(go(0, string, 0))


if __name__ == '__main__':
    test_go()
