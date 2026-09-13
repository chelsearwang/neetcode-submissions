import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)] # (cost, point), where point is idx in points arr
        total_cost = 0

        while heap and len(visited) < n:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue # alr connected
            # add current point
            visited.add(point)
            total_cost += cost
            # consider connecting this point to every unvisited point
            for neighbor in range(n):
                if neighbor in visited:
                    continue
                # calculate Manhattan distance
                distance = abs(points[point][0] - points[neighbor][0]) + abs(points[point][1] - points[neighbor][1])
                heapq.heappush(heap, (distance, neighbor))

        return total_cost