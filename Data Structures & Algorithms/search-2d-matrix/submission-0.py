class Solution:
    def searchMatrix(self, matrix: List[List[List[int]]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Treat the matrix as a single flat array stretching from 0 to total elements - 1
        l = 0
        r = (rows * cols) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Map the 1D index 'mid' directly to its 2D coordinates
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1 # Target is to the right
            else:
                r = mid - 1 # Target is to the left
                
        return False