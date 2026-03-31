class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l_price = sys.maxsize
        for price in prices:
            if price < l_price:
                l_price = price
            
            proft = price - l_price
            if proft > res:
                res = proft
        
        return res

        