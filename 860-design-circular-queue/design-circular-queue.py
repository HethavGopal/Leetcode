class MyCircularQueue:
    def __init__(self, k: int):
        self.head = 0
        self.tail = 0  # Next insertion position
        self.size = 0
        self.k = k
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.tail] = value
        self.size += 1

        self.tail += 1
        if self.tail == self.k:
            self.tail = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.head] = None
        self.size -= 1

        self.head += 1
        if self.head == self.k:
            self.head = 0

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        index = self.tail - 1
        if index < 0:
            index = self.k - 1

        return self.q[index]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k