def a_star_algorithm(graph, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_nodes = []
    closed_nodes = []
    open_nodes.append(start_node)

    while len(open_nodes) > 0:
        current_node = open_nodes[0]
        current_idx = 0

        for idx, node in enumerate(open_nodes):
            if node.f < current_node.f:
                current_node = node
                current_idx = idx

        open_nodes.pop(current_idx)
        closed_nodes.append(current_node)

        if current_node == end_node:
            path = []
            temp = current_node
            while temp is not None:
                path.append(temp.cord)
                temp = temp.parent
            return [(t[1], t[0]) for t in path][::-1]

        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            current_position = (current_node.cord[0] + new_position[0], current_node.cord[1] + new_position[1])

            if current_position[0] > (len(graph) - 1) or current_position[0] < 0 or current_position[1] > (
                    len(graph[len(graph) - 1]) - 1) or current_position[1] < 0:
                continue

            if graph[current_position[0]][current_position[1]] != 0:
                continue

            new_node = Node(current_node, current_position)
            neighbours.append(new_node)

        for neighbour in neighbours:
            for closed in closed_nodes:
                if neighbour == closed:
                    continue

            neighbour.g = current_node.g + 1
            neighbour.h = calculate(neighbour, end_node)
            neighbour.f = neighbour.g + neighbour.h

            for opened in open_nodes:
                if neighbour == opened and neighbour.g > opened.g:
                    continue

            open_nodes.append(neighbour)
