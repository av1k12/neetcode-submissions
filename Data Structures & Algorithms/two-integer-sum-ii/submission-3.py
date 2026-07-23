class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1 = 0
        for n1 in numbers:
            if (target - n1) in numbers:
                array = [numbers.index(n1) + 1, numbers.index(target - n1) + 1]
                return array

        return [0,0]