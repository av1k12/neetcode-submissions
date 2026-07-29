class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        blah = {}
        for i in nums:
            blah[i] = 0
        
        ans = 0
        for i in blah:
            if i-1 not in blah and blah[i] == 0:
                counter = 1
                num = i
                while num+1 in blah:
                    counter += 1
                    num += 1
                    blah[num] = 1
                if counter > ans:
                    ans = counter
        return ans