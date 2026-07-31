class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # não precisa de elevar ao quadrado porque é monotonico, a raiz é só uma op a mais.
        pq = [(x ** 2 + y ** 2, x, y) for x, y in points]
        return [(x, y) for _, x, y in heapq.nsmallest(k, pq)]