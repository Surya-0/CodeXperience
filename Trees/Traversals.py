class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def preorder_traversal(root,res):
    if root is None:
        return

    res.append(root.val)

    print("The value of the root is :",root.val)
    preorder_traversal(root.left,res)
    preorder_traversal(root.right,res)



    return

def postorder_traversal(root,res):
    if root is None:
        return

    print("The value of the root is :", root.val)
    postorder_traversal(root.left, res)
    postorder_traversal(root.right, res)

    res.append(root.val)

    return

def inorder_traversal(root,res):
    if root is None:
        return

    print("The value of the root is :",root.val)
    inorder_traversal(root.left,res)
    res.append(root.val)
    inorder_traversal(root.right,res)

    return



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

pre_res = []
preorder_traversal(a,pre_res)
print("The preorder traversal is : ",pre_res)

post_res = []
postorder_traversal(a,post_res)
print("The postorder traversal is : ",post_res)

in_res = []
inorder_traversal(a,in_res)
print("The inorder traversal is : ",in_res)