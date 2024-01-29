class MyQueue:

    def __init__(self):
        self.f = []
        self.s = []

    def push(self, x: int) -> None:
        while self.f:
            self.s.append(self.f.pop())
        self.f.append(x)
        while self.s:
            self.f.append(self.s.pop())

    def pop(self) -> int:
        return self.f.pop() if self.f else None

    def peek(self) -> int:
        return self.f[-1] if self.f else None

    def empty(self) -> bool:
        return len(self.f) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()