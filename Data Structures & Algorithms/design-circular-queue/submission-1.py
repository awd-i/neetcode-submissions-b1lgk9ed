class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.cap = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        index = (self.head + self.count) % self.cap
        self.q[index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.count
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        index = self.head
        return self.q[index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.head + self.count - 1) % self.cap
        return self.q[index]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.cap:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()