class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)
            print(x, y)
            print(pq)
            rs = abs(x - y)
            print(rs)
            if rs > 0:
                heapq.heappush(pq, -rs)
            print()
        
        return abs(pq[0]) if len(pq) == 1 else 0