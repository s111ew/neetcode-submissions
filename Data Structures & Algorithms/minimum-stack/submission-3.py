class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack == []:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[len(self.mins) - 1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.stack) - 1]
