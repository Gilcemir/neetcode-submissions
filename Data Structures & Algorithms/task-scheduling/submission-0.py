class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = deque([(0, v) for v in Counter(tasks).values()])
        pq = []

        while pq or queue:
            while queue and queue[0][0] <= time:
                _, count = queue.popleft()
                heapq.heappush_max(pq, count)
            if not pq:
                time = queue[0][0]
                continue
            
            time += 1
            count = heapq.heappop_max(pq) - 1
            if count:
                queue.append((time + n, count))
            
        return time
        