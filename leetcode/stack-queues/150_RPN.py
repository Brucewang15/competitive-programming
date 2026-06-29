class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                result = 0
                if t == '+':
                    result = op1 + op2
                elif t == '-':
                    result = op2 - op1
                elif t == '*':
                    result = op1 * op2
                elif t == '/':
                    result = int(op2 / op1)
                stack.append(result)
        return stack[0]