def swap(li, i, j):
    temp = li[j]
    li[j] = li[i]
    li[i] = temp


def largest_to_end(li):
    n = len(li)

    for i in range(n - 1):
        if li[i] > li[i + 1]:
            swap(li, i, i + 1)

    return li


largest_to_end([1, 5, 10, 50, 3])
