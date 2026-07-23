class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        total = 0
        
        # Find the index of the tallest bar on the map
        peak_index = height.index(max(height))
        
        # 1. RUN YOUR LOGIC FORWARD (Stop at the peak)
        i = 0
        while i < peak_index:
            if height[i] == 0:
                i += 1
                continue
            temp_total = 0
            for j in range(i + 1, peak_index + 1):
                if height[j] < height[i]:
                    temp_total += (height[i] - height[j])
                if height[j] >= height[i]:
                    total += temp_total
                    i = j
                    break

        # 2. RUN YOUR EXACT LOGIC BACKWARDS (Start from the end, stop at the peak)
        i = len(height) - 1
        while i > peak_index:
            if height[i] == 0:
                i -= 1
                continue
            temp_total = 0
            for j in range(i - 1, peak_index - 1, -1):
                if height[j] < height[i]:
                    temp_total += (height[i] - height[j])
                if height[j] >= height[i]:
                    total += temp_total
                    i = j
                    break
                    
        return total