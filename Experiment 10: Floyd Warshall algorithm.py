
INF = float('inf')

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix (use INF for no edge):")
graph = []

for i in range(n):
    row = input().split()
    graph.append([INF if x.upper() == "INF" else int(x) for x in row])

dist = [row[:] for row in graph]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

print("Shortest distance matrix:")
for row in dist:
    print(*["INF" if x == INF else int(x) for x in row])
