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

    def shortest_paths_from_source(self, source):
        # Initialize distance array
        d = {vertex: float('inf') for vertex in self.graph}
        d[source] = 0

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
                    Q.put((alt, v))

        return d
    
    def nearest_three_points(self, source):
        distances = self.shortest_paths_from_source(source)
        # Filter points with distance less than 2
        # radius ကို ပြင်ချင်ရင် ဒီ ဂဏန်းကို ပြင်ပါ။
        # min_distance = 2
        min_distance = 3 * 1609.34 # 3 miles in meters
        filtered_distances = {point: distance for point, distance in distances.items() if distance < min_distance and point != source}
        # Sort the points by distance
        sorted_distances = sorted(filtered_distances.items(), key=lambda item: item[1])
        
        # Get the nearest three points
        nearest_three = [point for point, distance in sorted_distances][:3]
        # place id array ကို ပြန်ပေးမယ်။
        return nearest_three
    
        """
        distances = self.shortest_paths_from_source(source)
        sorted_distances = sorted(distances.items(), key=lambda item: item[1])

        # print(sorted_distances)
        # [('D', 0), ('B', 1), ('E', 1), ('F', 2), ('A', 3), ('C', 3)]
        
        # Exclude the source itself
        nearest_three = [point for point, distance in sorted_distances if point != source][:3]
        return nearest_three
        """

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
print(dijkstra.nearest_three_points('D'))  # Find the nearest 3 points to 'D'
