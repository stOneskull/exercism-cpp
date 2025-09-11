class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.ladies = set()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for lady in self.ladies: lady.update()
        for lady in self.ladies: lady.makecalls()


class ComputeCell:
    def __init__(self, cells, function):
        
        for cell in cells: cell.ladies.add(self)
        
        self.cells = cells
        self.function = function
        
        self.ladies = set()
        self.callbacks = set()
        
        self.update()
        self.old_value = self.value

    def update(self):
        values = [cell.value for cell in self.cells]
        self.value = self.function(values)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)

    def makecalls(self):
        if self.value == self.old_value: return
        
        for call in self.callbacks: call(self.value)
        
        for lady in self.ladies: lady.update()
        for lady in self.ladies: lady.makecalls()
