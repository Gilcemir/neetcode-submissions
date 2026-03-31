class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = [(-x, i) for i, x in enumerate(nums[0:k])]
        heapq.heapify(heap)
        
        val, i = heap[0]
        top = -val
        
        res = []
        res.append(top)

        l = 1
        for r in range(k, len(nums)):
            while i < l:
                heapq.heappop(heap)
                if not heap:
                    break
                _, i = heap[0]
            
            heapq.heappush(heap, (-nums[r], r))

            val, i = heap[0]
            top = -val
            res.append(top)
            l += 1

        
        return res