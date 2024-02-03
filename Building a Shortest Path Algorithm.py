my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    """
    Find the shortest path from the 'start' node to the 'target' node (or all nodes if 'target' is not specified)
    in a weighted graph.

    Parameters:
        graph (dict): A dictionary representing a weighted graph.
        start (str): The starting node for the path.
        target (str, optional): The target node to find the path to. If not specified, paths to all nodes will be printed.

    Returns:
        tuple: A tuple containing dictionaries of distances and paths.
               distances (dict): A dictionary containing the minimum distances from the 'start' node to each node.
               paths (dict): A dictionary containing the paths from the 'start' node to each node.
    """
    # List of unvisited nodes
    unvisited = list(graph)

    # Dictionary to store distances from start to each node
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Dictionary to store paths from start to each node
    paths = {node: [] for node in graph}
    paths[start].append(start)

    # Dijkstra's algorithm
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                # Update distance
                distances[node] = distance + distances[current]

                # Update path
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)

        # Remove the current node from the unvisited list
        unvisited.remove(current)

    # Print results
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths

# Example usage
shortest_path(my_graph, 'A', 'F')
