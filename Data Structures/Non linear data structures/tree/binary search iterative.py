class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def append(root,n):
    if root is None:
        return Node(n)
    else:
        curr = root
        while curr:
            if curr.data==n:
                return root
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')
def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
def search(root,n):
    if n==root:
        return root.data
    elif n<root.data:
        root.left=search(root,n)
    else:
        root.right=search(root,n)
    return root



if __name__=="__main__":
    root=None
    #node=Node(None)
    while True:
        n=int(input('enter'))
        if n>0:
            root =append(root,n)
        else:
            break
    while True:
        print('enter choice:1.in 2.post, 3.preorder, 4.search')
        ch=int(input('enter ch:'))
        if ch==1:
            print("inorder:",end=' ')
            inorder(root)
        if ch==2:
            print("postorder:", end=' ')
            postorder(root)
        if ch==3:
            print("preorder:", end=' ')
            preorder(root)
        if ch==4:
            print("search:")
            n=int(input('enter ele:'))
            search(root,n)




