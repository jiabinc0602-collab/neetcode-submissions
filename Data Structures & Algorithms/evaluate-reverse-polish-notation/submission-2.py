class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop1 + pop2)
            elif i == "-":
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2 - pop1)
            elif i == "*":
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop1 * pop2)
            elif i == "/":
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2 / pop1)
            else:
                stack.append(i)
        return int(stack.pop())