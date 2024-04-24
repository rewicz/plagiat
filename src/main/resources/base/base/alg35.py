def prime_alg(graph, n, start):
    visited = [False] * n
    visited[start] = True
    t = []

    for i in range(n - 1):
        minimum = math.inf
        x = 0
        y = 0
        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if (not visited[k]) and graph[j][k]:
                        if minimum > graph[j][k]:
                            minimum = graph[j][k]
                            x = j
                            y = k
        visited[y] = True
        t.append((x, y, graph[x][y]))
    return t
