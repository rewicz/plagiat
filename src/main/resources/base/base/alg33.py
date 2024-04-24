def bubble_sort_algorithm(d):
    if len(d) <= 1:
        return d

    for i in range(len(d)):
        for j in range(len(d)):
            if d[i] < d[j]:
                tmp = d[i]
                d[i] = d[j]
                d[j] = tmp
    return d

