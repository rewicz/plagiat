def floyd_warshall_algorithm(graph):
    n = len(graph)
    distance = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

    return distance

