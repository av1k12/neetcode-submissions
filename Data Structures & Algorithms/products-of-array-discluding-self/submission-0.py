class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        final = [1] * length
        
        prefix = 1
        for i in range(length):
            final[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length - 1, -1, -1):
            final[i] *= postfix
            postfix *= nums[i]
            
        return final