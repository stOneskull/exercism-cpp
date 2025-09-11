class Node:
    def __init__(self, val, nextnode=None, prevnode=None):
        self.val = val
        self.nextnode = nextnode
        self.prevnode = prevnode
        
    def setnext(self, node):
        self.nextnode = node
        
    def setprev(self, node):
        self.prevnode = node


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def __iter__(self):
        node = self.start
        while node:
            yield node.val
            node = node.nextnode
            
    def push(self, val):
        node = Node(val, prevnode=self.end)
        if self.length:
            node.prevnode.setnext(node)
        else:
            self.start = node
        self.end = node
        self.length += 1
        
    def pop(self):
        self.length -= 1
        val = self.end.val
        if self.length:
            self.end = self.end.prevnode
            self.end.setnext(None)
        return val
        
    def unshift(self, val):
        node = Node(val, nextnode=self.start)
        if self.length:
            node.nextnode.setprev(node)
        else:
            self.end = node
        self.start = node
        self.length += 1
        
    def shift(self):
        self.length -= 1
        val = self.start.val
        if self.length:
            self.start = self.start.nextnode
            self.start.setprev(None)
        return val
