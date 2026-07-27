class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return nums
        
        ans = []
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 1

        for i in range(k):
            max_key = max(seen, key=seen.get)
            ans.append(max_key)
            del seen[max_key]
        return ans

            
