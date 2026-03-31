class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []

    def push(self, val: int) -> None:
        if len(self.mn) == 0 or val <= self.mn[-1]:
            self.mn.append(val)
        else:
            self.mn.append(self.mn[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mn:
            return self.mn[-1]
