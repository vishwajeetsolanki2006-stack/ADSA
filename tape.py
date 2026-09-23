
INF = float('inf')


def min_key(key, mst_set, V):
    minimum = INF
    min_index = -1

    for v in range(V):
        if not mst_set[v] and key[v] < minimum:
            minimum = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    V = len(graph)

    parent = [-1] * V

    key = [INF] * V

    mst_set = [False] * V

    key[0] = 0

    for _ in range(V - 1):


        u = min_key(key, mst_set, V)

        mst_set[u] = True

        for v in range(V):
            if (
                graph[u][v] != 0
                and not mst_set[v]
                and graph[u][v] < key[v]
            ):
                parent[v] = u
                key[v] = graph[u][v]

    print("Edge\tWeight")

    total_weight = 0

    for i in range(1, V):
        weight = graph[i][parent[i]]
        print(f"{parent[i]} - {i}\t{weight}")
        total_weight += weight

    print("Total weight:", total_weight)
