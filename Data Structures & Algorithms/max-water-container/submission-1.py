class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) - 1

        while l <= r:
            area = (r-l) * min(heights[r], heights[l])
            print(area)
            max_water = max(area, max_water)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water