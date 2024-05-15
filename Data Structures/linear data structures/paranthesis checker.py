class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top = newnode