class Zipper:
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, tree, depth=[]):
        self.tree = tree
        self.depth = depth

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        self.tree['value'] = value
        return self

    def left(self):
        if self.tree['left']:
            return Zipper(
                self.tree['left'],
                self.depth + [self.tree]
            )

    def set_left(self, tree):
        self.tree['left'] = tree
        return self

    def right(self):
        if self.tree['right']:
            return Zipper(
                self.tree['right'],
                self.depth + [self.tree]
            )

    def set_right(self, tree):
        self.tree['right'] = tree
        return self

    def up(self):
        if not self.depth:
            return
        return Zipper(
            self.depth[-1], self.depth[:-1]
        )

    def to_tree(self):
        return (
            self.depth[0] if self.depth
            else self.tree
        )
