import heapq
class MedianFinder:

    def __init__(self):
        # store arr in two heaps: maxheap for left, minheap for right
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and self.right:
            if abs(self.left[0]) > num:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        if len(self.left) - len(self.right) > 1:
            temp = heapq.heappop(self.left)
            heapq.heappush(self.right, -temp)
        elif len(self.right) - len(self.left) > 1:
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -temp)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            l = -self.left[0]
            r = self.right[0]
            return (l+r)/2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]    
