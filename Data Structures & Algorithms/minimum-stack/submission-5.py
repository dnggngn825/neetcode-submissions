class MinStack:
    def __init__(self):
        self.stack = []
        self.mi = float('inf')

    def push(self, val: int) -> None:
        self.mi = min(val, self.mi)
        self.stack.append((val, self.mi))            

    def pop(self) -> None:
        self.stack.pop()
        self.mi = self.getMin() if len(self.stack) else float('inf')
            

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
