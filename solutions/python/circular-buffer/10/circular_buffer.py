class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.clear()

    def clear(self):
        self.written = []
        self.empties = [
        lambda:23 for slot in range(self.cap)
        ]
            
    def read(self):
        try:
            slot = self.written.pop(0)
        except IndexError:
            raise BufferEmptyException('buffer empty')
        data = slot.data
        slot.data = None
        self.empties.append(slot)
        return data

    def write(self, data):
        try:
            slot = self.empties.pop(0)
        except IndexError:
            raise BufferFullException('buffer full')
        slot.data = data
        self.written.append(slot)

    def overwrite(self, data):
        try:
            slot = self.empties.pop(0)
        except IndexError:
            slot = self.written.pop(0)
        slot.data = data
        self.written.append(slot)
