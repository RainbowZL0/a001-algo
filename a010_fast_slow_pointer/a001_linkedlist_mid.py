from math import ceil


def entry(lst):
    """
    用快慢指针在列表里“模拟”单链表找中点
    偶数长度时取“上中位” (即慢指针走到第二个中点的前一个)
    """
    if not lst:
        return
    s = 0
    f = 0
    bound = len(lst)  # 让 bound 指向“越界位置”，更好理解 while f < bound
    while f+1 < bound and f+1+1 < bound:
        s += 1
        f += 2
    return s


def tst(length):
    lst = [0 for _ in range(length)]
    result = entry(lst)
    correct_answer = ceil(length / 2) - 1
    print(correct_answer == result)


def batch_tst():
    for length in range(1, 10):
        tst(length)


if __name__ == '__main__':
    batch_tst()
