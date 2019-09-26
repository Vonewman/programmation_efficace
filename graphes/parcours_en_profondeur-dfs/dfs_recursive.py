def dfs_recursive(graph, node, seen):
    """
    DFS implementation in a recursive way.
    """
    seen[node] = True
    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs_recursive(graph, neighbor, seen)
