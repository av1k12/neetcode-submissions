class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # Stores [start_index, height]
        
        for ind, h in enumerate(heights):
            # Track the furthest left this current height 'h' can stretch backward
            start = ind
            
            # Change 2 & 3: Use a while loop to pop all bars taller than the incoming one
            while stack and stack[-1][1] > h:
                pop_idx, pop_h = stack.pop()
                
                # Width is the current index minus where that popped bar originally started
                temp_area = pop_h * (ind - pop_idx)
                if temp_area > area:
                    area = temp_area
                    
                # Since the popped bar was taller than 'h', 'h' can extend backward 
                # into the space that the popped bar occupied.
                start = pop_idx
            
            # Change 1: Push the pair containing the updated start index and height
            stack.append([start, h])
                    
        # Final Clean-up: Process any bars left stranded in the stack that managed
        # to stretch all the way to the very end of the histogram
        while stack:
            pop_idx, pop_h = stack.pop()
            temp_area = pop_h * (len(heights) - pop_idx)
            if temp_area > area:
                area = temp_area

        return area