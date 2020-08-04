class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.length = 0
        self.index = 0

    def append(self, item):
        if self.length < self.capacity:
            self.data.append(item)
            self.length += 1
            print(self.data, self.index)

        elif self.length == self.capacity:
            self.data[self.index] = item
            self.index += 1

            if self.index == self.capacity:
                self.index = 0

    def get(self):
        return self.data