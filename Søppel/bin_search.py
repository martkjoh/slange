def bin_search(lst, value, min, max):
    if min >= max:
        return False
    mid = (min + max) // 2
    if lst[mid] == value:
        return mid
    else:
        if lst[mid] < value:
            return bin_search(lst, value, mid, max)
        else:
            return bin_search(lst, value, min, mid)


lst = [1, 2, 3, 9, 11, 13, 17, 25, 57, 90]

i = bin_search(lst, 13, 0, len(lst))
print(i)