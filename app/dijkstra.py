from queue import PriorityQueue


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, source, target):
        # Initialize distance array
        d = {vertex: float('inf') for vertex in self.graph}
        d[source] = 0

        # Initialize predecessor array
        pi = {vertex: None for vertex in self.graph}

        # Priority queue for vertices
        Q = PriorityQueue()

        # Add source vertex to queue
        Q.put((0, source))

        while not Q.empty():
            # Extract min cost
            cost, u = Q.get()

            if u not in self.graph:
                continue

            # Relax each adjacent vertex
            for v, edge_cost in self.graph[u].items():
                alt = d[u] + edge_cost
                if alt < d[v]:
                    d[v] = alt
                    pi[v] = u
                    Q.put((alt, v))

        # Traverse from target to source
        S = []
        u = target
        dist = 0

        while pi[u] is not None:
            S.append(u)
            dist += self.graph[u][pi[u]]
            u = pi[u]

        S.append(source)
        S.reverse()

        # Construct solution dictionary
        solution = {"status": "route", "distance": dist, "solution_path": S}

        if pi[target] is None:
            solution["status"] = "no_route"
            solution["err_msg"] = f"No route from {source} to {target}"

        return solution


graph = {
    'A': {'B': 3, 'D': 3, 'F': 6},
    'B': {'A': 3, 'D': 1, 'E': 3},
    'C': {'E': 2, 'F': 3},
    'D': {'A': 3, 'B': 1, 'E': 1, 'F': 2},
    'E': {'B': 3, 'C': 2, 'D': 1, 'F': 5},
    'F': {'A': 6, 'C': 3, 'D': 2, 'E': 5},
}

# Usage
dijkstra = Dijkstra(graph)
print(dijkstra.shortest_path('D', 'C'))  # Example usage
