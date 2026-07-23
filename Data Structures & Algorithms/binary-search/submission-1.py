class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = (len(nums)-1)//2
        l = 0
        r = len(nums) - 1

        while l < r:
            print("L: ", l)
            print("M: ", middle)
            print("R: ", r)
            print()
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
                middle = ((r - l) // 2) + l
            else:
                r = middle - 1
                middle = ((r-l)//2) + l
 
        if l == r:
            if nums[r] == target:
                return r
        
        return -1
        