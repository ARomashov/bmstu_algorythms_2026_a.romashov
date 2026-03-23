class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        self.tail = None

        for elem in arr:
            self.push(elem)

    def get_head(self):
        return self.head
    
    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node 
            self.tail = node 

def find_intersection(head_A, head_B):
    pA, pB = head_A, head_B
    while pA != pB:
        if pA is None: 
            pA = head_B
        if pB is None:
            pB = head_A

        pA = pA.next
        pB = pB.next
    return pA

# Тесты
arr1, arr2 = [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]
list1 = LinkedList([4])
list2 = LinkedList([5, 6])
intersection = LinkedList([1, 8, 4, 5])
#list1.tail.next = intersection.get_head()
#list2.tail.next = intersection.get_head()

curr_node = list2.get_head()
print(find_intersection(list1.get_head(), list2.get_head())) # None

list1 = LinkedList([3, 6])
list2 = LinkedList([1])
intersection = LinkedList([8, 9, 6])
list1.tail.next = intersection.get_head()
list2.tail.next = intersection.get_head()

print(find_intersection(list1.get_head(), list2.get_head()).value)