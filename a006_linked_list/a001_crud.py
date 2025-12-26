class Node:
    def __init__(self, data):
        self.data = data  # 存储节点数据
        self.next = None  # 指向下一个节点的引用（初始为None）


class LinkedList:
    def __init__(self):
        self.head = None  # 初始化链表为空

    # 在链表末尾添加节点
    def append(self, data):
        new_node = Node(data)  # 创建新节点

        # 如果链表为空，头节点就是新节点
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:  # 遍历到最后一个节点
            last = last.next
        last.next = new_node  # 将新节点加到最后一个节点后面

    # 删除链表中指定值的节点
    def delete(self, key):
        cur = self.head

        # 如果头节点是要删除的节点
        if cur is not None and cur.data == key:
            self.head = cur.next
            return

        # 搜索要删除的节点
        prev = None
        while cur is not None and cur.data != key:
            prev = cur
            cur = cur.next

        # 如果链表中没有找到该值
        if cur is None:
            return

        # 删除节点
        prev.next = cur.next

    def delete_v2(self, key):
        # 我写的版本
        cur = self.head

        if cur and cur.data == key:
            self.head = cur.next
            return

        prev = None
        while cur is not None and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        if cur.data == key:
            prev.next = cur.next

    # 打印链表内容
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def build_list_from_py_list(self, lst):
        for elem in lst:
            self.append(elem)
            
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def tst_linklist():
    llist = LinkedList()

    # 添加元素
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)

    # 打印链表
    print("链表内容:")
    llist.print_list()

    # 删除一个元素
    llist.delete(20)
    print("删除 20 后的链表内容:")
    llist.print_list()


# 测试链表的操作
if __name__ == "__main__":
    tst_linklist()
