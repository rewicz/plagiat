def bubble_sort(d):
    if len(d) <= 1:
        return d
    less = []
    equal = []
    more = []

    pivot = d[0]
    for n in d:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            equal.append(n)
        elif n > pivot:
            more.append(n)
    return alg35(less) + equal + alg35(more)
