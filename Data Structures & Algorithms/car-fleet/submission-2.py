class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #[[],[]]

        joined = list(zip(position, speed))
        sort = sorted(joined, reverse = True)

        for p, s in sort:
            time = (target - p) / s
            if stack and stack[-1] < time:
                stack.append(time)
            elif len(stack) == 0:
                stack.append(time)

        return len(stack)

