class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adv: dict[int, list[int]] = defaultdict(list)
        for u, v in prerequisites:
            adv[u].append(v)
        
        deg: list[int] = [0] * numCourses
        for _, v in prerequisites:
            deg[v] += 1
        
        q = deque([v for v in range(numCourses) if deg[v] == 0])

        while q:
            u = q.popleft()
            for v in adv[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        for v in deg:
            if v != 0:
                return False
                
        return True
        