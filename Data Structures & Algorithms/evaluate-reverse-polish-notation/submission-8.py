class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        print(6 // -132)

        for token in tokens:
            if token == "+":
                print("before +:", stack)
                stack.append(stack.pop() + stack.pop())
                print("after +:", stack)
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                print("before -:", stack)
                stack.append(val2 - val1)
                print("after -:", stack)
            elif token == "*":
                print("before *:", stack)
                stack.append(stack.pop() * stack.pop())
                print("after *:", stack)
            elif token == "/":
                print("before /:", stack)
                val1 = stack.pop()
                val2 = stack.pop()
                print("val2:", val2, " // val1:", val1)
                stack.append(int(val2 / val1))
                print("after /:", stack)
            else:
                stack.append(int(token))
                print("appended:", stack)
        
        return stack.pop()