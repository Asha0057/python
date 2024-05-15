class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class circular:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        size=int(input())
        for i in range(size):
            data=int(input())
            newnode=Node(data)
            newnode.next=None
            if(self.head==None):
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next=newnode
                newnode.prev=self.tail
                self.tail=newnode
                self.head.prev = self.tail
                self.tail.next = self.head

    def display(self):
        temp=self.head
        while(temp.next!=self.head):
            print(temp.data,end=' ')
            temp=temp.next
        #print(temp.data)

    def insertfront(self):
        newnode=Node(int(input('enter :')))
        if(self.head==None):
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
            self.head.prev = self.tail
            self.tail.next = self.head
obj=circular()
obj.create()
obj.display()
obj.insertfront()
obj.display()
obj.insertend()
obj.display()
