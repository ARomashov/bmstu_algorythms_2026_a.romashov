from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTreeIterative(arr):
    if not len(arr) or arr[0] == None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    
    i = 1
    
    while i < len(arr):
        current = queue.pop()
        
        if i < len(arr) and arr[i] != None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] != None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        
        i += 1
        
    return root 


def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


if __name__ == '__main__':
    # Тест 1
    tree1 = buildTreeIterative([9, 16, 8, 6, 11])
    try:
        assert(levelOrder(tree1) == [[9], [16, 8], [6, 11]])
        print('Тест 1 пройден')
    except AssertionError:
        print('Тест 1 не пройден')
    
    # Тест 2
    tree2 = buildTreeIterative([3, 9, 20, 15, 7])
    try:
        assert levelOrder(tree2) == [[3], [9, 20], [15, 7]]
        print('Тест 2 пройден')
    except AssertionError:
        print('Тест 2 не пройден')  
    
    # Тест 3
    tree3 = buildTreeIterative([1, 2])
    tree3.left.left = TreeNode(3)
    try:
        assert levelOrder(tree3) == [[1], [2], [3]]  
        print('Тест 3 пройден')
    except:
        print('Тест 3 не пройден')
    
    