
def solve(pos, path, graph, n):
    # Base condition: all vertices are included
    if pos == n:
        if graph[path[n - 1]][path[0]] == 1:
            print("Hamiltonian Cycle:", end=" ")
            print(*path, path[0], sep=" -> ")
            return True
        return False

    # Try each vertex
    for v in range(1, n):
        # Check edge and whether vertex is already used
        if graph[path[pos - 1]][v] == 1 and v not in path:
            path[pos] = v

            if solve(pos + 1, path, graph, n):
                return True

            # Backtracking
            path[pos] = -1

    return False


def hamiltonian(graph, n):
    path = [-1] * n
    path[0] = 0

    if not solve(1, path, graph, n):
        print("No Hamiltonian Cycle exists.")


n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 or 1):")

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

hamiltonian(graph, n)
