"""两个链表表示两个大数（低位在前），逐位相加生成结果链表。

解题思路：
1. 指针 i、j 分别遍历两个链表，同时维护进位 carry。
2. 每轮取当前节点值（空节点视作 0），求和后：
   - `total // 10` 得到新的进位；
   - `total % 10` 作为当前结果节点。
3. 任一链表走完但仍有进位时继续循环，保证最高位进位被写入。
时间复杂度 O(m + n)，空间复杂度 O(m + n) 用于结果链表。
"""

from a001_crud import LinkedList


def build_tst_ll_1():
    """构造两条示例链表，模拟 962 + 9994 的加法用例。"""
    ll1 = LinkedList()
    ll2 = LinkedList()
    lst1 = [4, 6, 2]
    lst2 = [4, 9, 9, 9]
    ll1.build_list_from_py_list(lst1)
    ll2.build_list_from_py_list(lst2)

    return ll1, ll2


def add_two_lists(ll1: LinkedList, ll2: LinkedList):
    """两个逆序数字链表求和，返回新的链表。

    链表节点存储个位到高位的数字（类似 LeetCode 2），从头结点开始对齐逐位相加。
    关键点：
    - 空位补 0，避免提前结束某一条链表。
    - 维护 carry 确保跨位进位被带入下一轮。
    - 循环条件包含 carry，处理最高位产生的新节点。
    """
    i = ll1.head
    j = ll2.head
    carry = 0
    rst_ll = LinkedList()

    while i or j or carry:
        val1 = i.data if i else 0
        val2 = j.data if j else 0
        total = val1 + val2 + carry
        carry = total // 10
        rst_ll.append(total % 10)

        if i:
            i = i.next
        if j:
            j = j.next

    return rst_ll


def tst_add_two_lists():
    """运行示例用例并打印两条输入链表与求和结果。"""
    ll1, ll2 = build_tst_ll_1()
    print("List 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()

    rst_ll = add_two_lists(ll1, ll2)
    print("Resultant List after addition:")
    rst_ll.print_list()


if __name__ == "__main__":
    tst_add_two_lists()
