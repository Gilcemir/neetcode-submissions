class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = [0] * numCourses
        adj = defaultdict(list)
        # A dependência é do segundo para o primeiro, por isso é v, u e não u, v
        for v, u in prerequisites:
            deg[v] += 1
            adj[u].append(v)
        
        q = deque([v for v in range(numCourses) if deg[v] == 0])
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        
        return order if len(order) == numCourses else []

        