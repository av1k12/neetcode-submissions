class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        l = 0
        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                cur_prof = prices[r] - prices[l]
                if cur_prof > profit:
                    profit = cur_prof
            r += 1
        return profit