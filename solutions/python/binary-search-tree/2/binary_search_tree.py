class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, node):
        side = ('left', 'right')[node>self.data]
        try: getattr(self, side).add(node)
        except: setattr(self, side, TreeNode(node))

    def sort(self, nodes):
        if self.left: self.left.sort(nodes)
        nodes.append(self.data)
        if self.right: self.right.sort(nodes)
        return nodes

    def __str__(self):
        return (
        'TreeNode(data={}, left={}, right={}'
        .format(self.data, self.left, self.right)
        )


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = TreeNode(tree_data.pop(0))
        
        for node in tree_data:
            self.tree.add(node)

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.tree.sort([])
