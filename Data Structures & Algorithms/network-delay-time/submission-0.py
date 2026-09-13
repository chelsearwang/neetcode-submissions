import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float("inf")] * (n + 1) # index 0 unused, 0 based indexing
        distances[k] = 0

        graph = [[] for _ in range(n + 1)]
        for time in times:
            graph[time[0]].append((time[1], time[2])) # (ending node, weight)
        
        heap = [] # minheap to store (distance, node)
        heapq.heappush(heap, (0, k))
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]: # skip outdated heap entires
                continue
            neighbors = graph[node]
            for neighbor in neighbors:
                neighbor_node = neighbor[0]
                weight = neighbor[1]
                new_dist = dist + weight
                if new_dist < distances[neighbor_node]:
                    distances[neighbor_node] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor_node))
        max_dist = max(distances[1:]) # ignore index 0
        if max_dist == float("inf"):
            return -1
        return max_dist