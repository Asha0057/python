class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def append(root,n):
    if root is None:
        return Node(n)
    else:
        curr=root
        curr1=root
        flag=0
    while True:
        if curr.left is None:
            curr.left=Node(n)
            break
        elif curr.right is None:
            curr.right=Node(n)
            break
        elif flag==0:
            curr=curr1.left
            flag=1
        else:
            curr=curr1.right
            flag=0
            curr1=curr1.left
    return root
def inorder(curr):
    if curr:
        inorder(curr.left)
        print(curr.data,end=' ')
        inorder(curr.right)
def postorder(curr):
    if curr:
        postorder(curr.left)
        postorder(curr.right)
        print(curr.data, end=' ')
def preorder(curr):
    if curr:
        print(curr.data,end=' ')
        preorder(curr.left)
        preorder(curr.right)
if __name__=="__main__":
    root=None
    #node=Node(None)
    while True:
        n=int(input('enter'))
        if n>0:
            root =append(root,n)
        else:
            break
    print("inorder:",end=' ')
    inorder(root)
    print("postorder:", end=' ')
    postorder(root)
    print("preorder:", end=' ')
    preorder(root)




