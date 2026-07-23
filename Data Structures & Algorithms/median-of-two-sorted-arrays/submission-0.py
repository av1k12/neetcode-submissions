class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Change 1: Ensure nums1 is always the smaller array to binary search efficiently
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Change 2: Set binary search pointers strictly on the smaller array A
        l = 0
        r = len(A) - 1
        
        # Change 3: Run partition binary search
        while True:
            # Calculate mid index for array A
            m = (r + l) // 2 if (r + l) >= 0 else -1
            # Calculate corresponding partition index for array B
            m2 = half - (m + 1) - 1
            
            # Identify edge values around the partition cuts
            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m + 1] if (m + 1) < len(A) else float('inf')
            Bleft = B[m2] if m2 >= 0 else float('-inf')
            Bright = B[m2 + 1] if (m2 + 1) < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2 != 0:
                    return min(Aright, Bright)
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1 # Reduce elements from array A's left side
            else:
                l = m + 1 # Take more elements from array A's left side