class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._pq = nums
        heapq.heapify(self._pq)
        self._k = k        

    def add(self, val: int) -> int:
        heapq.heappush(self._pq, val)
        return heapq.nlargest(self._k, self._pq)[self._k - 1]
        
