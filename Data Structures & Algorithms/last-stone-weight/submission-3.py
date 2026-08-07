import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append((-1)*i)
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = heap[0]
            heapq.heappop(heap)
            stone2 = heap[0]
            heapq.heappop(heap)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(heap, -(abs(stone1-stone2)))
            heapq.heapify(heap)
            # print(heap)
        if len(heap) == 0:
            return 0
        return abs(heap[0])