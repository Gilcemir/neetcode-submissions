class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points]
        print(pq)
        return [(x, y) for _, x, y in heapq.nsmallest(k, pq)]