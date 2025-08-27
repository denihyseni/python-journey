import heapq as hq


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
}
visited = set()
node = [n for n in graph]
distance = {n: float('inf') for n in graph}
weight = 0
heap = []
distance['A'] = 0
hq.heappush(heap,(0,'A'))
while len(visited) < len(graph):
    current_distance, current_node = hq.heappop(heap)
    if current_node not in visited:
        visited.add(current_node)
    for neighbor , weight in graph[current_node]:
        new_distance = current_distance+ weight
        if new_distance < distance[neighbor]:
            distance[neighbor] = new_distance
            hq.heappush(heap,(new_distance,neighbor))
        

for node, dist in distance.items():
    print(f"Node {node} has shortest distance {dist}")
