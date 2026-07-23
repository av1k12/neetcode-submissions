class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0
        left = 0
        cur_max_prof = 0
        right = 1

        while right < (len(prices)):
            cur_prof = prices[right] - prices[left]
            if cur_prof > 0:
                if cur_prof > cur_max_prof:
                    cur_max_prof = cur_prof
            else:
                left = right
            right += 1
        return cur_max_prof
            
            
        