from a006_linked_list.a001_crud import LinkedList


def build_tst_ll():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    return ll


def reverse_linked_list(ll: LinkedList):
    prev = None
    cur = ll.head
    while cur:
        next_code = cur.next
        cur.next = prev
        prev = cur
        cur = next_code
    ll.head = prev
    

def tst_reverse_linked_list():
    ll = build_tst_ll()
    reverse_linked_list(ll)
    ll.print_list()
    

if __name__ == "__main__":
    tst_reverse_linked_list()
    