class MinStack:

    def __init__(self):
        self.nums = []
        self.min_s = []
        

    def push(self, val: int) -> None:
        self.nums.append(val)
        self.min_s.append(min(val, self.min_s[-1]) if self.min_s else val)

    def pop(self) -> None:
        self.nums.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
