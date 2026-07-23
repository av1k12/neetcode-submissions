class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        val_Ops = {'+','-','*','/'} #why is a set faster for look ups

        for i in range(len(tokens)):
            n = tokens[i]
            if n not in val_Ops:
                stack.append(int(n))
            else:
                b = stack.pop()
                a = stack.pop()

                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(a - b)
                elif n == '*':
                    stack.append(a * b)
                elif n == '/':
                    stack.append(int(a/b))
         
        return int(stack[0])
        