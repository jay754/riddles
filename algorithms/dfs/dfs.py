#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs(G, start):
    stack = [start]
    visited = set()

    while Start:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(G[node] - visited)
    return visited
