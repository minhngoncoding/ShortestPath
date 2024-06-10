Members list:
1) Đặng Minh Ngôn
2) Lã Minh Tuấn Kiệt
3) Trần Vĩnh Tiến 
4) Nguyễn Thành Lộc
5) Huỳnh Thanh Tân

1. Bellman Ford:
Step 1: Initialize distances from src to all other vertices
Step 2: Relax all edges |V| - 1 times. A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
Step 3: check for negative-weight cycles. The above step guarantees shortest distances if graph doesn't contain negative weight cycle. If we get a shorter path, then there is a cycle.

2. Floyd Warshall
- dist[][] will be the output matrix that will finally have the shortest distances between every pair of vertices initializing the solution matrix same as input graph matrix or we can say that the initial  values of shortest distances are based on shortest paths considering no intermediate vertices
Step 1: Add all vertices one by one to the set of intermediate vertices. 
Step 2: Before start of an iteration, we have shortest distances between all pairs of vertices such that the shortest distances consider only the vertices in the set {0, 1, 2, .. k-1} as intermediate vertices.
Step 3: After the end of a iteration, vertex no. k is added to the set of intermediate vertices and the set becomes {0, 1, 2, .. k}

3.top-k-shortest-path.py
Input:
        graph: A dictionary where keys are nodes and values are dictionaries mapping neighbors to their weights (in json file).
        source: The starting node.
        target: The ending node.
        k: The number of shortest paths to find.

Output
        A list contain a path length (in meter) and sub-list is a full path between start and end node.