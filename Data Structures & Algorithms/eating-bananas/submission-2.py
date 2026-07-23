class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Change 1: Search the range of possible speeds, not the array indices
        l = 1
        r = max(piles)
        
        # We want to find the lowest valid speed, so track it globally
        ans = r

        while l <= r:
            m = (r + l) // 2
            hours = 0
            
            for i in piles:
                # Change 2: Use floor division to find whole hours
                whole = i // m
                hours += whole
                if (i % m) > 0:
                    hours += 1
            
            # Change 3: Shift pointers based on whether Koko made the deadline
            if hours <= h:
                ans = m     # This speed works! Save it as a candidate
                r = m - 1   # Try to see if an even slower speed works
            else:
                l = m + 1   # Too slow, force Koko to speed up
                
        return ans