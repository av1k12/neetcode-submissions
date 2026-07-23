class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                h = min(heights[i], heights[j])
                area = h * width
                if area > max_val:
                    max_val = area
        return max_val