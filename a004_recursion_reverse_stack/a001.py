def pop_bottom(a: list):
    if not a:
        return None
    record = a.pop()
    if not a:
        return record
    temp = pop_bottom(a=a)
    a.append(record)
    return temp


def test_pop_last():
    array = [5, 4, 3, 2, 1]
    print(pop_bottom(array))
    print(array)


def reverse_stack(a: list):
    if not a:
        return
    record = pop_bottom(a)
    reverse_stack(a)
    a.append(record)
    return


def test_reverse_stack():
    a = [5, 4, 3, 2, 1]
    reverse_stack(a)
    print(a)


if __name__ == "__main__":
    test_reverse_stack()
