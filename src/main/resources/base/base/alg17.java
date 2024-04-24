public static void dijkstra(int[][] graph, int startNode) {
        int nVertices = graph.length;
        int[] shortestDistances = new int[nVertices];
        boolean[] added = new boolean[nVertices];

        Arrays.fill(shortestDistances, Integer.MAX_VALUE);
        Arrays.fill(added, false);

        shortestDistances[startNode] = 0;

        for (int i = 1; i < nVertices; i++) {
        int nearestVertex = -1;
        int shortestDistance = Integer.MAX_VALUE;
        for (int vertexIndex = 0; vertexIndex < nVertices; vertexIndex++) {
        if (!added[vertexIndex] && shortestDistances[vertexIndex] < shortestDistance) {
        nearestVertex = vertexIndex;
        shortestDistance = shortestDistances[vertexIndex];
        }
        }

        added[nearestVertex] = true;

        for (int vertexIndex = 0; vertexIndex < nVertices; vertexIndex++) {
        int edgeDistance = graph[nearestVertex][vertexIndex];

        if (edgeDistance > 0 && ((shortestDistance + edgeDistance) < shortestDistances[vertexIndex])) {
        shortestDistances[vertexIndex] = shortestDistance + edgeDistance;
        }
        }
        }
        }