def minimum_distance(distance, visited):
    minimum = math.inf
    min_index = -1
    for v in range(len(distance)):
        if distance[v] < minimum and (not visited[v]):
            minimum = distance[v]
            min_index = v
    return min_index