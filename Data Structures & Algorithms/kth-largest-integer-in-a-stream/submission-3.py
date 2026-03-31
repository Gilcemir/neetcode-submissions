class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._pq, self._k = nums, k
        heapq.heapify(self._pq)
        while len(self._pq) > k:
            heapq.heappop(self._pq)
        

    def add(self, val: int) -> int:
        if len(self._pq) >= self._k:
            heapq.heappushpop(self._pq, val)
        else:
            heapq.heappush(self._pq, val)
        return self._pq[0]
        
