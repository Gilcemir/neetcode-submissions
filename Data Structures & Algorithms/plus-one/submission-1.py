class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1
        result = []
        while last >= 0:
            if digits[last] == 9:
                digits[last] = 0
            else:
                digits[last] += 1
                return digits
            last -= 1
        
        return [1] + digits
        