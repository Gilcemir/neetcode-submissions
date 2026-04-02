class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = list(zip(position, speed))
        tuples.sort()

        print(tuples)

        speed = (target - tuples[-1][0]) / tuples[-1][1]
        res = 1

        while tuples:
            p, s = tuples.pop()
            temp_speed = (target - p) / s
            print("speed: ", speed)
            print("temp_speed: ", temp_speed)
            if temp_speed > speed:
                res += 1
                speed = temp_speed
        
        return res
            