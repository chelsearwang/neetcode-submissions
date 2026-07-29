from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1+num2)
            elif token == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1-num2)
            elif token == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1*num2)
            elif token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1/num2)
            else:
                stack.append(token)
        return int(stack.pop())