class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def DFS(root):
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

DFS(a)


