class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.clear()

    def clear(self):
        self.readlist = [
        object() for slot in range(self.cap)
        ]
        self.writelist = []
            
    def read(self):
        try:
            slot = self.writelist.pop(0)
        except IndexError:
            raise BufferEmptyException('buffer empty')
        info = slot.data
        slot.data = None
        self.readlist.append(slot)
        return info

    def write(self, data):
        try:
            slot = self.readlist.pop(0)
        except IndexError:
            raise BufferFullException('buffer full')
        slot.data = data
        self.writelist.append(slot)

    def overwrite(self, data):
        try:
            slot = self.readlist.pop(0)
        except IndexError:
            slot = self.writelist.pop(0)
        slot.data = data
        self.writelist.append(slot)
