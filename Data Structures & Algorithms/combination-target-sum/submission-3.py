class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start_idx: int, current_combo: list[int], remaining: int):
            # Base Case 1: Found a valid combination
            if remaining == 0:
                res.append(list(current_combo))  # make a copy
                return

            # Base Case 2: Exceeded target
            if remaining < 0:
                return

            # Explore choices from start_idx to end
            for i in range(start_idx, len(nums)):
                val = nums[i]
                # 1. Choose
                current_combo.append(val)
                # 2. Recurse (pass i again, not i + 1, because we can reuse the same element)
                backtrack(i, current_combo, remaining - val)
                # 3. Un-choose (Backtrack)
                current_combo.pop()

        backtrack(0, [], target)
        return res