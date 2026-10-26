
INF = float('inf')

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 means no edge):")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex (0 to n-1): "))

distance = [INF] * n
visited = [False] * n

distance[source] = 0

for count in range(n):
    u = -1
    min_distance = INF


    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # Update distances of adjacent vertices
    for v in range(n):
        if (not visited[v] and graph[u][v] != 0
                and distance[u] + graph[u][v] < distance[v]):
            distance[v] = distance[u] + graph[u][v]

print("Shortest distances from source vertex", source, ":")
for i in range(n):
    if distance[i] == INF:
        print(f"To vertex {i}: INF")
    else:
        print(f"To vertex {i}: {distance[i]}")
