class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # max heap, keep smallest distances
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap) # pop max
        result = []
        for item in heap:
            result.append(item[1])
        return result