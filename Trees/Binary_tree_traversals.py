from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.left = left
        self.right = right
        self.val = val


# root left right
def preorder(node,res):
    if not node:
        return

    res.append(node.val)
    preorder(node.left,res)
    preorder(node.right,res)
    return

def postorder(node,res):
    if not node:
        return

    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.val)

    return

def inorder(node,res):
    if not node:
        return

    inorder(node.left,res)
    res.append(node.val)
    inorder(node.right,res)

    return

def dfs(node):
    if not node:
        return []

    res = [node.val]
    left = dfs(node.left)
    right = dfs(node.right)
    res.extend(left)
    res.extend(right)

    return res

def bfs(node):
    if not node:
        return []
    temp_q = deque()
    temp_q.append(node)
    res = []
    while temp_q:
        node = temp_q.popleft()
        res.append(node.val)
        if node.left:
            temp_q.append(node.left)

        if node.right:
            temp_q.append(node.right)
    return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

preorder_arr = []
inorder_arr = []
postorder_arr = []

preorder(a,preorder_arr)
inorder(a,inorder_arr)
postorder(a,postorder_arr)

print("preorder : ",preorder_arr)
print("postorder : ",postorder_arr)
print("inorder : ",inorder_arr)
print("The depth first traversal is : ",dfs(a))
print("The breadth first traversal is : ",bfs(a))





