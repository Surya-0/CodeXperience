from collections import defaultdict


def is_special(weight):
    while weight > 0:
        digit = weight % 10
        if digit % 2 == 0:
            return False
        weight //= 10
    return True


def count_special_triplets(edges):
    # Build the graph
    graph = defaultdict(list)
    for v1, v2, weight in edges:
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))

    def dfs(node, parent):
        special_subtree_size[node] = 0
        subtree_size[node] = 1  # Include itself
        for neighbor, weight in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            if is_special(weight):
                special_subtree_size[node] += subtree_size[neighbor]  # Count all nodes in special subtree
                subtree_size[node] += subtree_size[neighbor]
            else:
                subtree_size[node] += subtree_size[neighbor]
                special_subtree_size[node] += special_subtree_size[neighbor]

    n = len(graph)
    special_subtree_size = [0] * (n + 1)
    subtree_size = [0] * (n + 1)

    dfs(1, -1)

    total_triplets = 0

    for node in range(1, n + 1):
        for neighbor, weight in graph[node]:
            if is_special(weight):
                remaining = subtree_size[1] - subtree_size[neighbor]  # Size of tree excluding this subtree
                total_triplets += special_subtree_size[neighbor] * remaining
            else:
                total_triplets += special_subtree_size[neighbor] * (subtree_size[1] - subtree_size[neighbor])

    return total_triplets


# Example usage:
edges = [[1, 2, 3], [2, 3, 35], [3, 4, 90], [1, 5, 7333]]
print(count_special_triplets(edges))
