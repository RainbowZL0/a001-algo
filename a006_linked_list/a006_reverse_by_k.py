from a006_linked_list.a001_crud import LinkedList

# 解题思路（反转链表的每 k 个节点）:
# 1) 以当前分组的起点 cur_start 出发，先走 k 步拿到分组终点 cur_finish；
#    若不足 k 个节点则不再处理，直接结束。
# 2) 在 cur_start 到 cur_finish.next 这一半开区间内原地反转指针。
# 3) 反转后把上一组的尾巴 last_tail 指向本组新的头 cur_finish，
#    再把本组原起点 cur_start（反转后变成尾巴）指向下一组起点 next_start，
#    同时更新 last_tail、cur_start 继续处理下一组。
# 4) 记录第一组反转后的头 rst_head，最后写回链表头。


def reverse_by_k(ll: LinkedList, k: int):
    cur_start = ll.head  # 本轮分组起点
    rst_head = None  # 反转后新的链表头
    last_tail = None  # 上一组反转后的尾部
    while cur_finish := get_finish(cur_start, k):  # 不足 k 个时直接退出
        next_start = cur_finish.next  # 下一组的起点
        reverse(cur_start, next_start)  # 原地反转当前分组
        cur_start.next = next_start  # 当前分组尾连向下一组起点
        if last_tail:
            last_tail.next = cur_finish  # 上一组尾连向当前新头
        else:
            rst_head = cur_finish  # 记录第一组的新头
        last_tail = cur_start  # 更新上一组尾
        cur_start = next_start  # 继续下一组
    if rst_head:
        ll.head = rst_head
    return ll


def get_finish(cur_head, k):
    # 返回从 cur_head 开始数第 k 个节点；不足 k 个则返回 None
    i = 0
    cur = cur_head
    while cur:
        i += 1
        if i == k:
            return cur
        cur = cur.next
    return None


def reverse(cur_start, next_start):
    # 反转 [cur_start, next_start) 半开区间
    if not cur_start:
        return
    cur = cur_start
    pre = None
    while cur != next_start:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt


def tst_reverse_by_k():
    ll = LinkedList()
    ll.build_list_from_py_list([1, 2, 3, 4, 5, 6, 7])
    print("Original list:")
    ll.print_list()

    k = 2
    reversed_ll = reverse_by_k(ll, k)
    print(f"Reversed by k={k}:")
    reversed_ll.print_list()


if __name__ == "__main__":
    tst_reverse_by_k()
