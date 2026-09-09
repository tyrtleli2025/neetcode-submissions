class MinStack:
    def __init__(self):
        self.items = []
        self.minimums = [float('inf')]

    def push(self, val: int) -> None:
        self.items.append(val)
        if val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        value = self.items[-1]

        if value == self.minimums[-1]:
            minimum = self.minimums.pop()
        val = self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
