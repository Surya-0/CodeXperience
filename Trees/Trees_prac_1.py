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

        if curr.right is not None:
            stack.append(curr.right)

        if curr.left is not None:
            stack.append(curr.left)

def rec_DFS(root):
    if root == None:
        return []

    arr = [root.val]
    print("hi ",root.val)
    print("hi left",root.left)
    left_val = rec_DFS(root.left)
    print("hi right",root.right)
    right_val = rec_DFS(root.right)
    print("The left value is :",left_val)
    print("The right value is : ",right_val)
    arr.extend(left_val)
    arr.extend(right_val)
    print("The return array is :",arr)
    return arr



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
print("----------------")
print(rec_DFS(a))


