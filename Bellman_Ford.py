class Graph:
    def __init__(self, vertices):
        self.M = vertices   
        self.graph = []     

    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])


    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for k in range(self.M):
            print("{0}\t\t{1}".format(k, distance[k]))


    def bellman_ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0
        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c

        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(distance)
if __name__ == '__main__':
    graph = Graph(10)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(4, 3, -5)
    graph.bellman_ford(0)
