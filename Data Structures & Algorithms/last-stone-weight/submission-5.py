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
        
        pq.append(0) # se tem, adiciona e nao faz difernça, se nao tem, retorna 0
        return abs(pq[0])