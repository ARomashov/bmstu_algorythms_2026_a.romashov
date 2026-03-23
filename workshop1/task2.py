class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, arr=None):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    def pop(self):
        if self.top is None:
            return -1
        
        top = self.top
        self.top = self.top.next
        return top


def sort_stack():
    return 

stack1 = Stack()
for i in range(0, 10):
    stack1.push(i)
