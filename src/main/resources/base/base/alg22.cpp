    void dijkstra(const std::vector<std::vector<int>>& graph, int startNode) {
        int nVertices = graph.size();
        std::vector<int> shortestDistances(nVertices, std::numeric_limits<int>::max());
        std::vector<bool> added(nVertices, false);

        shortestDistances[startNode] = 0;

        for (int i = 1; i < nVertices; i++) {
            int nearestVertex = -1;
            int shortestDistance = std::numeric_limits<int>::max();
            for (int vertexIndex = 0; vertexIndex < nVertices; vertexIndex++) {
                if (!added[vertexIndex] && shortestDistances[vertexIndex] < shortestDistance) {
                    nearestVertex = vertexIndex;
                    shortestDistance = shortestDistances[vertexIndex];
                }
            }

            added[nearestVertex] = true;

            for (int vertexIndex = 0; vertexIndex < nVertices; vertexIndex++) {
                if (graph[nearestVertex][vertexIndex] > 0) {
                    int edgeDistance = graph[nearestVertex][vertexIndex];
                    if (shortestDistance + edgeDistance < shortestDistances[vertexIndex]) {
                        shortestDistances[vertexIndex] = shortestDistance + edgeDistance;
                    }
                }
            }
        }
    }