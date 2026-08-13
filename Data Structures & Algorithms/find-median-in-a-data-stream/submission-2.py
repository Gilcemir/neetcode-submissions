"""
slots deve produzir:
Quantidade de numeros -> slots
0 -> 0
1, 2 -> 1
3, 4 -> 2
5, 6 -> 3

Assim, upper_pq será a heap de entrada; se estiver cheia, ela remove o menor e joga
para a fila de lower.

returnar a média então é trivial (código auto descritivo)
"""

class MedianFinder:

    def __init__(self):
        self.upper_pq = []
        self.lower_pq = []
        self.count = 0

    def slots(self) -> int:
        return (self.count + 1) // 2        

    def addNum(self, num: int) -> None:
        self.count += 1
        # vazio
        if not self.upper_pq:
            heapq.heappush(self.upper_pq, num)
            return
        # se o novo número é menor que upper limit, deve entrar no lower limit
        if num < self.upper_pq[0]:
            # se tem espaço, adiciona 
            if len(self.lower_pq) < self.slots():
                heapq.heappush_max(self.lower_pq, num)
            #se não tem, remove, e joga o maior para fila dos maiores, depois insere
            else:
                popped = heapq.heappushpop_max(self.lower_pq, num)
                heapq.heappush(self.upper_pq, popped)
        else:
            if len(self.upper_pq) < self.slots():
                heapq.heappush(self.upper_pq, num)
            else:
                popped = heapq.heappushpop(self.upper_pq, num)
                heapq.heappush_max(self.lower_pq, popped)


    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.upper_pq[0] + self.lower_pq[0]) / 2 
        if len(self.upper_pq) > len(self.lower_pq):
            return self.upper_pq[0]
        return self.lower_pq[0]
        
        