class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        print(6 // -132)

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        
        return stack.pop()