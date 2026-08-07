import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.kth = k
        heapq.heapify(self.heap)
        # list might have more than k elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.kth:   
            # maintain k elements in heap (so smallest in heap is kth largest)
            heapq.heappop(self.heap)
        return self.heap[0]
