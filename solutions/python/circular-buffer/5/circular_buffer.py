class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.clear()

    def clear(self):
        self.buffer = {
        slot: None for slot in range(self.cap)
        }
        self.slot = self.cap
            
    def read(self):
        slots = {
        slot: val for slot, val in self.buffer.items()
        if val is not None
        }
        
        if not slots:
            raise BufferEmptyException('buffer empty')
            
        slot = min(slots)
        val = self.buffer[slot]
        self.buffer[slot] = None
        return val

    def write(self, data):
        empties = {
        slot: val for slot, val in self.buffer.items()
        if val is None
        }
        
        if not empties:
            raise BufferFullException('buffer full')
            
        del(self.buffer[min(empties)])
        self.slot += 1
        self.buffer[self.slot] = data

    def overwrite(self, data):
        del(self.buffer[min(self.buffer)])
        self.slot += 1
        self.buffer[self.slot] = data


