class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def append(root,n):
    if root is None:
        return Node(n)
    if n<root.data:
        root.left=append(root.left,n)
    else:
        root.right=append(root.right,n)
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
def search(root,s):
    curr = root
    while curr is not None:
        if curr.data == s:
            print(s, 'is present')
            return
        elif s < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    print(s, 'is not present')

    #return root
def deletion(root,d):
    if root is None:
        return root
    if d<root.data:
        root.left=deletion(root.left,d)
    if d>root.data:
        root.right=deletion(root.right,d)
    if root.left is None:
        temp=root.right
        root = None
        return temp
    if root.right is None:
        temp=root.left
        root=None
        return temp
    suc_par=root
    succ=root.right
    while succ.left is not None:
        suc_par=succ
        succ=succ.left
        root.data=succ.data
        if suc_par_left==succ:
            suc_par_left=succ.right
        else:
            suc_par_right=succ.right
            succ=None
    return root
"""def deletion(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deletion(root.left, key)
    elif key > root.data:
        root.right = deletion(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deletion(root.right, temp.data)
    return root
"""



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
        ch = int(input('enter ch:'))
        if ch == 1:
            print("inorder:", end=' ')
            inorder(root)
        if ch == 2:
            print("postorder:", end=' ')
            postorder(root)
        if ch == 3:
            print("preorder:", end=' ')
            preorder(root)
        if ch == 4:
            print("search:")
            s = int(input('enter ele:'))
            search(root, s)
        if ch==5:
            print('deletion:')
            d=int(input('enter element to del:'))





