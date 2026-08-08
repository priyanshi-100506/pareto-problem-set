import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements in the heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value into the heap first
        heapq.heappush(self.heap, val)
        
        # If the heap size exceeds k, pop the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of our min-heap is now the kth largest element
        return self.heap[0]
