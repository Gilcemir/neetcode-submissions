class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)
            rs = abs(x - y)
            if rs > 0:
                heapq.heappush(pq, -rs)
        
        return abs(pq[0]) if len(pq) == 1 else 0