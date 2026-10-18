# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))

            current_arch_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_arch_sum)

            return node.val + max(left_gain, right_gain)
        get_max_gain(root)
        return max_sum