import random

class Robot:
    names = []

    def __init__(self):
        self.reset()

    def reset(self):
        while True:
            name = ''
            for char in range(2):
                name += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for num in range(3):
                name += str(random.choice(range(10)))
            if name in Robot.names:
                continue
            Robot.names.append(name)
            self.name = name
            break
