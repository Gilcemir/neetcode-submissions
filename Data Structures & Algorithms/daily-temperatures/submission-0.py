class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        queue = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[i - 1]:
                peek = queue[-1]
                while temperatures[i] > temperatures[peek] and queue:
                    top = queue.pop()
                    res[top] = i - top
                    if queue:
                        peek = queue[-1]
            
            queue.append(i)
        
        return res
