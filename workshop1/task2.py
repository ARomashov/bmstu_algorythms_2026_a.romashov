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
        return top.value


def sort_stack(stack):
    temp = Stack()
    while stack.top is not None:
        if temp.top is None:
            temp.push(stack.pop())

        stack_top = stack.pop()
        if stack_top < temp.top.value:
            stack.push(temp.pop())
            temp.push(stack_top)
        else:
            temp.push(stack_top)
    
    while temp.top is not None:
        stack.push(temp.pop())
    return stack

stack1 = Stack()
stack1.push(2)
stack1.push(3)
stack1.push(1)
stack1.push(4)

sorted_stack = sort_stack(stack1)
while sorted_stack.top is not None:
    print(sorted_stack.pop()) # Неправильно выводит (