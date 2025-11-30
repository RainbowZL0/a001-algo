def merge_part(lst, l_start, l_end, r_end):
    if l_start >= r_end:
        return
    merged = []
    i = l_start
    j = l_end + 1
    while i <= l_end and j <= r_end:
        if lst[i] <= lst[j]:
            merged.append(lst[i])
            i += 1
        else:
            merged.append(lst[j])
            j += 1
    while i <= l_end:
        merged.append(lst[i])
        i += 1
    while j <= r_end:
        merged.append(lst[j])
        j += 1
    
    a = l_start
    for k in range(len(merged)):
        lst[a] = merged[k]
        a += 1
        

def merge_sort_iter(lst):
    half_range = 1
    while half_range < len(lst):
        start = 0
        end = start + 2 * half_range - 1
        while start < len(lst):
            g1_end = start + half_range - 1
            if g1_end + 1 < len(lst):
                g2_end = min(end, len(lst) - 1)
                merge_part(lst, start, g1_end, g2_end)
            start += 2 * half_range
            end += 2 * half_range
        half_range *= 2
        

def tst_merge_sort_iter():
    lst: list[int] = [3, 38, 27, 43, 3, 9, 82, 10]
    print("Original list:", lst)
    merge_sort_iter(lst)
    print("Sorted list:", lst)


if __name__ == "__main__":
    tst_merge_sort_iter()
    