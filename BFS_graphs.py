g = {1: [2, 3, 4], 2: [3, 6], 3:[5], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [9]}
k = list(g.keys())

def bfs(graph):
    visited = set()

    def bfs_visit(graph, start):
        queue = []

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    for i in k:
        if i not in visited:
            bfs_visit(g, i)


bfs(g)