class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "/", "*"}
        stack = []
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(a + b)
                if t == "-":
                    stack.append(b - a)
                if t == "*":
                    stack.append(a * b)
                if t == "/":
                    if a == 0 or b == 0:
                        stack.append(0)
                    stack.append(int(b / a))
        return stack[-1]