#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def bfs(G, start):
    Q = [start]
    visited = set()

    while Start:
        node = stack.pop(0)
        if node not in visited:
            visited.add(node)
            Q.extend(G[node] - visited)
    return visited
