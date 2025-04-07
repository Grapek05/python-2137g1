graph = {
    'A':{'B': 4, 'C': 2},
    'B':{'D': 1, 'C': 5},
    'C':{'D': 8, 'F': 2},
    'D':{'F': 2},
    'F':{}
}


def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(graph):
            current_node = None
            for node in graph:
                if node not in visited:
                    if current_node is None or distances[node] < distances[current_node]:
                        current_node = node

            if current_node is None:
                break

            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

            visited.add(current_node)

            return distances
        
if __name__ == "__main__":
    start_node = 'A'
    result = dijkstra(graph, start_node)
    print(f"Shortest distances from node {start_node}: {result}")