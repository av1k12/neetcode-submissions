class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        pairs = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            print('c: ', c)
            if (c in pairs):
                stack.append(c)
            elif ((len(stack) < 1) or (c != pairs.get(stack[-1]))):
                return False
            else:
                stack.pop()
                print('matched so popped')
            print('stack: ', stack, '\n')
        return len(stack) == 0